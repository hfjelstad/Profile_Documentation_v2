# 🏢 Central Organisation Registry — Shared IDs Across Roles

## 1. 🎯 Introduction

In many national data architectures, organisations are managed in a **central registry** that is external to individual NeTEx deliveries. The registry treats each organisation as a single entity with a single identifier — regardless of whether that organisation acts as an authority, an operator, or both.

This creates an interesting modelling pattern: the **same identifier** can appear in both `AuthorityRef` and `OperatorRef` within a NeTEx delivery, because the delivery only contains references (`@ref`), not inline object definitions.

In this guide you will learn:
- 🏢 How a central organisation registry differs from inline NeTEx objects
- 🔄 Why the same ID can be used in `AuthorityRef` and `OperatorRef`
- 📐 What the XSD allows and what it constrains
- 🧩 How to model an organisation that fills multiple roles
- ✅ A validating XML example

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

### Registry Model (external)

Organisations are **not defined** in the delivery. They exist in an external registry. The delivery only carries `@ref` strings — no inline objects to validate against.

```text
Central Registry (external)
 └── Organisation id="REG:Organisation:Ruter"    ← untyped, role-neutral

NeTEx delivery (no ResourceFrame organisations)
Line
 ├── AuthorityRef ref="REG:Organisation:Ruter"   ← "Ruter as authority"
 └── OperatorRef  ref="REG:Organisation:Ruter"   ← "Ruter as operator"
```

The **element name is the role**. The registry doesn't need to know about NeTEx types — the context in the delivery defines the relationship.

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

### When Validation Applies

| Scenario | Ref validated? | Reason |
|----------|---------------|--------|
| Inline objects in `<organisations>` | **Yes** | XSD keyref constraints match `@ref` to `@id` on typed elements |
| No inline objects (external registry) | **No** | No `@id` to validate against — `@ref` is just a string |
| Mixed (some inline, some external) | **Partial** | Only inline objects trigger keyref validation |

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
  <AuthorityRef ref="REG:Organisation:Ruter"/>
  <OperatorRef ref="REG:Organisation:Ruter"/>
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
  <AuthorityRef ref="REG:Organisation:Ruter"/>
  <OperatorRef ref="REG:Organisation:Vy"/>
</Line>
```

### Pattern 3 — Operator on Journey Differs from Line

A line is commissioned by one authority and operated by one default operator, but a specific journey is operated by a substitute.

```xml
<Line id="OPR:Line:3" version="1">
  <Name>Linje 3</Name>
  <TransportMode>rail</TransportMode>
  <AuthorityRef ref="REG:Organisation:Jernbanedirektoratet"/>
  <OperatorRef ref="REG:Organisation:Vy"/>
</Line>

<!-- A specific journey on Line 3, operated by SJ instead of Vy -->
<ServiceJourney id="OPR:ServiceJourney:3001" version="1">
  <OperatorRef ref="REG:Organisation:SJ"/>
  <JourneyPatternRef ref="OPR:JourneyPattern:3A"/>
  ...
</ServiceJourney>
```

> [!NOTE]
> `ServiceJourney` only has `OperatorRef`, not `AuthorityRef`. The authority relationship is always via the Line.

---

## 5. ✅ Validating Example

The following complete XML validates against the NeTEx XSD. It demonstrates:
- No `ResourceFrame` with inline organisations (external registry)
- Same `@ref` used in both `AuthorityRef` and `OperatorRef` on a Line
- Different organisations on different Lines
- Operator override on a ServiceJourney

See [Example_CentralOrganisationRegistry.xml](Example_CentralOrganisationRegistry.xml) for the full file.

```xml
<Line id="OPR:Line:1" version="1">
  <Name>Stadsbuss 1</Name>
  <TransportMode>bus</TransportMode>
  <!-- Same org is both authority and operator -->
  <AuthorityRef ref="REG:Organisation:KommuneTransport"/>
  <OperatorRef ref="REG:Organisation:KommuneTransport"/>
</Line>

<Line id="OPR:Line:2" version="1">
  <Name>Regionbuss 2</Name>
  <TransportMode>bus</TransportMode>
  <!-- Different orgs per role -->
  <AuthorityRef ref="REG:Organisation:Fylkeskommune"/>
  <OperatorRef ref="REG:Organisation:PrivatBuss"/>
</Line>
```

---

## 6. ⚠️ Considerations

### For Data Producers

| Concern | Guidance |
|---------|----------|
| **ID format** | Use the registry's codespace consistently (`REG:Organisation:xxx`) |
| **No inline objects needed** | The delivery does not need to re-define organisations from the registry |
| **Element = role** | `AuthorityRef` means "this org acts as authority here", `OperatorRef` means "this org operates here" |
| **SIRI compatibility** | SIRI-ET and SIRI-VM use `OperatorRef` — the same registry ID works |

### For Data Consumers

| Concern | Guidance |
|---------|----------|
| **Resolving refs** | Look up the organisation in the central registry, not in the NeTEx file |
| **Building full NeTEx** | If you need to produce a complete document with inline objects, you must choose one NeTEx type per organisation per `<organisations>` block |
| **Same ID, different roles** | Do not assume `AuthorityRef="X"` and `OperatorRef="X"` are errors — they indicate dual-role |

### For Registry Operators

| Concern | Guidance |
|---------|----------|
| **Stable IDs** | Organisation IDs must be stable — they are cached in timetable datasets across systems |
| **Role-neutral** | The registry does not need to distinguish Authority from Operator — NeTEx context handles that |
| **Codespace** | Assign a dedicated codespace (e.g. `REG`) for registry-managed identifiers |

---

## 7. 🔗 Related Resources

### Guides in This Repository
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) — Authority, Operator, Contract, and ResponsibilitySet (inline model)
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — Data ownership and cross-frame patterns
- [IT Architecture](../ITArchitecture/ITArchitecture_Guide.md) — Data exchange architecture and actor roles
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — ID formatting rules and codespace patterns
- [MaaS Consumers](../MaaSConsumers/MaaSConsumers_Guide.md) — Consumer perspective on resolving references
