# NeTEx XML Validation Guide (for LLM Agents)

This guide explains how to validate NeTEx XML example files against the official XSD schema. It covers local validation, CI validation, and common validation errors with their fixes.

---

## 1. Schema Location

The NeTEx XSD schema is maintained at the official [NeTEx-CEN/NeTEx](https://github.com/NeTEx-CEN/NeTEx) repository. Clone it locally:

```bash
git clone --depth=1 https://github.com/NeTEx-CEN/NeTEx.git netex-xsd
```

The root schema file is then:

```
netex-xsd/xsd/NeTEx_publication.xsd
```

This is the root schema file. It imports all NeTEx sub-schemas.

---

## 2. Local Validation

### 2.1 Using the validation script

The repo includes a validation script:

```bash
# Validate ALL XML examples under Objects/ and Frames/
./scripts/validate-xml.sh

# Validate only git-changed files (vs EnStandardBranch)
./scripts/validate-xml.sh --changed

# Validate specific files
./scripts/validate-xml.sh Objects/Quay/Example_Quay_NP.xml
```

**Requires:** `xmllint` (from `libxml2-utils` on Linux, `brew install libxml2` on macOS, `choco install xsltproc` on Windows).

The script auto-fetches the XSD from `origin/main` if not present locally.

### 2.2 Using Python + lxml (Windows alternative)

If `xmllint` is not available, use Python with `lxml`:

```bash
pip install lxml
```

```python
from lxml import etree

schema_doc = etree.parse("netex-xsd/xsd/NeTEx_publication.xsd")
schema = etree.XMLSchema(schema_doc)

doc = etree.parse("Objects/Quay/Example_Quay_NP.xml")
if schema.validate(doc):
    print("OK")
else:
    for err in schema.error_log:
        print(err)
```

To fetch the schema:
```bash
git clone --depth=1 https://github.com/NeTEx-CEN/NeTEx.git netex-xsd
```

### 2.3 Batch validation (Python)

```python
import glob
from lxml import etree

schema = etree.XMLSchema(etree.parse("netex-xsd/xsd/NeTEx_publication.xsd"))

for f in sorted(set(
    glob.glob("Objects/**/Example_*.xml", recursive=True) +
    glob.glob("Frames/**/Example_*.xml", recursive=True) +
    glob.glob("Frames/Example_*.xml")
)):
    try:
        doc = etree.parse(f)
        if not schema.validate(doc):
            print(f"FAIL: {f}")
            for err in schema.error_log:
                print(f"  {err}")
    except etree.XMLSyntaxError as e:
        print(f"PARSE ERROR: {f} -- {e}")
```

---

## 3. CI Validation

Two GitHub Actions workflows handle validation:

| Workflow | Trigger | What it does |
|----------|---------|-------------|
| `PR_Validator.yml` | Pull request (opened/synchronize/reopen) on `**/*.xml` paths | Validates changed XML files in PRs |
| `Commit_Validator.yml` | Push to `EnStandardBranch` on `**/*.xml` paths | Validates changed XML on push (fail-fast) |

Both call the reusable `INT_NeTEx_Validator.yml` workflow which:
1. Checks out the code
2. Clones the official NeTEx XSD from [NeTEx-CEN/NeTEx](https://github.com/NeTEx-CEN/NeTEx)
3. Installs `xmllint`
4. Diffs changed XML files against the base branch
5. Validates each changed XML file against `NeTEx_publication.xsd`

A separate `NeTEx_EXT.yml` workflow provides external/API validation (for Power Automate).

---

## 4. XML Example File Requirements

Every XML example must:

1. **Have a root `PublicationDelivery` element** (unless it's a bare object like Route_MIN which is a standalone fragment)
2. **Declare the NeTEx namespace:** `xmlns="http://www.netex.org.uk/netex"`
3. **Include `PublicationTimestamp` and `ParticipantRef`** as direct children of `PublicationDelivery`
4. **Use `dataObjects` (lowercase d)** — not `DataObjects`
5. **Wrap objects in the correct Frame type** (SiteFrame for stops, TimetableFrame for journeys, etc.)

---

## 5. Common Validation Errors and Fixes

### 5.1 Element ordering (most common)

**Error:** `Element 'X': This element is not expected. Expected is one of (Y, Z, ...)`

**Cause:** NeTEx XSD uses `xs:sequence`, so child elements must appear in the exact order defined by the schema. This order follows the inheritance chain — elements from parent types come before elements from child types.

**General inheritance ordering (innermost to outermost):**
1. `ValidBetween` (EntityInVersion level)
2. `keyList`, `Extensions`, `BrandingRef` (DataManagedObject level)
3. `Name`, `ShortName`, `Description`, `PrivateCode` (GroupOfEntities level)
4. `Centroid` (Zone level)
5. `AccessibilityAssessment` (SiteElement level)
6. `TopographicPlaceRef`, `ParentSiteRef` (Site level)
7. Object-specific elements (StopPlace, Quay, Parking, etc.)

**Fix:** Reorder elements to match the XSD sequence. When unsure, check the XSD type definition and trace the inheritance chain.

### 5.2 Element casing

**Error:** `Element 'PointsInSequence': This element is not expected. Expected is ... pointsInSequence`

**Cause:** NeTEx uses lowercase-first for collection/container properties (`dataObjects`, `pointsInSequence`, `vehicleJourneys`, `stopPlaces`, `quays`, `parkingProperties`, `boardingPositions`, `journeyInterchanges`).

**Fix:** Use the exact casing from the XSD. Property elements (containers) are lowercase-first. Type elements are uppercase-first.

### 5.3 Keyref validation (versioned refs)

**Error:** `No match found for key-sequence ['X:Y:Z', '1'] of keyref 'Journey_KeyRef'`

**Cause:** A `*Ref` element (e.g., `ServiceJourneyRef`) includes a `version="X"` attribute, which triggers keyref validation requiring the referenced object to exist in the same file with matching `id` and `version`.

**Fix options:**
- **Remove the `version` attribute** from the Ref element (recommended for external references)
- **Add the referenced object** as a stub in the same file within a CompositeFrame
- **Use `versionRef` instead of `version`** — `versionRef` does not trigger keyref validation

### 5.4 Missing wrapper

**Error:** `No matching global declaration available for the validation root` or parse errors about extra content

**Cause:** The file has a bare element (e.g., `<VehicleTypes>`) or multiple root elements without a `PublicationDelivery` wrapper.

**Fix:** Wrap in `PublicationDelivery` with the appropriate Frame:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" version="2.0">
  <PublicationTimestamp>2026-01-01T00:00:00Z</PublicationTimestamp>
  <ParticipantRef>EuPro</ParticipantRef>
  <dataObjects>
    <ResourceFrame id="ERP:ResourceFrame:1" version="1">
      <!-- content here -->
    </ResourceFrame>
  </dataObjects>
</PublicationDelivery>
```

### 5.5 Invalid enum values

**Error:** `[facet 'enumeration'] The value 'X' is not an element of the set {Y, Z, ...}`

**Cause:** An element uses a value not in the XSD-defined enumeration.

**Common examples:**
- `PropulsionType`: valid values are `combustion`, `electric`, `electricAssist`, `hybrid`, `human`, `other` (NOT `diesel`, `hydrogen`)
- `StopPlaceType`: valid values include `onstreetBus`, `busStation`, `railStation`, `metroStation`, `airport`, `harbourPort`, etc.

**Fix:** Use a value from the enumeration listed in the error message.

### 5.6 Invalid attributes

**Error:** `attribute 'X': The attribute 'X' is not allowed`

**Cause:** An element has an attribute that the XSD doesn't permit (e.g., `version` on `Codespace`).

**Fix:** Remove the invalid attribute.

### 5.7 Identity constraint fields

**Error:** `Not all fields of key identity-constraint 'X_AnyVersionedKey' evaluate to a node`

**Cause:** An element that requires both `id` and `version` attributes (because it's a versioned entity) is missing one of them.

**Fix:** Add both `id` and `version` attributes to the element.

---

## 6. Frame Type Reference

Each Frame Description file documents which object types it contains in **Section 3 ("Contained Elements")**. See the individual Frame descriptions:

- [ResourceFrame](../../Frames/ResourceFrame/Description_ResourceFrame.md)
- [ServiceFrame](../../Frames/ServiceFrame/Description_ServiceFrame.md)
- [TimetableFrame](../../Frames/TimetableFrame/Description_TimetableFrame.md)
- [SiteFrame](../../Frames/SiteFrame/Description_SiteFrame.md)
- [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Description_ServiceCalendarFrame.md)
- [FareFrame](../../Frames/FareFrame/Description_FareFrame.md)
- [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Description_VehicleScheduleFrame.md)

Use a `CompositeFrame` when cross-frame references need to resolve within the same file.

---

## 7. Codespace and Profile Conventions

See [LLM/README.md](../README.md#2-profiles) for profile codes, codespace conventions, and naming rules.

---

## 8. Post-fix Checklist

See [LLM/README.md Section 7](../README.md#7-validation--quality-assurance) for the full set of synchronization rules between XML examples, Tables, and Descriptions.

After any XML fix, always re-run validation to confirm the fix works.
