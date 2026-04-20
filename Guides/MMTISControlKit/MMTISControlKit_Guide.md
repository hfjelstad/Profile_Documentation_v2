# MMTIS Control Authority Survival Kit

> A practical toolkit for National Access Point operators and control authorities responsible for ensuring the quality and completeness of NeTEx data under EU Delegated Regulation 2017/1926 on Multimodal Travel Information Services (MMTIS).
>
> _Designed to be useful even — especially — when budgets are tight._

---

## What This Guide Covers

1. [Regulatory recap](#regulatory-recap) — What you are required to check
2. [Accessing your country's data](#accessing-your-countrys-data) — Where to find and download NeTEx feeds
3. [Validation toolkit](#validation-toolkit) — Free tools for automated checks
4. [Completeness controls](#completeness-controls) — Verifying data coverage
5. [Quality controls](#quality-controls) — Checking data consistency and correctness
6. [Issuing controls](#issuing-controls) — A structured audit workflow
7. [Budget-friendly infrastructure](#budget-friendly-infrastructure) — Running everything on open-source tools

---

## Regulatory Recap

EU Delegated Regulation [2017/1926](https://eur-lex.europa.eu/eli/reg_del/2017/1926/oj) requires Member States to set up a **National Access Point (NAP)** and ensure that transport operators and authorities provide specific data categories:

| Priority | Data categories | Original deadline |
|----------|----------------|-------------------|
| **A** | Stops, networks, timetables, fares (basic), accessibility | 1 Dec 2019 |
| **B** | On-demand transport, detailed fares, bike-sharing, car-sharing | 1 Dec 2020 |
| **C** | Car parks, fuel stations, electric charging, road tolls | 1 Dec 2021 |

The preferred exchange format for scheduled transport is **NeTEx**, with the **EPIP** (European Passenger Information Profile) as the baseline. National profiles (Nordic, French, German, etc.) add further constraints.

For a detailed mapping of regulation requirements to NeTEx objects, see the [Regulatory Compliance Guide](/Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md).

> [!IMPORTANT]
> As a control authority, your job is to verify that data published on your NAP is **present**, **valid**, **complete**, and **usable** — not to produce it yourself.

---

## Accessing Your Country's Data

### Known National Access Points

| Country | NAP | API/Bulk | URL |
|---------|-----|----------|-----|
| Norway | Entur | API + bulk download | <https://developer.entur.org/> |
| France | transport.data.gouv.fr | Bulk download + API | <https://transport.data.gouv.fr/> |
| UK | BODS | API + bulk | <https://data.bus-data.dft.gov.uk/> |
| Netherlands | NDOV | Bulk | <https://ndovloket.nl/> |
| Finland | Fintraffic | API | <https://www.fintraffic.fi/en/fintraffic/open-data> |
| Sweden | Trafiklab | API | <https://www.trafiklab.se/> |
| Germany | NAP-DE | Catalogue | <https://mobilithek.info/> |
| Switzerland | opentransportdata | API + bulk | <https://opentransportdata.swiss/> |
| EU overview | NAP status page | — | [EC NAP directory](https://transport.ec.europa.eu/transport-themes/intelligent-transport-systems/road/action-plan-and-directive/national-access-points_en) |

### Automated Download Script

```python
"""
Download all NeTEx datasets from a NAP and prepare them for validation.
Adjust the URL pattern to your country's NAP API.
"""
import requests, zipfile, io, os, json

OUTPUT_DIR = "nap_datasets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Example: French NAP API — list NeTEx datasets
# Replace with your NAP's API endpoint
response = requests.get("https://transport.data.gouv.fr/api/datasets", params={"type": "public-transit"})
datasets = response.json()

for ds in datasets:
    for resource in ds.get("resources", []):
        if resource.get("format", "").lower() == "netex":
            name = ds.get("slug", "unknown")
            url = resource.get("original_url") or resource.get("url")
            print(f"Downloading: {name}")
            try:
                r = requests.get(url, timeout=60)
                dest = os.path.join(OUTPUT_DIR, f"{name}.zip")
                with open(dest, "wb") as f:
                    f.write(r.content)
            except Exception as e:
                print(f"  ERROR: {e}")

print(f"\nDownloaded to {OUTPUT_DIR}/")
```

---

## Validation Toolkit

All tools below are **free and open-source**. No commercial licences required.

### Level 1 — XSD Schema Validation

Checks that the XML is structurally valid against the NeTEx schema.

**Tool: `xmllint`** (pre-installed on Linux/macOS, available via MSYS2 or WSL on Windows)

```bash
#!/bin/bash
# validate_all.sh — Validate all NeTEx files against the XSD
XSD_PATH="path/to/NeTEx/xsd/NeTEx_publication.xsd"

find nap_datasets -name "*.xml" | while read f; do
    echo -n "$f: "
    xmllint --noout --schema "$XSD_PATH" "$f" 2>&1 | tail -1
done
```

**Tool: Python + lxml** (cross-platform)

```python
from lxml import etree
import glob, sys

XSD_PATH = "path/to/NeTEx/xsd/NeTEx_publication.xsd"
schema = etree.XMLSchema(etree.parse(XSD_PATH))

results = {"valid": 0, "invalid": 0, "errors": []}

for xml_file in glob.glob("nap_datasets/**/*.xml", recursive=True):
    try:
        doc = etree.parse(xml_file)
        if schema.validate(doc):
            results["valid"] += 1
        else:
            results["invalid"] += 1
            for error in schema.error_log:
                results["errors"].append({
                    "file": xml_file,
                    "line": error.line,
                    "message": str(error.message),
                })
    except etree.XMLSyntaxError as e:
        results["invalid"] += 1
        results["errors"].append({"file": xml_file, "line": 0, "message": str(e)})

print(f"Valid: {results['valid']}, Invalid: {results['invalid']}")
for e in results["errors"][:20]:
    print(f"  {e['file']}:{e['line']} — {e['message']}")
```

### Level 2 — Profile Conformance

Beyond basic XSD, check whether the data conforms to the expected **profile** (EPIP, Nordic, French, etc.). Profile checks verify:

- Required elements are present (e.g., `Line/TransportMode` is mandatory in most profiles)
- ID format follows the profile convention
- Frame structure matches expectations
- Cardinality constraints stricter than XSD are met

```python
"""
Basic profile conformance checker — checks common requirements across profiles.
Extend per your national profile.
"""
from lxml import etree

NS = {"n": "http://www.netex.org.uk/netex"}

def check_profile_conformance(xml_file):
    """Run basic profile conformance checks on a NeTEx file."""
    tree = etree.parse(xml_file)
    issues = []

    # Check: Every Line must have a TransportMode
    for line in tree.iter("{http://www.netex.org.uk/netex}Line"):
        mode = line.findtext("{http://www.netex.org.uk/netex}TransportMode")
        if not mode:
            issues.append(f"Line {line.get('id')}: missing TransportMode")

    # Check: Every ScheduledStopPoint should have a Name
    for ssp in tree.iter("{http://www.netex.org.uk/netex}ScheduledStopPoint"):
        name = ssp.findtext("{http://www.netex.org.uk/netex}Name")
        if not name:
            issues.append(f"ScheduledStopPoint {ssp.get('id')}: missing Name")

    # Check: Every ServiceJourney must reference a JourneyPattern
    for sj in tree.iter("{http://www.netex.org.uk/netex}ServiceJourney"):
        jp_ref = sj.find(".//{http://www.netex.org.uk/netex}JourneyPatternRef")
        sjp_ref = sj.find(".//{http://www.netex.org.uk/netex}ServiceJourneyPatternRef")
        if jp_ref is None and sjp_ref is None:
            issues.append(f"ServiceJourney {sj.get('id')}: missing JourneyPatternRef")

    # Check: All Ref elements must have a non-empty 'ref' attribute
    for el in tree.iter():
        tag = etree.QName(el.tag).localname
        if tag.endswith("Ref") and el.get("ref") is not None:
            if not el.get("ref").strip():
                issues.append(f"{tag} at line {el.sourceline}: empty ref attribute")

    # Check: PublicationDelivery has a ParticipantRef
    root = tree.getroot()
    participant = root.findtext("{http://www.netex.org.uk/netex}ParticipantRef")
    if not participant:
        issues.append("PublicationDelivery: missing ParticipantRef")

    return issues
```

### Level 3 — Referential Integrity

Check that every `*Ref` element actually points to an existing object:

```python
def check_referential_integrity(xml_files):
    """Check that all references resolve to existing objects across a set of files."""
    ns = "http://www.netex.org.uk/netex"

    # Collect all defined IDs
    defined_ids = set()
    references = []

    for xml_file in xml_files:
        tree = etree.parse(xml_file)
        for el in tree.iter():
            obj_id = el.get("id")
            if obj_id:
                defined_ids.add(obj_id)

            tag = etree.QName(el.tag).localname
            if tag.endswith("Ref"):
                ref_val = el.get("ref")
                if ref_val:
                    references.append({
                        "file": xml_file,
                        "line": el.sourceline,
                        "ref_type": tag,
                        "ref_value": ref_val,
                    })

    # Check each reference
    broken = []
    for ref in references:
        if ref["ref_value"] not in defined_ids:
            broken.append(ref)

    return broken

broken_refs = check_referential_integrity(glob.glob("nap_datasets/some_dataset/*.xml"))
print(f"Broken references: {len(broken_refs)}")
for b in broken_refs[:10]:
    print(f"  {b['file']}:{b['line']} — {b['ref_type']} → {b['ref_value']}")
```

> [!NOTE]
> Some references intentionally point to objects in **other datasets** (e.g., `StopPlace` references may resolve in a national stop register, not in the timetable file). Factor this in before reporting false positives.

---

## Completeness Controls

These checks verify that a NAP's data coverage matches what the regulation requires.

### Data Category Checklist

Use this checklist to verify presence of Priority A data at minimum:

```python
def check_completeness(xml_files):
    """Check that mandatory data categories are present in a NeTEx delivery."""
    ns = "http://www.netex.org.uk/netex"

    found = {
        "StopPlace": False,
        "Line": False,
        "Route": False,
        "ServiceJourneyPattern": False,
        "ScheduledStopPoint": False,
        "ServiceJourney": False,
        "DayType": False,
        "Operator": False,
        "Authority": False,
        "Network": False,
        "PassengerStopAssignment": False,
    }

    for xml_file in xml_files:
        tree = etree.parse(xml_file)
        for key in found:
            if not found[key]:
                if tree.find(f".//{{{ns}}}{key}") is not None:
                    found[key] = True

    print("Completeness check (Priority A required objects):")
    for key, present in found.items():
        status = "✓" if present else "✗ MISSING"
        print(f"  {key}: {status}")

    return found
```

### Geographic Coverage

Does the data actually cover the expected geographic area?

```python
def check_geographic_coverage(xml_files):
    """Extract bounding box of all stop coordinates to verify geographic coverage."""
    ns = "http://www.netex.org.uk/netex"
    lats, lons = [], []

    for xml_file in xml_files:
        tree = etree.parse(xml_file)
        for loc in tree.iter(f"{{{ns}}}Location"):
            lat = loc.findtext(f"{{{ns}}}Latitude")
            lon = loc.findtext(f"{{{ns}}}Longitude")
            if lat and lon:
                try:
                    lats.append(float(lat))
                    lons.append(float(lon))
                except ValueError:
                    pass

    if lats and lons:
        print(f"Geographic coverage:")
        print(f"  Latitude:  {min(lats):.4f} → {max(lats):.4f}")
        print(f"  Longitude: {min(lons):.4f} → {max(lons):.4f}")
        print(f"  Stop points with coordinates: {len(lats)}")
    else:
        print("  WARNING: No coordinates found in any stop point!")

    return {"lat_min": min(lats, default=None), "lat_max": max(lats, default=None),
            "lon_min": min(lons, default=None), "lon_max": max(lons, default=None),
            "count": len(lats)}
```

### Temporal Coverage

Are the timetables current, or have they expired?

```python
from datetime import date, datetime

def check_temporal_coverage(xml_files):
    """Check that operating periods cover the current date."""
    ns = "http://www.netex.org.uk/netex"
    today = date.today()
    periods = []

    for xml_file in xml_files:
        tree = etree.parse(xml_file)
        for op in tree.iter(f"{{{ns}}}OperatingPeriod"):
            from_date_str = op.findtext(f"{{{ns}}}FromDate")
            to_date_str = op.findtext(f"{{{ns}}}ToDate")
            if from_date_str and to_date_str:
                try:
                    from_date = datetime.fromisoformat(from_date_str.replace("Z", "+00:00")).date()
                    to_date = datetime.fromisoformat(to_date_str.replace("Z", "+00:00")).date()
                    periods.append({"from": from_date, "to": to_date, "id": op.get("id")})
                except ValueError:
                    pass

    if not periods:
        print("  WARNING: No OperatingPeriods found")
        return

    earliest = min(p["from"] for p in periods)
    latest = max(p["to"] for p in periods)
    current = any(p["from"] <= today <= p["to"] for p in periods)
    expired = all(p["to"] < today for p in periods)

    print(f"Temporal coverage:")
    print(f"  Earliest start: {earliest}")
    print(f"  Latest end:     {latest}")
    print(f"  Covers today ({today}): {'YES' if current else 'NO'}")
    if expired:
        print(f"  ⚠️  ALL operating periods have expired!")

    return {"earliest": earliest, "latest": latest, "current": current, "expired": expired}
```

---

## Quality Controls

### Data Consistency Checks

```python
def check_data_quality(xml_files):
    """Run data quality checks across a NeTEx delivery."""
    ns = "http://www.netex.org.uk/netex"
    issues = []

    for xml_file in xml_files:
        tree = etree.parse(xml_file)

        # Check: ServiceJourney passing times should be chronologically ordered
        for sj in tree.iter(f"{{{ns}}}ServiceJourney"):
            sj_id = sj.get("id")
            prev_time = None
            for tt in sj.iter(f"{{{ns}}}TimetabledPassingTime"):
                dep = tt.findtext(f"{{{ns}}}DepartureTime")
                arr = tt.findtext(f"{{{ns}}}ArrivalTime")
                current = dep or arr
                if current and prev_time and current < prev_time:
                    issues.append(f"{xml_file}: ServiceJourney {sj_id} — "
                                  f"times not chronological ({prev_time} → {current})")
                if current:
                    prev_time = current

        # Check: StopPoints should have valid coordinates
        for ssp in tree.iter(f"{{{ns}}}ScheduledStopPoint"):
            loc = ssp.find(f"{{{ns}}}Location")
            if loc is not None:
                lat = loc.findtext(f"{{{ns}}}Latitude")
                lon = loc.findtext(f"{{{ns}}}Longitude")
                try:
                    lat_f, lon_f = float(lat), float(lon)
                    if not (-90 <= lat_f <= 90) or not (-180 <= lon_f <= 180):
                        issues.append(f"{xml_file}: ScheduledStopPoint {ssp.get('id')} — "
                                      f"coordinates out of range ({lat}, {lon})")
                    if lat_f == 0 and lon_f == 0:
                        issues.append(f"{xml_file}: ScheduledStopPoint {ssp.get('id')} — "
                                      f"suspicious coordinates (0, 0)")
                except (ValueError, TypeError):
                    issues.append(f"{xml_file}: ScheduledStopPoint {ssp.get('id')} — "
                                  f"invalid coordinate format")

        # Check: Lines should have distinct names
        line_names = {}
        for line in tree.iter(f"{{{ns}}}Line"):
            name = line.findtext(f"{{{ns}}}Name")
            if name in line_names:
                issues.append(f"{xml_file}: Duplicate Line name '{name}' "
                              f"(IDs: {line_names[name]}, {line.get('id')})")
            else:
                line_names[name] = line.get("id")

    return issues
```

### Quick Summary Report

```python
def generate_summary_report(xml_files):
    """Generate a summary report for a NAP dataset."""
    ns = "http://www.netex.org.uk/netex"

    counts = {}
    for xml_file in xml_files:
        tree = etree.parse(xml_file)
        for el in tree.iter():
            tag = etree.QName(el.tag).localname
            if el.get("id") is not None:  # Only count objects with IDs
                counts[tag] = counts.get(tag, 0) + 1

    print("=" * 50)
    print("DATASET SUMMARY REPORT")
    print("=" * 50)
    print(f"\nFiles analysed: {len(xml_files)}")
    print(f"\nObject counts:")
    for tag in sorted(counts.keys()):
        print(f"  {tag:40s} {counts[tag]:>6d}")
    print(f"\n{'Total objects':40s} {sum(counts.values()):>6d}")
```

---

## Issuing Controls

### Audit Workflow

A structured approach to auditing a NAP dataset:

```
┌─────────────────────────────────────────────────────┐
│ 1. DOWNLOAD                                        │
│    Retrieve all current NeTEx datasets from NAP     │
├─────────────────────────────────────────────────────┤
│ 2. XSD VALIDATION                                  │
│    Schema-level check: is the XML well-formed       │
│    and structurally valid?                           │
├─────────────────────────────────────────────────────┤
│ 3. PROFILE CONFORMANCE                             │
│    Does the data conform to the expected profile    │
│    (EPIP / national)?                               │
├─────────────────────────────────────────────────────┤
│ 4. REFERENTIAL INTEGRITY                           │
│    Do all internal references resolve?              │
├─────────────────────────────────────────────────────┤
│ 5. COMPLETENESS                                    │
│    Are Priority A data categories (and B/C if       │
│    applicable) present?                             │
├─────────────────────────────────────────────────────┤
│ 6. TEMPORAL VALIDITY                               │
│    Are timetables current? Upcoming updates         │
│    submitted in time?                               │
├─────────────────────────────────────────────────────┤
│ 7. QUALITY SPOT-CHECKS                             │
│    Coordinates valid? Times chronological?          │
│    Duplicates? Orphan objects?                      │
├─────────────────────────────────────────────────────┤
│ 8. REPORT                                          │
│    Generate per-dataset findings; track trends      │
│    over time                                        │
└─────────────────────────────────────────────────────┘
```

### Control Report Template

```python
import json
from datetime import datetime

def run_full_audit(dataset_name, xml_files):
    """Run a full audit and produce a structured report."""
    report = {
        "dataset": dataset_name,
        "audit_date": datetime.now().isoformat(),
        "files_checked": len(xml_files),
        "checks": {}
    }

    # 1. XSD Validation
    xsd_path = "path/to/NeTEx/xsd/NeTEx_publication.xsd"
    schema = etree.XMLSchema(etree.parse(xsd_path))
    xsd_errors = []
    for f in xml_files:
        try:
            doc = etree.parse(f)
            if not schema.validate(doc):
                for err in schema.error_log:
                    xsd_errors.append({"file": f, "line": err.line, "msg": str(err.message)})
        except Exception as e:
            xsd_errors.append({"file": f, "line": 0, "msg": str(e)})
    report["checks"]["xsd_validation"] = {
        "status": "PASS" if not xsd_errors else "FAIL",
        "error_count": len(xsd_errors),
        "errors": xsd_errors[:50],  # Cap at 50 for readability
    }

    # 2. Completeness
    completeness = check_completeness(xml_files)
    missing = [k for k, v in completeness.items() if not v]
    report["checks"]["completeness"] = {
        "status": "PASS" if not missing else "FAIL",
        "missing_objects": missing,
    }

    # 3. Temporal coverage
    temporal = check_temporal_coverage(xml_files)
    report["checks"]["temporal_coverage"] = temporal

    # 4. Referential integrity
    broken = check_referential_integrity(xml_files)
    report["checks"]["referential_integrity"] = {
        "status": "PASS" if not broken else "WARN",
        "broken_count": len(broken),
        "samples": [{"ref_type": b["ref_type"], "ref_value": b["ref_value"]}
                     for b in broken[:20]],
    }

    # 5. Data quality
    quality_issues = check_data_quality(xml_files)
    report["checks"]["data_quality"] = {
        "status": "PASS" if not quality_issues else "WARN",
        "issue_count": len(quality_issues),
        "issues": quality_issues[:20],
    }

    # Save report
    report_file = f"audit_{dataset_name}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2, default=str)
    print(f"\nAudit report saved to {report_file}")

    return report
```

### Tracking Trends Over Time

Run regular audits (weekly or monthly) and compare:

- Is the number of XSD errors decreasing?
- Are new datasets appearing on the NAP?
- Are operating periods being updated before they expire?
- Are previously reported issues being fixed?

---

## Budget-Friendly Infrastructure

Everything above can run on a single machine with **zero software costs**:

| Component | Tool | Cost |
|-----------|------|------|
| Programming language | Python 3 | Free |
| XML parsing | `lxml` (pip install) | Free |
| Schema validation | `xmllint` or `lxml` | Free |
| XSD schema | [NeTEx-CEN/NeTEx](https://github.com/NeTEx-CEN/NeTEx) on GitHub | Free |
| XML editor | VS Code + Red Hat XML extension | Free |
| XPath querying | `lxml` / `xmllint --xpath` | Free |
| Automation | cron (Linux) / Task Scheduler (Windows) | Free (built-in) |
| CI/CD (if needed) | GitHub Actions (2,000 min/month free tier) | Free |
| Reporting | JSON/HTML output from Python scripts | Free |
| Data storage | Local filesystem / SQLite | Free |

### Minimal Automated Setup

A cron job or Windows Task Scheduler entry that:

1. Downloads the latest datasets from your NAP
2. Runs XSD validation on all files
3. Runs completeness and temporal checks
4. Saves a JSON report
5. Optionally sends an email summary if issues are found

```bash
# Example crontab entry — run every Monday at 06:00
0 6 * * 1 cd /opt/nap-audit && python3 audit_runner.py >> /var/log/nap-audit.log 2>&1
```

### XPath as a Query Tool

For ad-hoc investigations, `xmllint --xpath` is your best friend:

```bash
# Count all Lines in a file
xmllint --xpath "count(//*[local-name()='Line'])" dataset.xml

# List all Line names
xmllint --xpath "//*[local-name()='Line']/*[local-name()='Name']/text()" dataset.xml

# Find all StopPoints without coordinates
xmllint --xpath "//*[local-name()='ScheduledStopPoint'][not(*[local-name()='Location'])]/@id" dataset.xml

# Count ServiceJourneys
xmllint --xpath "count(//*[local-name()='ServiceJourney'])" dataset.xml
```

---

## Quick Reference Card

| What to check | How | Severity if missing |
|---------------|-----|-------------------|
| XML well-formedness | `xmllint --noout file.xml` | Blocker |
| XSD schema validation | `xmllint --schema NeTEx_publication.xsd` | Blocker |
| ParticipantRef present | XPath check | High |
| Lines have TransportMode | Profile check script | High |
| Stops have coordinates | Geographic coverage script | High |
| Times are chronological | Quality check script | High |
| Operating periods current | Temporal coverage script | High |
| All references resolve | Referential integrity script | Medium |
| Stop names present | Profile check script | Medium |
| Coordinates within country bounds | Geographic coverage script | Medium |
| No duplicate Line names | Quality check script | Low |

---

## Further Reading

| Topic | Resource |
|-------|----------|
| EU Regulation mapping to NeTEx | [Regulatory Compliance Guide](/Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md) |
| XSD validation in depth | [Validation Guide](/Guides/Validation/Validation.md) |
| Setting up validation tools | [Tools Guide](/Guides/Tools/Tools_Guide.md) |
| NeTEx basics for newcomers | [FAQ](/Guides/FAQ/FAQ.md) |
| Parsing NeTEx as a developer | [Developer Quickstart](/Guides/DeveloperQuickstart/DeveloperQuickstart_Guide.md) |
| Official NeTEx XSD | [NeTEx-CEN/NeTEx on GitHub](https://github.com/NeTEx-CEN/NeTEx) |
| EU NAP directory | [EC transport NAP page](https://transport.ec.europa.eu/transport-themes/intelligent-transport-systems/road/action-plan-and-directive/national-access-points_en) |
