# 📋 ResponsibilitySet as Role-Assignment Model

## 1. 🎯 Introduction

NeTEx provides two mechanisms for associating organisations with data objects:

| Mechanism | How it works | Example |
|-----------|-------------|---------|
| **Direct refs** | `AuthorityRef` / `OperatorRef` as child elements on `Line` | `<OperatorRef ref="..."/>` |
| **ResponsibilitySet** | `responsibilitySetRef` attribute on any `DataManagedObject`, pointing to a set of role assignments | `responsibilitySetRef="..."` |

The direct-ref model is simpler but limited — it only covers two roles (`AuthorityRef` and `OperatorRef`) and is only available on specific objects like `Line`. `ResponsibilitySet` is the general-purpose mechanism, available on **every** `DataManagedObject` in NeTEx, with a richer role vocabulary.

This guide explores using `ResponsibilitySet` as the **primary** mechanism for organisation role assignment, particularly in architectures with a central organisation registry.

In this guide you will learn:
- 📋 What `ResponsibilitySet` is and how it works in the XSD
- 🧩 How stakeholder roles map to the Authority/Operator concept
- 🏗️ How to model organisation responsibilities using `ResponsibilitySet`
- ⚖️ Trade-offs compared to the direct-ref model
- ✅ A validating XML example

---

## 2. 📋 ResponsibilitySet in the XSD

### Structure

A `ResponsibilitySet` is a `DataManagedObject` containing one or more `ResponsibilityRoleAssignment` entries. Each assignment maps a **role** to an **organisation**.

```text
ResponsibilitySet
 └── roles
      ├── ResponsibilityRoleAssignment
      │    ├── StakeholderRoleType      ← "planning", "operation", etc.
      │    ├── DataRoleType             ← "creates", "distributes", etc. (optional)
      │    └── ResponsibleOrganisationRef  ← which organisation
      │
      └── ResponsibilityRoleAssignment
           ├── StakeholderRoleType
           └── ResponsibleOrganisationRef
```

### How Objects Reference It

Every `DataManagedObject` inherits a `responsibilitySetRef` **attribute** (not a child element):

```xml
<Line id="OPR:Line:1" version="1" responsibilitySetRef="REG:ResponsibilitySet:Line1">
  <Name>Linje 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

This attribute is available on `Line`, `ServiceJourney`, `StopPlace`, `Route`, `JourneyPattern`, `FareZone`, and any other object inheriting from `DataManagedObject`.

### Where ResponsibilitySet Lives

`ResponsibilitySet` objects are defined in the `ResourceFrame`:

```xml
<ResourceFrame id="REG:ResourceFrame:Responsibilities" version="1">
  <responsibilitySets>
    <ResponsibilitySet id="REG:ResponsibilitySet:Line1" version="1">
      ...
    </ResponsibilitySet>
  </responsibilitySets>
</ResourceFrame>
```

---

## 3. 🧩 Stakeholder Role Types

The `StakeholderRoleTypeEnumeration` provides a rich vocabulary for describing organisational roles:

| Value | Meaning | Maps to |
|-------|---------|---------|
| `planning` | Plans/commissions the service | ≈ Authority |
| `operation` | Operates the service | ≈ Operator |
| `control` | Controls/monitors the service | — |
| `reservation` | Manages reservations | — |
| `entityLegalOwnership` | Owns the entity/infrastructure | — |
| `fareManagement` | Manages fares and ticketing | — |
| `financing` | Finances the service | — |
| `securityManagement` | Manages security | — |
| `customerService` | Handles customer relations | — |
| `dataRegistrar` | Responsible for data quality | — |
| `facilityManagement` | Manages physical facilities | — |
| `lessor` | Leases out assets | — |
| `tenant` | Leases assets from others | — |
| `other` | Other role | — |

> [!NOTE]
> `StakeholderRoleType` is a **list type** — a single assignment can carry multiple roles (e.g. `planning operation` for an organisation that both plans and operates).

### Data Role Types

In addition to stakeholder roles, each assignment can carry a `DataRoleType` describing how the organisation manages the **data**:

| Value | Meaning |
|-------|---------|
| `creates` | Creates the data |
| `augments` | Enriches existing data |
| `validates` | Validates data quality |
| `collects` | Collects data from sources |
| `aggregates` | Aggregates data from multiple sources |
| `distributes` | Distributes data to consumers |
| `owns` | Is the authoritative owner of the data |
| `all` | All data roles |

---

## 4. 🏗️ Modelling Patterns

### Pattern 1 — Same Organisation, Both Roles

An organisation that both plans and operates a line:

```xml
<ResponsibilitySet id="REG:ResponsibilitySet:SelfOperated" version="1">
  <Name>Self-operated line</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:SO-1" version="1">
      <StakeholderRoleType>planning operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<Line id="OPR:Line:1" version="1" responsibilitySetRef="REG:ResponsibilitySet:SelfOperated">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

> [!TIP]
> Since `StakeholderRoleType` is a list, both roles can be in a single assignment when the same organisation fills them.

### Pattern 2 — Split Authority and Operator

A transit authority commissions services from a separate operator:

```xml
<ResponsibilitySet id="REG:ResponsibilitySet:Line2" version="1">
  <Name>Fylke-commissioned, privately operated</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L2-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Fylkeskommune"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L2-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:PrivatBuss"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<Line id="OPR:Line:2" version="1" responsibilitySetRef="REG:ResponsibilitySet:Line2">
  <Name>Regionbuss 2</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

### Pattern 3 — Richer than Authority/Operator

`ResponsibilitySet` can express relationships that the direct-ref model cannot:

```xml
<ResponsibilitySet id="REG:ResponsibilitySet:Line3" version="1">
  <Name>Complex rail line</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L3-Plan" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Jernbanedirektoratet"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L3-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Vy"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L3-Infra" version="1">
      <StakeholderRoleType>entityLegalOwnership</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:BaneNOR"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:L3-Fare" version="1">
      <StakeholderRoleType>fareManagement</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Entur"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>
```

This captures four distinct organisational responsibilities on a single line — something impossible with only `AuthorityRef` and `OperatorRef`.

### Pattern 4 — Shared ResponsibilitySet Across Objects

A single `ResponsibilitySet` can be referenced by multiple objects:

```xml
<ResponsibilitySet id="REG:ResponsibilitySet:FylkesBuss" version="1">
  <Name>All Fylke bus lines</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:FB-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Fylkeskommune"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:FB-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:PrivatBuss"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<!-- Multiple lines share the same responsibility set -->
<Line id="OPR:Line:10" version="1" responsibilitySetRef="REG:ResponsibilitySet:FylkesBuss">
  <Name>Rute 10</Name>
  <TransportMode>bus</TransportMode>
</Line>

<Line id="OPR:Line:11" version="1" responsibilitySetRef="REG:ResponsibilitySet:FylkesBuss">
  <Name>Rute 11</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

### Pattern 5 — Journey-Level Override

A `ServiceJourney` can reference a different `ResponsibilitySet` than its parent `Line`, enabling operator override at the journey level:

```xml
<ResponsibilitySet id="REG:ResponsibilitySet:SubstitutOper" version="1">
  <Name>Substitute operator for specific journeys</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:Sub-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:SubstituBuss"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<ServiceJourney id="OPR:ServiceJourney:1001" version="1"
                responsibilitySetRef="REG:ResponsibilitySet:SubstitutOper">
  <JourneyPatternRef ref="OPR:JourneyPattern:1A"/>
  ...
</ServiceJourney>
```

---

## 5. 📐 XSD Validation Analysis

### The `responsibilitySetRef` Attribute

The `responsibilitySetRef` on `DataManagedObject` is an **attribute** of type `ResponsibilitySetIdType` (a plain string type). The keyref constraint in `NeTEx_publication.xsd` only covers **elements** named `ResponsibilitySetRef`:

```xml
<xsd:keyref name="ResponsibilitySet_AnyKeyRef" refer="netex:ResponsibilitySet_AnyVersionedKey">
  <xsd:selector xpath=".//netex:ResponsibilitySetRef | .//netex:DefaultResponsibilitySetRef | ..."/>
  <xsd:field xpath="@ref"/>
  <xsd:field xpath="@version"/>
</xsd:keyref>
```

The attribute `responsibilitySetRef="..."` is **not matched** by this selector — it only matches child elements. Therefore, the attribute is **not constrained** by keyref validation.

### The `ResponsibleOrganisationRef` Element

Inside `ResponsibilityRoleAssignment`, `ResponsibleOrganisationRef` IS covered by a keyref:

```xml
<xsd:keyref name="Organisation_AnyKeyRef" refer="netex:Organisation_AnyVersionedKey">
  <xsd:selector xpath=".//netex:OrganisationRef | .//netex:ResponsibleOrganisationRef | .//netex:ProvidedByRef"/>
  <xsd:field xpath="@ref"/>
  <xsd:field xpath="@version"/>
</xsd:keyref>

<xsd:key name="Organisation_AnyVersionedKey">
  <xsd:selector xpath=".//netex:GeneralOrganisation | .//netex:Authority | .//netex:Operator | ..."/>
  <xsd:field xpath="@id"/>
  <xsd:field xpath="@version"/>
</xsd:key>
```

The same two-field tuple mechanism applies: if `@version` is omitted on `ResponsibleOrganisationRef`, the keyref tuple is incomplete and the constraint is **not violated**.

### Validation Summary

| Element/Attribute | Keyref constrained? | Omit `@version` needed? |
|-------------------|---------------------|-------------------------|
| `responsibilitySetRef` (attribute on Line etc.) | **No** — not matched by keyref selector | No — attribute is unconstrained |
| `ResponsibleOrganisationRef` (element in role assignment) | **Yes** — Organisation_AnyKeyRef | Yes — omit to skip keyref |
| `ResponsibilitySetRef` (element, e.g. in role assignment) | **Yes** — ResponsibilitySet_AnyKeyRef | Yes — omit to skip keyref |

---

## 6. ⚖️ Comparison: ResponsibilitySet vs Direct Refs

| Aspect | Direct Refs (`AuthorityRef`/`OperatorRef`) | `ResponsibilitySet` |
|--------|-------------------------------------------|---------------------|
| **Roles available** | 2 (authority, operator) | 14+ (planning, operation, control, fareManagement, ...) |
| **Available on** | `Line` only (both); `ServiceJourney` (OperatorRef only) | Every `DataManagedObject` |
| **Multiple orgs per object** | Max 2 (one per element) | Unlimited role assignments |
| **Reusability** | Each Line must repeat refs | One set, many referencing objects |
| **Consumer readability** | Immediate — flat lookup | Requires resolution: object → responsibility set → role assignments |
| **SIRI compatibility** | Yes — SIRI uses `OperatorRef` directly | No — SIRI does not resolve `ResponsibilitySet` |
| **Ecosystem support** | Universal | Limited — most consumers don't process it |

### The NeTEx Standard's Position (v2.0)

The XSD annotation on `Line` explicitly states:

> *"An OPERATOR should be set, even when the same as the AUTHORITY. In some cases OPERATOR or AUTHORITY are managed through a ResponsibilitySet. However, for compatibility OperatorRef and AuthorityRef still should be filled in."* — `LinePropertiesGroup`, v2.0

This means NeTEx acknowledges `ResponsibilitySet` as a valid mechanism but recommends **keeping direct refs for compatibility**.

### Recommendation

| Approach | When to use |
|----------|-------------|
| **ResponsibilitySet only** | Greenfield systems where you control all consumers and need rich role modelling |
| **Direct refs only** | Maximum interoperability with existing ecosystem (SIRI, GTFS converters, journey planners) |
| **Both (recommended)** | Use `ResponsibilitySet` for rich semantics AND keep `AuthorityRef`/`OperatorRef` for backward-compatible consumers |

---

## 7. ✅ Validating Example

See [Example_ResponsibilitySet.xml](Example_ResponsibilitySet.xml) for the full validating file.

The example demonstrates:
- `ResponsibilitySet` definitions in `ResourceFrame` with `GeneralOrganisation` objects
- Multiple stakeholder roles per line (planning, operation, entityLegalOwnership)
- `responsibilitySetRef` attribute on `Line` and `ServiceJourney`
- Shared `ResponsibilitySet` across multiple lines
- Journey-level operator override via separate `ResponsibilitySet`
- Full validation against `NeTEx_publication.xsd`

```xml
<!-- Registry organisations as GeneralOrganisation -->
<GeneralOrganisation id="REG:GeneralOrganisation:KommuneTransport" version="1">
  <Name>KommuneTransport AS</Name>
</GeneralOrganisation>

<!-- ResponsibilitySet: self-operated line -->
<ResponsibilitySet id="REG:ResponsibilitySet:SelfOperated" version="1">
  <Name>Self-operated (planning + operation)</Name>
  <roles>
    <ResponsibilityRoleAssignment id="REG:ResponsibilityRoleAssignment:SO-1" version="1">
      <StakeholderRoleType>planning operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport" version="1"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<!-- Line using responsibilitySetRef attribute -->
<Line id="OPR:Line:1" version="1" responsibilitySetRef="REG:ResponsibilitySet:SelfOperated">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

---

## 8. 🔗 Related Resources

### Guides in This Folder
- [Central Organisation Registry](CentralOrganisationRegistry_Guide.md) — Using `AuthorityRef`/`OperatorRef` with shared IDs from a central registry

### Other Guides
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) — Authority, Operator, Contract, and ResponsibilitySet (inline model)
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — Data ownership and cross-frame patterns

### XSD References
- `netex_responsibilitySet_version.xsd` — ResponsibilitySet and ResponsibilityRoleAssignment definitions
- `netex_responsibility_support.xsd` — StakeholderRoleTypeEnumeration, DataRoleTypeEnumeration
- `netex_responsibility_version.xsd` — DataManagedObjectStructure with `responsibilitySetRef` attribute
