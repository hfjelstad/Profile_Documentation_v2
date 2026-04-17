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
- 🔀 Separation of concerns: registry owns orgs, delivery owns role assignments
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
<Line id="ENT:Line:1" version="1" responsibilitySetRef="ENT:ResponsibilitySet:Line1">
  <Name>Linje 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

This attribute is available on `Line`, `ServiceJourney`, `StopPlace`, `Route`, `JourneyPattern`, `FareZone`, and any other object inheriting from `DataManagedObject`.

### Where ResponsibilitySet Lives

`ResponsibilitySet` objects are defined in the `ResourceFrame`:

```xml
<ResourceFrame id="ENT:ResourceFrame:Responsibilities" version="1">
  <responsibilitySets>
    <ResponsibilitySet id="ENT:ResponsibilitySet:Line1" version="1">
      ...
    </ResponsibilitySet>
  </responsibilitySets>
</ResourceFrame>
```

---

## 3. 🔀 Separation of Concerns

When using a central organisation registry, there is a natural separation:

| Codespace | Owns | Concern |
|-----------|------|---------|
| **ENT** | Everything in the delivery: `ResponsibilitySet`, `Line`, `ServiceJourney`, etc. | The delivery — what is operated and who fills which role |
| **REG** | Only appears on `ResponsibleOrganisationRef` and `OrganisationRef` in contracts | External reference to the organisation registry |
| **CON** | Only appears on `ContractRef` | External reference to the contract registry |

The registries don't need to know which lines or journeys a contract applies to — that's the delivery's concern. The registries only publish **who** the organisations are and **what** contracts exist between them.

```text
ENT (Delivery)                              REG (Org registry)   CON (Contract registry)
┌───────────────────────────────────────┐     ┌──────────────────┐ ┌──────────────────┐
│ ResponsibilitySet: FylkePrivat      │     │ GeneralOrg:      │ │ Contract:        │
│   planning  → REG:Fylkeskommune   │────►│  Fylkeskommune   │ │  FK-PB-2026      │
│   operation → REG:PrivatBuss       │     │  PrivatBuss      │ │  FK-SB-2026      │
│   contract  → CON:FK-PB-2026      │────►│  ...             │ │  KT-SelfOp-2026  │
│                                       │     └──────────────────┘ └──────────────────┘
│ Line: Regionbuss 2                    │
│   responsibilitySetRef=FylkePrivat   │
└───────────────────────────────────────┘
```

Each role is modelled as a **separate** `ResponsibilityRoleAssignment` — even when the same organisation fills both roles. This keeps the structure consistent and each assignment independently updatable.

---

## 4. 🧩 Stakeholder Role Types

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

## 5. 🏗️ Modelling Patterns

### Pattern 1 — Same Organisation, Both Roles

An organisation that both plans and operates a line. Each role gets its own assignment:

```xml
<ResponsibilitySet id="ENT:ResponsibilitySet:SelfOperated" version="1">
  <Name>Self-operated line</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:SO-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:SO-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<Line id="ENT:Line:1" version="1" responsibilitySetRef="ENT:ResponsibilitySet:SelfOperated">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

> [!TIP]
> Always use separate assignments per role — even for the same organisation. This keeps the structure consistent and each assignment independently updatable.

### Pattern 2 — Split Authority and Operator

A transit authority commissions services from a separate operator, linked to an external contract:

```xml
<ResponsibilitySet id="ENT:ResponsibilitySet:Line2" version="1">
  <Name>Fylke-commissioned, privately operated</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L2-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Fylkeskommune"/>
      <AssociatedContract>
        <ContractRef ref="CON:Contract:FK-PB-2026"/>
      </AssociatedContract>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L2-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:PrivatBuss"/>
      <AssociatedContract>
        <ContractRef ref="CON:Contract:FK-PB-2026"/>
      </AssociatedContract>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<Line id="ENT:Line:2" version="1" responsibilitySetRef="ENT:ResponsibilitySet:Line2">
  <Name>Regionbuss 2</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

### Pattern 3 — Richer than Authority/Operator

`ResponsibilitySet` can express relationships that the direct-ref model cannot:

```xml
<ResponsibilitySet id="ENT:ResponsibilitySet:Line3" version="1">
  <Name>Complex rail line</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L3-Plan" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Jernbanedirektoratet"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L3-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Vy"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L3-Infra" version="1">
      <StakeholderRoleType>entityLegalOwnership</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:BaneNOR"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:L3-Fare" version="1">
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
<ResponsibilitySet id="ENT:ResponsibilitySet:FylkesBuss" version="1">
  <Name>All Fylke bus lines</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:FB-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:Fylkeskommune"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:FB-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:PrivatBuss"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<!-- Multiple lines share the same responsibility set -->
<Line id="ENT:Line:10" version="1" responsibilitySetRef="ENT:ResponsibilitySet:FylkesBuss">
  <Name>Rute 10</Name>
  <TransportMode>bus</TransportMode>
</Line>

<Line id="ENT:Line:11" version="1" responsibilitySetRef="ENT:ResponsibilitySet:FylkesBuss">
  <Name>Rute 11</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

### Pattern 5 — Journey-Level Override

A `ServiceJourney` can reference a different `ResponsibilitySet` than its parent `Line`, enabling operator override at the journey level:

```xml
<ResponsibilitySet id="ENT:ResponsibilitySet:SubstitutOper" version="1">
  <Name>Substitute operator for specific journeys</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:Sub-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:SubstituBuss"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<ServiceJourney id="ENT:ServiceJourney:1001" version="1"
                responsibilitySetRef="ENT:ResponsibilitySet:SubstitutOper">
  <JourneyPatternRef ref="ENT:JourneyPattern:1A"/>
  ...
</ServiceJourney>
```

---

## 6. 📐 XSD Validation Analysis

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
| `ContractRef` (element in AssociatedContract) | **Yes** — Contract_AnyKeyRef | Yes — omit to skip keyref |
| `OrganisationRef` (element in contractees/contractors) | **Yes** — Organisation_AnyKeyRef | Yes — omit to skip keyref |

---

## 7. 📝 Contract Integration

### Contract as External Registry Object

`Contract` (v2.0) represents an agreement between organisations. When managed in a **contract registry**, it follows the same external-reference pattern as organisations:

| Codespace | Object | Concern |
|-----------|--------|---------|
| **CON** | `Contract` | Who pays whom — the contractual relationship |
| **REG** | `GeneralOrganisation` | Who the parties are |
| **ENT** | `ResponsibilitySet` | What roles they play on which lines/journeys |

### AssociatedContract in ResponsibilityRoleAssignment

Each role assignment can reference an external contract via `AssociatedContract` > `ContractRef`:

```xml
<ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:FP-Oper" version="1">
  <StakeholderRoleType>operation</StakeholderRoleType>
  <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:PrivatBuss"/>
  <AssociatedContract>
    <ContractRef ref="CON:Contract:FK-PB-2026"/>
  </AssociatedContract>
</ResponsibilityRoleAssignment>
```

### Contract Structure

`Contract` is a `DataManagedObject` with:

| Element | Description |
|---------|-------------|
| `Name` | Human-readable name |
| `ContractType` | `formal`, `informal`, `written`, `oral`, `plainUnderstood` |
| `LegalStatus` | `binding`, `nonBinding` |
| `contractees` | The commissioning party (`OrganisationRef` list) |
| `contractors` | The delivering party (`OrganisationRef` list) |
| `contractDocuments` | External links (PDFs etc.) |

### What Contract Provides vs What ResponsibilitySet Provides

| Concern | Contract | ResponsibilitySet |
|---------|----------|--------------------|
| **Who are the parties?** | ✅ contractees + contractors | ✅ ResponsibleOrganisationRef |
| **What is the legal basis?** | ✅ ContractType, LegalStatus | ❌ |
| **What role does each party play?** | ❌ (only contractee/contractor) | ✅ StakeholderRoleType (14+ roles) |
| **Which NeTEx objects does it apply to?** | ❌ | ✅ via `responsibilitySetRef` on Line, ServiceJourney, etc. |

Contract and ResponsibilitySet are **complementary** — Contract captures the legal relationship, ResponsibilitySet binds it to specific operational objects.

### Keyref for ContractRef

`ContractRef` follows the same two-field keyref pattern:

```xml
<xsd:keyref name="Contract_AnyKeyRef" refer="netex:Contract_AnyVersionedKey">
  <xsd:selector xpath=".//netex:ContractRef | .//netex:SupplyContractRef"/>
  <xsd:field xpath="@ref"/>
  <xsd:field xpath="@version"/>
</xsd:keyref>
```

Omitting `@version` on `ContractRef` skips the keyref — same mechanism as `ResponsibleOrganisationRef`.

---

## 8. ⚖️ Comparison: ResponsibilitySet vs Direct Refs

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

## 9. ✅ Validating Example

See [Example_ResponsibilitySet.xml](Example_ResponsibilitySet.xml) for the full validating file.

The example demonstrates:
- `GeneralOrganisation` objects under `REG:` codespace (external org registry)
- `Contract` objects under `CON:` codespace (external contract registry)
- All delivery objects under `ENT:` codespace — single codespace for the entire delivery
- `ContractRef` in `AssociatedContract` linking role assignments to external contracts
- Each role as its own `ResponsibilityRoleAssignment` — even when same org fills both
- `ResponsibleOrganisationRef` and `ContractRef` without `@version` (cross-codespace refs, keyref skipped)
- `responsibilitySetRef` attribute on `Line` and `ServiceJourney`
- Journey-level operator override via separate `ResponsibilitySet`
- Full validation against `NeTEx_publication.xsd`

```xml
<!-- Registry organisations as GeneralOrganisation (REG codespace — external) -->
<GeneralOrganisation id="REG:GeneralOrganisation:KommuneTransport" version="1">
  <Name>KommuneTransport AS</Name>
</GeneralOrganisation>

<!-- ResponsibilitySet (ENT codespace — delivery concern) -->
<ResponsibilitySet id="ENT:ResponsibilitySet:SelfOperated" version="1">
  <Name>Self-operated (planning + operation)</Name>
  <roles>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:SO-Auth" version="1">
      <StakeholderRoleType>planning</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport"/>
    </ResponsibilityRoleAssignment>
    <ResponsibilityRoleAssignment id="ENT:ResponsibilityRoleAssignment:SO-Oper" version="1">
      <StakeholderRoleType>operation</StakeholderRoleType>
      <ResponsibleOrganisationRef ref="REG:GeneralOrganisation:KommuneTransport"/>
    </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>

<!-- Line using responsibilitySetRef attribute (ENT codespace) -->
<Line id="ENT:Line:1" version="1" responsibilitySetRef="ENT:ResponsibilitySet:SelfOperated">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
</Line>
```

---

## 10. 🔗 Related Resources

### Guides in This Folder
- [Central Organisation Registry](CentralOrganisationRegistry_Guide.md) — Using `AuthorityRef`/`OperatorRef` with shared IDs from a central registry

### Other Guides
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) — Authority, Operator, Contract, and ResponsibilitySet (inline model)
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — Data ownership and cross-frame patterns

### XSD References
- `netex_responsibilitySet_version.xsd` — ResponsibilitySet and ResponsibilityRoleAssignment definitions
- `netex_responsibility_support.xsd` — StakeholderRoleTypeEnumeration, DataRoleTypeEnumeration
- `netex_responsibility_version.xsd` — DataManagedObjectStructure with `responsibilitySetRef` attribute
