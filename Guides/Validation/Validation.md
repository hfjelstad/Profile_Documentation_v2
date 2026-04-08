# ✅ NeTEx Validation Guide

## 1. 🎯 Introduction

Validating NeTEx XML against the official schema catches structural errors, wrong element ordering, invalid references, and missing required elements before they cause issues downstream. This guide covers the validation process from schema setup to troubleshooting.

In this guide you will learn:
- 📦 Which schema entry point to use
- 🖥️ How to validate locally and in CI
- ❌ The most common validation errors and how to fix them
- 🔧 Troubleshooting tips

> For **tool installation** (xmllint, lxml, editors), see the [Tools Guide](../Tools/Tools_Guide.md).

---

## 2. 📦 Schema Setup

### Entry Points

| Schema File | When to Use |
|-------------|-------------|
| `NeTEx_publication.xsd` | **Default** — validates the full NeTEx schema |
| `NeTEx_publication_timetable.xsd` | Timetable-focused — imports Part 2 journey modules |

> 💡 **Tip:** Use `NeTEx_publication.xsd` unless you have a specific reason for the timetable entry point.

### Getting the Schema

Clone (or shallow-clone) the official NeTEx XSD directly from the source:

```bash
git clone --depth=1 https://github.com/NeTEx-CEN/NeTEx.git netex-xsd
```

The entry point is then `netex-xsd/xsd/NeTEx_publication.xsd`.

> 💡 **Tip:** This always gives you the latest official schema. Re-run the clone (or `git -C netex-xsd pull`) to pick up updates.

> ⚠️ **Note:** The `netex-xsd/` folder is a working copy, not part of your project. Add it to `.gitignore` if needed.

### Using a Specific Version

To validate against a particular NeTEx release instead of the latest, check out the corresponding tag after cloning:

```bash
git clone https://github.com/NeTEx-CEN/NeTEx.git netex-xsd
cd netex-xsd
git tag -l            # list available versions
git checkout v1.15    # switch to a specific release
```

To switch back to the latest:

```bash
git checkout main
git pull
```

---

## 3. 🖥️ Running Validation

### Using This Repository's Script

The easiest way to validate:

```bash
# All XML files
./scripts/validate-xml.sh

# Only files changed vs EnStandardBranch
./scripts/validate-xml.sh --changed

# Specific files
./scripts/validate-xml.sh Objects/Line/Example_Line_MIN.xml
```

### Using xmllint Directly

```bash
xmllint --noout \
  --schema "netex-xsd/xsd/NeTEx_publication.xsd" \
  Objects/Line/Example_Line_MIN.xml
```

### Using Python lxml

```python
from lxml import etree

schema = etree.XMLSchema(etree.parse("netex-xsd/xsd/NeTEx_publication.xsd"))
doc = etree.parse("Objects/Line/Example_Line_MIN.xml")

if schema.validate(doc):
    print("PASS")
else:
    for err in schema.error_log:
        print(err)
```

### CI Validation

Pull requests are automatically validated by [`.github/workflows/PR_Validator.yml`](../../.github/workflows/PR_Validator.yml) when XML files change. Always validate locally first to avoid CI failures.

---

## 4. ❌ Common Errors and Fixes

### 4a. Wrong Element Order

```text
Element 'PublicCode': This element is not expected.
Expected is one of ( Name, Description, PrivateCode, ... )
```

**Cause:** NeTEx XSD uses `xs:sequence` — elements must appear in a specific order following the type inheritance chain.

**Fix:** Reorder elements to match the XSD sequence. Check the validated examples in this repository or the object's Table file for the correct order. See [NeTEx Conventions — Element Ordering](../NeTExConventions/NeTEx_Conventions.md#5--element-ordering) for details.

---

### 4b. Wrong Casing

```text
Element 'DataObjects': This element is not expected.
Expected is ( dataObjects )
```

**Cause:** Collection wrappers must use lowerCamelCase.

**Fix:** Change `DataObjects` to `dataObjects`. See [NeTEx Conventions — Casing Rules](../NeTExConventions/NeTEx_Conventions.md#2--casing-rules).

---

### 4c. Invalid Element

```text
Element 'PublicCode': This element is not expected.
```

**Cause:** The element doesn't exist on this type in the XSD (e.g., `PublicCode` is not valid on `Route`).

**Fix:** Remove the element or check the object's Table file for which elements are valid.

---

### 4d. Unresolved Versioned Reference

```text
No match found for key-sequence ['ERP:ServiceJourney:SJ_001', '1']
```

**Cause:** A `*Ref` element has a `version` attribute, but the referenced object with that exact version doesn't exist in the same file.

**Fix:** Either remove the `version` attribute from the `*Ref` (preferred for external references), or ensure the referenced object exists in the file with the matching version.

```xml
<!-- Problem: versioned ref, but object not in file -->
<ServiceJourneyRef ref="ERP:ServiceJourney:SJ_001" version="1"/>

<!-- Fix: remove version for external references -->
<ServiceJourneyRef ref="ERP:ServiceJourney:SJ_001"/>
```

---

### 4e. Missing Required Element

```text
Element 'ServiceJourney': Missing child element(s).
Expected is ( ... )
```

**Cause:** A mandatory child element is missing.

**Fix:** Add the required element. Check the error message for what's expected, or consult the object's Description file.

---

### 4f. Invalid Enum Value

```text
Element 'PropulsionType': 'diesel' is not a valid value.
```

**Cause:** The element value is not one of the allowed enum values in the XSD.

**Fix:** Check the XSD or the object's Table file for valid enum values. Common example: `PropulsionType` accepts `combustion`, `electric`, `hybrid`, etc. — not `diesel`.

---

## 5. 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Cannot find schema" | Ensure the XSD is available locally — clone from the official repo (see section 2) |
| Schema loads but nothing validates | Check you're using the correct entry point (`NeTEx_publication.xsd`) |
| Many errors cascade from one issue | Fix the **first** error only, then re-validate — later errors are often caused by the first |
| Validation passes locally, fails in CI | Ensure you've committed all changed files and pushed |
| xmllint not available (Windows) | Use Python lxml instead — `pip install lxml` |

---

## 6. 📋 Pre-Commit Checklist

Before committing XML changes:

- [ ] Run `./scripts/validate-xml.sh --changed` (or validate specific files)
- [ ] All files pass with 0 errors
- [ ] `ParticipantRef` is `EuPro` (not `ENTUR` or `ERP`)
- [ ] Codespace matches the profile: `ERP:` for MIN/ERP, `NP:` for Nordic Profile
- [ ] No `version` attributes on references to external objects

---

## 7. 🔗 Related Resources

### Guides
- [Tools](../Tools/Tools_Guide.md) — Editor setup, validator installation, development workflow
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — Casing, IDs, versioning, and element ordering rules
- [Get Started](../GetStarted/GetStarted_Guide.md) — NeTEx document structure fundamentals
