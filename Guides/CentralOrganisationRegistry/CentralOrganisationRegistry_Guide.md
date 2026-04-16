# 🏢 Central Organisation Registry — Shared IDs Across Roles

## 1. 🎯 Introduction

In many national data architectures, organisations are managed in a **central registry** that is external to individual NeTEx deliveries. The registry treats each organisation as a single entity with a single identifier — regardless of whether that organisation acts as an authority, an operator, or both.

This creates an interesting modelling pattern: the **same identifier** can appear in both `AuthorityRef` and `OperatorRef` within a NeTEx delivery, because the delivery only contains references (`@ref`), not inline object definitions.

In this guide you will learn:
- 🏢 How a central organisation registry differs from inline NeTEx objects
- 🔄 Why the same ID can be used in `AuthorityRef` and `OperatorRef`
- 📐 What the XSD allows — including full `NeTEx_publication.xsd` validation
- 🏗️ Using `GeneralOrganisation` as the registry's NeTEx export type
- 🧩 How to model an organisation that fills multiple roles
- ✅ Two validating XML examples (registry file + delivery file)

---

## 2. 🔄 Registry Model vs Inline Model

### Inline Model (traditional)

Each organisation is defined as a typed object in the `ResourceFrame`. The XSD enforces identity constraints: an `OperatorRef` must point to an `<Operator>`, and an `AuthorityRef` must point to an `<Authority>`.

```text
ResourceFrame
 └── organisations
      ├── Authority id="ENT:Authority:Ruter"    ← typed object
      └── Operator  id="ENT:Operator:Vy"        ← typed object

Line
 ├── AuthorityRef ref="ENT:Authority:Ruter"      ← must match Authority
 └── OperatorRef  ref="ENT:Operator:Vy"          ← must match Operator
```

With this model, a single organisation **cannot** share an ID across both roles, because `Authority` and `Operator` coexist in `<organisations>` and share the `OrganisationIdType` namespace.

### Registry Model (GeneralOrganisation)

Organisations are defined in a **separate registry file** as `GeneralOrganisation` — a role-neutral NeTEx type. Consuming deliveries reference these using `AuthorityRef` / `OperatorRef`, where the **element name defines the role**.

```text
Registry file (ResourceFrame)
 └── organisations
      ├── GeneralOrganisation id="REG:GeneralOrganisation:Ruter"
      ├── GeneralOrganisation id="REG:GeneralOrganisation:Vy"
      └── GeneralOrganisation id="REG:GeneralOrganisation:Unibuss"

Delivery file (no ResourceFrame organisations)
Line
 ├── AuthorityRef ref="REG:GeneralOrganisation:Ruter"   ← "Ruter as authority"
 └── OperatorRef  ref="REG:GeneralOrganisation:Ruter"   ← "Ruter as operator"
```

The **element name is the role**. The registry doesn't need to distinguish Authority from Operator — the NeTEx context in each delivery defines the relationship.

> [!TIP]
> Both files validate independently against the **full** `NeTEx_publication.xsd` (with all key/keyref constraints). No need for the NoConstraint schema.

---

## 3. 📐 XSD Analysis — What Allows This?

### Type Hierarchy

```text
Organisation (abstract)
 └── TransportOrganisation (abstract)
      ├── Authority
      └── Operator

OrganisationRef_Dummy (abstract)
 └── TransportOrganisationRef (abstract)
      ├── AuthorityRef    type: AuthorityRefStructure
      └── OperatorRef     type: OperatorRefStructure
```

### Ref Value Types

Both `AuthorityRefStructure` and `OperatorRefStructure` extend `TransportOrganisationRefStructure`, which ultimately resolves to `xsd:normalizedString`. There are **no pattern facets** distinguishing the ID types:

```text
ObjectIdType (xsd:normalizedString)
 └── OrganisationIdType
      └── TransportOrganisationIdType
           ├── OperatorIdType        ← no pattern constraint
           └── AuthorityIdType       ← no pattern constraint
```

### Why It Validates Against Full XSD

The `NeTEx_publication.xsd` defines key/keyref constraints with **two** fields:

```xml
<xsd:key name="Operator_AnyVersionedKey">
  <xsd:selector xpath=".//netex:Operator"/>
  <xsd:field xpath="@id"/>
  <xsd:field xpath="@version"/>      ← field 2
</xsd:key>

<xsd:keyref name="Operator_KeyRef" refer="Operator_AnyVersionedKey">
  <xsd:selector xpath=".//netex:OperatorRef"/>
  <xsd:field xpath="@ref"/>
  <xsd:field xpath="@version"/>      ← field 2
</xsd:keyref>
```

Per the XSD specification: *if any keyref field evaluates to an empty node-set (i.e. the attribute is absent), the constraint is **not violated**.* Since our `OperatorRef` and `AuthorityRef` elements omit `@version`, the keyref tuple is incomplete and the validator skips the check.

| File | Keyref triggered? | Reason |
|------|-------------------|--------|
| **Registry** | No refs at all | No `OperatorRef` / `AuthorityRef` present |
| **Delivery** | Refs exist, but no `@version` | Keyref tuple incomplete → constraint not applied |

> [!NOTE]
> This is not a workaround — it is intentional XSD design. Omitting `@version` on refs to external objects is standard practice in NeTEx, allowing cross-file references without breaking validation.

### Line XSD — Both Refs Accepted

`Line` is the **only** NeTEx object with both `AuthorityRef` and `OperatorRef` as direct child elements:

```xml
<!-- From LinePropertiesGroup in netex_line_version.xsd -->
<xsd:element ref="AuthorityRef" minOccurs="0"/>
<xsd:element ref="OperatorRef" minOccurs="0"/>
```

Both are optional (`minOccurs="0"`), and nothing in the XSD prevents them from carrying the same `@ref` value.

---

## 4. 🧩 Modelling Patterns

### Pattern 1 — Same Organisation, Both Roles on Line

The simplest case: an organisation is both the authority (bestiller) and the operator (utfører) for a line.

```xml
<Line id="OPR:Line:1" version="1">
  <Name>Linje 1</Name>
  <TransportMode>bus</TransportMode>
  <AuthorityRef ref="REG:GeneralOrganisation:Ruter"/>
  <OperatorRef ref="REG:GeneralOrganisation:Ruter"/>
</Line>
```

> [!TIP]
> This is common for municipal transit companies that both plan and operate their own services (e.g. a kommune-owned transport company).

### Pattern 2 — Different Organisations per Role

The standard case: a transit authority commissions services from a separate operator.

```xml
<Line id="OPR:Line:2" version="1">
  <Name>Linje 2</Name>
  <TransportMode>bus</TransportMode>
  <AuthorityRef ref="REG:GeneralOrganisation:Ruter"/>
  <OperatorRef ref="REG:GeneralOrganisation:Vy"/>
</Line>
```

### Pattern 3 — Operator on Journey Differs from Line

A line is commissioned by one authority and operated by one default operator, but a specific journey is operated by a substitute.

```xml
<Line id="OPR:Line:3" version="1">
  <Name>Linje 3</Name>
  <TransportMode>rail</TransportMode>
  <AuthorityRef ref="REG:GeneralOrganisation:Jernbanedirektoratet"/>
  <OperatorRef ref="REG:GeneralOrganisation:Vy"/>
</Line>

<!-- A specific journey on Line 3, operated by SJ instead of Vy -->
<ServiceJourney id="OPR:ServiceJourney:3001" version="1">
  <OperatorRef ref="REG:GeneralOrganisation:SJ"/>
  <JourneyPatternRef ref="OPR:JourneyPattern:3A"/>
  ...
</ServiceJourney>
```

> [!NOTE]
> `ServiceJourney` only has `OperatorRef`, not `AuthorityRef`. The authority relationship is always via the Line.

---

## 5. ✅ Validating Examples

Two files, both validate against the **full** `NeTEx_publication.xsd` (with all key/keyref constraints).

### File 1 — Registry Export

The registry publishes its organisations as `GeneralOrganisation` — role-neutral, with contact details.

See [Example_Registry_GeneralOrganisation.xml](Example_Registry_GeneralOrganisation.xml).

```xml
<ResourceFrame id="REG:ResourceFrame:Registry" version="1">
  <organisations>
    <GeneralOrganisation id="REG:GeneralOrganisation:KommuneTransport" version="1">
      <Name>KommuneTransport AS</Name>
      <ContactDetails>
        <Url>https://www.kommunetransport.example.no</Url>
      </ContactDetails>
    </GeneralOrganisation>
    <GeneralOrganisation id="REG:GeneralOrganisation:Fylkeskommune" version="1">
      <Name>Fylkeskommune Mobilitet</Name>
    </GeneralOrganisation>
    <GeneralOrganisation id="REG:GeneralOrganisation:PrivatBuss" version="1">
      <Name>PrivatBuss Norge AS</Name>
    </GeneralOrganisation>
  </organisations>
</ResourceFrame>
```

### File 2 — Operator Delivery

The delivery references registry organisations via `AuthorityRef` and `OperatorRef` — **without `@version`** on the refs, so keyref constraints are not triggered.

See [Example_CentralOrganisationRegistry.xml](Example_CentralOrganisationRegistry.xml).

```xml
<Line id="OPR:Line:1" version="1">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
  <!-- Same org is both authority and operator -->
  <AuthorityRef ref="REG:GeneralOrganisation:KommuneTransport"/>
  <OperatorRef ref="REG:GeneralOrganisation:KommuneTransport"/>
</Line>

<Line id="OPR:Line:2" version="1">
  <Name>Regionbuss 2</Name>
  <TransportMode>bus</TransportMode>
  <!-- Different orgs per role -->
  <AuthorityRef ref="REG:GeneralOrganisation:Fylkeskommune"/>
  <OperatorRef ref="REG:GeneralOrganisation:PrivatBuss"/>
</Line>
```

### Validation Proof

Both files validated against `NeTEx_publication.xsd` (full constraints):

```text
Example_Registry_GeneralOrganisation.xml: VALID
Example_CentralOrganisationRegistry.xml:  VALID
```

---

## 6. ⚠️ Considerations

### For Data Producers

| Concern | Guidance |
|---------|----------|
| **ID format** | Use the registry's codespace consistently (e.g. `REG:GeneralOrganisation:xxx`) |
| **Omit `@version` on refs** | This prevents keyref validation from failing against external objects |
| **No inline objects needed** | The delivery does not need to re-define organisations from the registry |
| **Element = role** | `AuthorityRef` means "this org acts as authority here", `OperatorRef` means "this org operates here" |
| **SIRI compatibility** | SIRI-ET and SIRI-VM use `OperatorRef` — the same registry ID works |

### For Data Consumers

| Concern | Guidance |
|---------|----------|
| **Resolving refs** | Look up the organisation in the central registry, not in the NeTEx file |
| **Building full NeTEx** | If you need inline objects, use `GeneralOrganisation` as the role-neutral type in `<organisations>` |
| **Same ID, different roles** | Do not assume `AuthorityRef="X"` and `OperatorRef="X"` are errors — they indicate dual-role |

### For Registry Operators

| Concern | Guidance |
|---------|----------|
| **Stable IDs** | Organisation IDs must be stable — they are cached in timetable datasets across systems |
| **Export as GeneralOrganisation** | Use `GeneralOrganisation` as the NeTEx type — it is role-neutral and the file validates against the full XSD |
| **Codespace** | Assign a dedicated codespace (e.g. `REG`) for registry-managed identifiers |

---

## 7. 🔗 Related Resources

### Guides in This Repository
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) — Authority, Operator, Contract, and ResponsibilitySet (inline model)
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — Data ownership and cross-frame patterns
- [IT Architecture](../ITArchitecture/ITArchitecture_Guide.md) — Data exchange architecture and actor roles
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — ID formatting rules and codespace patterns
- [MaaS Consumers](../MaaSConsumers/MaaSConsumers_Guide.md) — Consumer perspective on resolving references
