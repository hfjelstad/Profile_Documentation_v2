# 🔄 Organisation Migration — From Typed Objects to Registry Pattern

## 1. 🎯 Introduction

NeTEx profiles currently require typed `Authority` and `Operator` objects inline in each delivery's `ResourceFrame`. When migrating to a central organisation registry, a **transition period** is needed where deliveries still contain these typed objects — but link them back to the registry.

This guide documents a **short-term migration pattern** using `derivedFromObjectRef` to connect typed Authority/Operator objects to their role-neutral `GeneralOrganisation` counterparts in the registry, as well as the full **migration roadmap** from typed objects to ResponsibilitySet.

In this guide you will learn:
- 🔄 Why a migration path is needed (backward compatibility)
- 🔗 How `derivedFromObjectRef` traces typed objects to registry entities
- 📐 XSD analysis of all connection mechanisms and why `derivedFromObjectRef` is preferred
- 🏗️ Short-term modelling pattern with validating example
- 🗺️ Migration roadmap: typed objects → ResponsibilitySet

---

## 2. 🔄 The Migration Problem

### Current State — Typed Objects Everywhere

Existing NeTEx consumers expect inline Authority/Operator objects:

```xml
<ResourceFrame>
  <organisations>
    <Authority id="ENT:Authority:Ruter" version="1">
      <Name>Ruter AS</Name>
    </Authority>
    <Operator id="ENT:Operator:Vy" version="1">
      <Name>Vy AS</Name>
      <OperatorActivities>passenger</OperatorActivities>
    </Operator>
  </organisations>
</ResourceFrame>
```

### Target State — Registry References

The long-term goal is role-neutral organisations in a central registry, with roles assigned via `ResponsibilitySet`:

```xml
<!-- No local typed objects — just ResponsibilitySet pointing to registry -->
<Line id="ENT:Line:1" version="1"
      responsibilitySetRef="ENT:ResponsibilitySet:Line1">
  <Name>Linje 1</Name>
</Line>
```

### The Gap

Switching directly breaks consumers that:
- Look for `<Authority>` / `<Operator>` elements in `<organisations>`
- Validate against profiles that mandate inline organisation objects
- Index organisations by their concrete type

A transition pattern lets producers **keep typed objects** while establishing **traceability** to the registry.

---

## 3. 🔗 Connection Mechanisms — Why `derivedFromObjectRef`?

NeTEx offers multiple ways to link a typed object back to a registry entity:

### Available Mechanisms

| # | Mechanism | Level | Type | Pros | Cons |
|---|-----------|-------|------|------|------|
| 1 | `derivedFromObjectRef` | `EntityInVersion` (everything) | attribute | Lightweight, semantic fit, no child elements | Plain string, no XSD validation |
| 2 | `relatedOrganisations` | `Organisation` | element | Rich (name, role, description) | Heavy — requires its own ID, version, child elements |
| 3 | `delegatedFrom` | `Organisation` | element | List of org refs | Wrong semantics (TAP TSI delegation) |
| 4 | `responsibilitySetRef` | `DataManagedObject` | attribute | General-purpose, role vocabulary | Indirection — requires separate ResponsibilitySet object |

### Recommended: `derivedFromObjectRef`

The `derivedFromObjectRef` attribute is defined in `BasicModificationDetailsGroup` on `EntityInVersionStructure` — inherited by **every** NeTEx object:

```xml
<xsd:attribute name="derivedFromObjectRef" type="ObjectIdType" use="optional">
    <xsd:annotation>
        <xsd:documentation>Identity of object from which this object of ENTITY
        was derived. Normally the same.</xsd:documentation>
    </xsd:annotation>
</xsd:attribute>
```

It is the best fit for the migration pattern because:
- **Semantically correct** — the typed Authority *is derived from* the registry entity
- **Zero overhead** — just an attribute, no child elements or additional objects
- **Non-breaking** — consumers that don't understand it simply ignore it
- **Universal** — works on Authority, Operator, and any future organisation type

The companion attribute `derivedFromVersionRef` can optionally specify which version of the registry entity was used.

---

## 4. 🏗️ Short-Term Pattern

### Structure

```text
Registry (external)                  Delivery (local)
┌────────────────────────┐           ┌─────────────────────────────────────────────┐
│ GeneralOrganisation    │           │ Authority                                   │
│   id="REG:...Ruter"   │◄──────────│   id="ENT:Authority:Ruter"                  │
│   Name, Contact, etc. │  derived  │   derivedFromObjectRef="REG:...Ruter"       │
└────────────────────────┘  FromObj  │   Name (can differ / abbreviate)            │
                                     └─────────────────────────────────────────────┘
```

### Example

```xml
<ResourceFrame id="ENT:ResourceFrame:1" version="1">
  <organisations>
    <!-- Authority derived from registry entity -->
    <Authority id="ENT:Authority:Ruter" version="1"
               derivedFromObjectRef="REG:GeneralOrganisation:Ruter">
      <Name>Ruter AS</Name>
    </Authority>

    <!-- Operator derived from same registry -->
    <Operator id="ENT:Operator:Vy" version="1"
              derivedFromObjectRef="REG:GeneralOrganisation:Vy">
      <Name>Vy AS</Name>
      <OperatorActivities>passenger</OperatorActivities>
    </Operator>
  </organisations>
</ResourceFrame>
```

### Key Properties

| Property | Value |
|----------|-------|
| **Local ID** | Delivery codespace (e.g. `ENT:Authority:Ruter`) |
| **Registry link** | `derivedFromObjectRef="REG:GeneralOrganisation:Ruter"` |
| **Version tracking** | Optional: `derivedFromVersionRef="1"` |
| **Refs from Line etc.** | Standard `AuthorityRef`/`OperatorRef` with `@version` → keyref validated |
| **Consumer impact** | None — typed objects are present as before |

### Dual-Role Organisation

An organisation that is both authority and operator gets **two** typed objects, both derived from the same registry entity:

```xml
<Authority id="ENT:Authority:KT" version="1"
           derivedFromObjectRef="REG:GeneralOrganisation:KommuneTransport">
  <Name>KommuneTransport AS</Name>
</Authority>

<Operator id="ENT:Operator:KT" version="1"
          derivedFromObjectRef="REG:GeneralOrganisation:KommuneTransport">
  <Name>KommuneTransport AS</Name>
  <OperatorActivities>passenger</OperatorActivities>
</Operator>
```

> [!NOTE]
> Both Authority and Operator carry the same `derivedFromObjectRef` value, making the dual-role relationship explicit. The registry holds one entity; the delivery expresses two roles.

---

## 5. 📐 XSD Analysis

### `derivedFromObjectRef` Type

The attribute has type `ObjectIdType` — an `xsd:normalizedString` with no constraints:

```text
ObjectIdType (xsd:normalizedString)
 └── no pattern facets
 └── no enumeration
 └── no validation against any key/keyref
```

This means:
- ✅ Any string value is accepted (including cross-codespace IDs)
- ✅ No keyref lookup is performed — the registry entity doesn't need to be in the same file
- ⚠️ No XSD-level guarantee that the referenced object exists
- ⚠️ Typos in the value won't be caught by schema validation

### Where It Lives

```text
EntityStructure
 └── EntityInVersionStructure
      ├── @dataSourceRef
      └── BasicModificationDetailsGroup
           ├── @created
           ├── @changed
           ├── @modification
           ├── @version
           ├── @status
           ├── @derivedFromVersionRef
           ├── @compatibleWithVersionFrameVersionRef
           └── @derivedFromObjectRef    ← here
```

Inherited by `DataManagedObject`, `VersionedChild`, and all concrete types including Authority, Operator, GeneralOrganisation, Line, ServiceJourney, etc.

---

## 6. 🗺️ Migration Roadmap

### Phase 1 — Typed Objects with Registry Traceability (Short-Term)

Deliveries contain Authority/Operator objects as before, with `derivedFromObjectRef` pointing to the registry.

```xml
<Authority id="ENT:Authority:Ruter" version="1"
           derivedFromObjectRef="REG:GeneralOrganisation:Ruter">
  <Name>Ruter AS</Name>
</Authority>
```

**Consumer impact:** None. Consumers that don't understand `derivedFromObjectRef` ignore it.

### Phase 2 — Parallel Model (Transition)

Deliveries contain both:
- Authority/Operator objects (for backward compatibility)
- ResponsibilitySet (for new consumers)

```xml
<ResponsibilitySet id="ENT:ResponsibilitySet:Line1" version="1">
  <roles>
    <ResponsibilityRoleAssignment ...>
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Ruter"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<Line id="ENT:Line:1" version="1"
      responsibilitySetRef="ENT:ResponsibilitySet:Line1">
  <Name>Linje 1</Name>
  <AuthorityRef ref="ENT:Authority:Ruter" version="1"/>  <!-- kept for legacy -->
</Line>
```

**Consumer impact:** New consumers use ResponsibilitySet. Legacy consumers use AuthorityRef/OperatorRef. Both coexist.

### Phase 3 — ResponsibilitySet Only (Target)

Typed Authority/Operator objects are removed. All role assignments via ResponsibilitySet pointing to registry GeneralOrganisations.

```xml
<Line id="ENT:Line:1" version="1"
      responsibilitySetRef="ENT:ResponsibilitySet:Line1">
  <Name>Linje 1</Name>
  <!-- No AuthorityRef / OperatorRef -->
</Line>
```

**Consumer impact:** Consumers must support ResponsibilitySet to resolve organisation roles.

### Summary Table

| Phase | Delivery contains | Registry link | Backward compatible |
|-------|-------------------|---------------|---------------------|
| **1 — Traceability** | Authority + Operator | `derivedFromObjectRef` | ✅ Full |
| **2 — Parallel** | Authority + Operator + ResponsibilitySet | Both mechanisms | ✅ Legacy consumers unaffected |
| **3 — Target** | ResponsibilitySet only | `ResponsibleOrganisationRef` | ❌ Requires consumer migration |

---

## 7. ⚠️ Considerations

### For Data Producers

| Concern | Guidance |
|---------|----------|
| **Registry ID format** | Use the registry's codespace consistently (e.g. `REG:GeneralOrganisation:xxx`) in `derivedFromObjectRef` |
| **Local IDs** | Use your own codespace for the typed objects (e.g. `ENT:Authority:xxx`) |
| **Name synchronisation** | The Name in the typed object may diverge from the registry — consider syncing periodically |
| **Dual-role** | Create separate Authority and Operator objects with the same `derivedFromObjectRef` |
| **Version tracking** | Optionally add `derivedFromVersionRef` to track which registry version was used |

### For Data Consumers

| Concern | Guidance |
|---------|----------|
| **Registry lookup** | When `derivedFromObjectRef` is present, use it to enrich the organisation from the registry |
| **Ignoring the attribute** | If you don't support registries, the attribute is harmless — ignore it |
| **Phase 2 detection** | If both AuthorityRef and responsibilitySetRef exist, prefer ResponsibilitySet for richer role information |

### For Registry Operators

| Concern | Guidance |
|---------|----------|
| **Stable IDs** | Registry IDs in `derivedFromObjectRef` must remain stable across versions |
| **No breaking changes** | Renaming or deleting a registry ID breaks all deliveries that reference it |
| **Version management** | Publish versioned GeneralOrganisation objects so producers can use `derivedFromVersionRef` |

---

## 8. ✅ Validating Example

See [Example_OrganisationMigration.xml](Example_OrganisationMigration.xml).

The example demonstrates Phase 1 (short-term pattern):
- Two Authority objects and two Operator objects with `derivedFromObjectRef` pointing to registry GeneralOrganisations
- A dual-role organisation (KommuneTransport) appearing as both Authority and Operator
- Standard `AuthorityRef`/`OperatorRef` on Lines and `OperatorRef` on ServiceJourneys
- Full key/keyref validation against `NeTEx_publication.xsd`

---

## 9. 🔗 Related Resources

### Guides in This Repository
- [Central Organisation Registry](CentralOrganisationRegistry_Guide.md) — Reference-only pattern (no local typed objects): registry `GeneralOrganisation` IDs used directly in `AuthorityRef`/`OperatorRef`
- [ResponsibilitySet Role Model](ResponsibilitySet_Guide.md) — The target state: `ResponsibilitySet` as the primary role-assignment mechanism
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) — Authority, Operator, Contract, and ResponsibilitySet (inline model)
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — Data ownership and cross-frame patterns

### XSD References
- `BasicModificationDetailsGroup` in `netex_version_support.xsd` — defines `derivedFromObjectRef`
- `EntityInVersionStructure` in `netex_version_version.xsd` — inherits the attribute group
- `Organisation_VersionStructure` in `netex_organisation_version.xsd` — `relatedOrganisations`, `delegatedFrom`
