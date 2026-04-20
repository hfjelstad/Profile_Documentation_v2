#!/usr/bin/env python3
"""
check-doc-consistency.py

Consistency checks for NeTEx Nordic Profile documentation.

Three checks:
  1. XSD  — Validate all Example_*.xml wrapped in PublicationDelivery.
  2. Order — Table Structure Overview element order matches the XML example
             in the same directory.
  3. Desc  — Description Structure Overview top-level elements match the
             Table Structure Overview (same set, same order).

Usage:
    python scripts/check-doc-consistency.py             # all checks
    python scripts/check-doc-consistency.py --xsd-only
    python scripts/check-doc-consistency.py --order-only
    python scripts/check-doc-consistency.py --desc-only
    python scripts/check-doc-consistency.py --target Frames/ServiceFrame

Exit code 0 = all clear, 1 = errors found.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Optional

WORKSPACE = Path(__file__).resolve().parent.parent
XSD_PATH = WORKSPACE / "XSD" / "xsd" / "NeTEx_publication.xsd"

# ──────────────────────────────────────────────────────────────────────────────
# Structure Overview parsers
# ──────────────────────────────────────────────────────────────────────────────

def _extract_code_block(md_text: str) -> Optional[str]:
    """Return the content of the first ```text ... ``` block, or None."""
    m = re.search(r"```text\s*\n(.*?)```", md_text, re.DOTALL)
    return m.group(1) if m else None


def parse_table_overview(md_path: Path) -> Optional[List[str]]:
    """
    Extract depth-1 non-attribute element names from a Table_*.md
    Structure Overview.

    Depth-1 lines look like:
        ' ├─ routes (0..1)'   or   ' └─ notices (0..1)'
    They start with exactly one space then a box-drawing character.
    Deeper lines start with ' │' (space + pipe) and are ignored.
    """
    text = md_path.read_text(encoding="utf-8")
    block = _extract_code_block(text)
    if block is None:
        return None

    elements: List[str] = []
    for line in block.splitlines():
        # Depth-1: starts with exactly ' ├' or ' └' (1 space then box char)
        if not re.match(r"^ [├└]", line):
            continue
        # Strip all leading tree decoration
        raw = re.sub(r"^[ ├└─\s]+", "", line).strip()
        if not raw:
            continue
        name = raw.split()[0]
        if name.startswith("@"):
            continue  # skip attributes
        # 'OperatorRef/@ref' → 'OperatorRef'
        name = name.split("/")[0]
        elements.append(name)
    return elements or None


def parse_desc_overview(md_path: Path) -> Optional[List[str]]:
    """
    Extract the direct-child element names from a Description_*.md Structure
    Overview code block, skipping attribute names (@id, @version, etc.).

    Two formats are in use:

    **Flat format** (typical for Frames, e.g. Description_ServiceFrame.md):
        Children are at depth-0, each starting with an emoji icon at column 0:
            📄 @id (1..1)
            📁 routes (0..1)

    **Nested format** (typical for Objects, e.g. Description_Contract.md):
        The root object is at depth-0 alone, children are at depth-1 indented
        with two spaces then a tree character:
            📄 Contract
              ├─ 📄 @id (1..1)
              ├─ 📄 Name (0..1)

    Detection: if there is exactly ONE depth-0 emoji line and it has no
    cardinality annotation (e.g. no parentheses), the nested format is assumed.
    """
    text = md_path.read_text(encoding="utf-8")
    block = _extract_code_block(text)
    if block is None:
        return None

    lines = block.splitlines()

    # ── Collect depth-0 emoji lines (col 0) ──────────────────────────────────
    ICON_RE = re.compile(r"^[📄📁🔗]")  # emoji at col 0
    depth0: List[str] = []
    for line in lines:
        if not ICON_RE.match(line):
            continue
        raw = re.sub(r"^[📄📁🔗]\s+", "", line).strip()
        if not raw:
            continue
        name = raw.split()[0].split("/")[0]
        if not name.startswith("@"):
            depth0.append(name)

    # ── Detect nested format ──────────────────────────────────────────────────
    # Nested format: exactly one depth-0 element and it has no cardinality
    # annotation like (0..1) or (0..n) on the same line (bare object name).
    first_line_remainder = (
        block.split(depth0[0], 1)[1].split("\n")[0] if depth0 else ""
    )
    use_nested = (
        len(depth0) == 1
        and not re.search(r"\d+\.\.[0-9n]", first_line_remainder)
    )

    if use_nested:
        # Extract depth-1 children: lines with exactly 2-space indent + tree char
        # e.g. '  ├─ 📄 Name (0..1)' or '  └─ 📁 contractees (0..1)'
        DEPTH1_RE = re.compile(r"^  [├└]─\s+[📄📁🔗]?\s*(.+)")
        children: List[str] = []
        for line in lines:
            m = DEPTH1_RE.match(line)
            if not m:
                continue
            name = m.group(1).strip().split()[0].split("/")[0]
            if not name.startswith("@") and name not in children:
                children.append(name)
        return children if children else depth0

    # ── Flat format: depth-0 elements ARE the children ───────────────────────
    return depth0 if depth0 else None


# ──────────────────────────────────────────────────────────────────────────────
# XML helpers
# ──────────────────────────────────────────────────────────────────────────────

def _local(tag) -> str:
    """Strip namespace from a tag: '{ns}Name' → 'Name'.
    Returns '' for non-element nodes (comments, PIs) whose tag is a callable."""
    if not isinstance(tag, str):
        return ""
    return tag.split("}")[-1] if "}" in tag else tag


def xml_direct_children(xml_path: Path, element_name: str) -> Optional[List[str]]:
    """
    Find the first <element_name> element in the XML and return its direct
    child element local-names in document order (deduplicated, first occurrence
    wins).
    Returns None if the element is not found or the file cannot be parsed.
    """
    try:
        import lxml.etree as ET
        tree = ET.parse(str(xml_path))
    except Exception:
        return None

    target = None
    for el in tree.getroot().iter():
        if _local(el.tag) == element_name:
            target = el
            break
    if target is None:
        return None

    seen: List[str] = []
    for child in target:
        name = _local(child.tag)
        if name and name not in seen:
            seen.append(name)
    return seen


def _prefer_np(examples: List[Path]) -> Path:
    """Given a list of Example XML paths, prefer one with '_NP' in its name."""
    for p in examples:
        if "_NP" in p.name:
            return p
    return examples[0]


def _object_name(table_or_desc_path: Path) -> str:
    """
    'Table_ServiceFrame.md'      → 'ServiceFrame'
    'Description_ServiceFrame.md' → 'ServiceFrame'
    """
    stem = table_or_desc_path.stem  # e.g. Table_ServiceFrame
    return re.sub(r"^(Table|Description)_", "", stem)


# ──────────────────────────────────────────────────────────────────────────────
# Check 1: XSD validation
# ──────────────────────────────────────────────────────────────────────────────

def run_xsd_checks(target: Optional[Path], errors: List[str]) -> None:
    """XSD-validate every Example XML wrapped in a PublicationDelivery."""
    try:
        import lxml.etree as ET
    except ImportError:
        errors.append("[SETUP] lxml is required: pip install lxml")
        return

    if not XSD_PATH.exists():
        errors.append(f"[SETUP] Schema not found: {XSD_PATH}")
        return

    schema = ET.XMLSchema(ET.parse(str(XSD_PATH)))

    search_root = target if target else WORKSPACE
    for xml_path in sorted(search_root.rglob("Example_*.xml")):
        if "XSD" in xml_path.parts:
            continue

        try:
            doc = ET.parse(str(xml_path))
        except ET.XMLSyntaxError as exc:
            errors.append(f"[PARSE ERROR] {xml_path.relative_to(WORKSPACE)}: {exc}")
            continue

        root = doc.getroot()
        if _local(root.tag) != "PublicationDelivery":
            continue  # fragment — skip

        if not schema.validate(doc):
            last = schema.error_log.last_error
            errors.append(
                f"[XSD INVALID] {xml_path.relative_to(WORKSPACE)}: "
                f"line {last.line}: {last.message}"
            )


# ──────────────────────────────────────────────────────────────────────────────
# Check 2: Table element order vs XML
# ──────────────────────────────────────────────────────────────────────────────

def run_order_checks(
    target: Optional[Path], errors: List[str], warnings: List[str]
) -> None:
    """
    For each Table_*.md with Example XML(s) in the same directory, verify
    that the element order in the Structure Overview matches the XML.
    """
    search_root = target if target else WORKSPACE
    for table_path in sorted(search_root.rglob("Table_*.md")):
        if "XSD" in table_path.parts:
            continue

        obj_name = _object_name(table_path)
        examples = list(table_path.parent.glob("Example_*.xml"))
        if not examples:
            warnings.append(
                f"[NO EXAMPLE] {table_path.relative_to(WORKSPACE)} "
                f"— no Example XML in same directory, skipping order check"
            )
            continue

        table_order = parse_table_overview(table_path)
        if table_order is None:
            warnings.append(
                f"[NO OVERVIEW] {table_path.relative_to(WORKSPACE)} "
                f"— no ```text Structure Overview found, skipping"
            )
            continue

        xml_path = _prefer_np(examples)
        xml_order = xml_direct_children(xml_path, obj_name)
        if xml_order is None:
            warnings.append(
                f"[NO ELEMENT] {xml_path.relative_to(WORKSPACE)} "
                f"— <{obj_name}> not found in XML, skipping"
            )
            continue

        table_set = set(table_order)
        xml_set = set(xml_order)

        if table_set - xml_set:
            warnings.append(
                f"[TABLE EXTRA] {table_path.relative_to(WORKSPACE)}: "
                f"in Table but not XML: {sorted(table_set - xml_set)}"
            )
        if xml_set - table_set:
            warnings.append(
                f"[XML EXTRA] {xml_path.relative_to(WORKSPACE)}: "
                f"in XML but not Table: {sorted(xml_set - table_set)}"
            )

        # Order check: common elements must appear in the same relative order
        common_from_table = [e for e in table_order if e in xml_set]
        common_from_xml = [e for e in xml_order if e in table_set]
        if common_from_table != common_from_xml:
            errors.append(
                f"[ORDER MISMATCH] {table_path.relative_to(WORKSPACE)} "
                f"vs {xml_path.relative_to(WORKSPACE)}\n"
                f"  Table: {common_from_table}\n"
                f"  XML:   {common_from_xml}"
            )


# ──────────────────────────────────────────────────────────────────────────────
# Check 3: Description Structure Overview vs Table Structure Overview
# ──────────────────────────────────────────────────────────────────────────────

def run_desc_checks(
    target: Optional[Path], errors: List[str], warnings: List[str]
) -> None:
    """
    For each Description_*.md, compare its Structure Overview to the
    corresponding Table_*.md Structure Overview.
    """
    search_root = target if target else WORKSPACE
    for desc_path in sorted(search_root.rglob("Description_*.md")):
        if "XSD" in desc_path.parts:
            continue

        obj_name = _object_name(desc_path)
        table_path = desc_path.parent / f"Table_{obj_name}.md"
        if not table_path.exists():
            warnings.append(
                f"[NO TABLE] {desc_path.relative_to(WORKSPACE)} "
                f"— no matching {table_path.name}"
            )
            continue

        desc_order = parse_desc_overview(desc_path)
        table_order = parse_table_overview(table_path)

        if desc_order is None:
            warnings.append(
                f"[NO OVERVIEW] {desc_path.relative_to(WORKSPACE)} "
                f"— no Structure Overview code block found"
            )
            continue
        if table_order is None:
            warnings.append(
                f"[NO OVERVIEW] {table_path.relative_to(WORKSPACE)} "
                f"— no Structure Overview code block found"
            )
            continue

        if desc_order != table_order:
            errors.append(
                f"[DESC MISMATCH] {desc_path.relative_to(WORKSPACE)}\n"
                f"  Description: {desc_order}\n"
                f"  Table:       {table_order}"
            )


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# Check 4: Sidebar completeness
# ──────────────────────────────────────────────────────────────────────────────

def run_sidebar_checks(errors: List[str]) -> None:
    """Verify every documented Object/Frame/Guide folder is linked in _sidebar.md."""
    sidebar_path = WORKSPACE / "_sidebar.md"
    if not sidebar_path.exists():
        errors.append("[SETUP] _sidebar.md not found")
        return

    sidebar = sidebar_path.read_text(encoding="utf-8")

    for section, pattern in [
        ("Guides", "*_Guide.md"),
        ("Guides", "*.md"),
        ("Objects", "Description_*.md"),
        ("Frames", "Description_*.md"),
    ]:
        section_root = WORKSPACE / section
        if not section_root.exists():
            continue
        for folder in sorted(section_root.iterdir()):
            if not folder.is_dir():
                continue
            if not list(folder.glob(pattern)):
                continue
            if folder.name not in sidebar:
                errors.append(
                    f"[SIDEBAR MISSING] {section}/{folder.name} has docs "
                    f"but is not linked in _sidebar.md"
                )


def main() -> None:
    # Ensure UTF-8 output on Windows consoles
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(
        description="Check NeTEx profile documentation consistency"
    )
    parser.add_argument("--xsd-only", action="store_true", help="Only XSD validation")
    parser.add_argument(
        "--order-only", action="store_true", help="Only Table-vs-XML order check"
    )
    parser.add_argument(
        "--desc-only", action="store_true", help="Only Description-vs-Table check"
    )
    parser.add_argument(
        "--sidebar-only", action="store_true", help="Only sidebar completeness check"
    )
    parser.add_argument(
        "--target",
        metavar="PATH",
        help="Scope checks to a subdirectory (e.g. Frames/ServiceFrame)",
    )
    args = parser.parse_args()

    run_all = not (args.xsd_only or args.order_only or args.desc_only or args.sidebar_only)
    target = (WORKSPACE / args.target) if args.target else None

    errors: List[str] = []
    warnings: List[str] = []

    if run_all or args.xsd_only:
        print("▶ XSD validation …")
        before = len(errors)
        run_xsd_checks(target, errors)
        print(f"  {len(errors) - before} error(s)")

    if run_all or args.order_only:
        print("▶ Table-vs-XML order check …")
        before = len(errors)
        run_order_checks(target, errors, warnings)
        print(f"  {len(errors) - before} error(s), {len(warnings)} warning(s)")

    if run_all or args.desc_only:
        print("▶ Description-vs-Table check …")
        before = len(errors)
        run_desc_checks(target, errors, warnings)
        print(f"  {len(errors) - before} error(s)")
    if run_all or args.sidebar_only:
        print("\u25b6 Sidebar completeness check \u2026")
        before = len(errors)
        run_sidebar_checks(errors)
        print(f"  {len(errors) - before} error(s)")
    if warnings:
        print(f"\n⚠  Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  {w}")

    if errors:
        print(f"\n✗ Errors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print(f"\n✓ All checks passed  ({len(warnings)} warning(s))")
        sys.exit(0)


if __name__ == "__main__":
    main()
