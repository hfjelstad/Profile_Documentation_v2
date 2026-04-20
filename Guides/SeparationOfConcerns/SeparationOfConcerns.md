# 🧩 Separation of Concerns

## 1. 🎯 Introduction

Public transport data spans multiple domains — from passenger-facing timetables to vehicle operations to railway infrastructure planning. When these domains are tightly coupled, a change in one area forces cascading changes in others: updating a vehicle allocation should not require republishing the passenger timetable, and vice versa.

**Separation of concerns** is the practice of structuring NeTEx data so that each domain owns its data independently, with well-defined coupling points between them.

In this guide you will learn:
- 🏗️ The three domains of public transport data and how they map to NeTEx frames
- 🔗 Three coupling strategies — from simple direct references to fully decoupled links
- ⚖️ How to choose the right level of separation for your use case
- 📝 Practical NeTEx XML examples for each approach

---

## 2. 🏗️ The Three Domains

Public transport data naturally separates into three concerns, each with a distinct focus and audience:

```text
+---------------------+    +---------------------+    +---------------------+
| INFRASTRUCTURE      |    | VEHICLE OPERATIONS  |    | TRAVELER            |
|                     |    |                     |    | INFORMATION         |
| Planning traffic    |    | Describing the      |    | Describing the      |
| flow to ensure      |    | vehicles needed to  |    | travel opportunity  |
| optimal use of      |    | perform journeys    |    | for passengers      |
| railway infra.      |    | and dead runs       |    |                     |
|---------------------|    |---------------------|    |---------------------|
| Train paths/slots   |    | Block, TrainBlock   |    | ServiceJourney      |
| Infrastructure      |    | TrainPart, Vehicle  |    | JourneyPattern      |
| manager allocation  |    | VehicleSchedule     |    | Line, Route         |
|                     |    | DeadRun             |    | ScheduledStopPoint  |
+---------------------+    +---------------------+    +---------------------+
```

### Domain → Frame Mapping

| Domain | NeTEx Frame | Key Objects | Owner |
|--------|-------------|-------------|-------|
| 🧳 Traveler | [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md), [ServiceFrame](../../Frames/ServiceFrame/Table_ServiceFrame.md) | ServiceJourney, JourneyPattern, Line, Route, ScheduledStopPoint, DestinationDisplay | Timetable planners |
| 🚌 Vehicle Operations | [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) | Block, TrainBlock, TrainPart, Vehicle, DeadRun | Operations planners |
| 🚉 Infrastructure | *(not yet standardized)* | Train path/slot, track sections | Infrastructure manager |

> 💡 **Tip:** The [ResourceFrame](../../Frames/ResourceFrame/Table_ResourceFrame.md) provides shared resources (Operator, Authority, VehicleType) used by all three domains. It acts as a common foundation, not a domain itself.

---

## 3. 🔗 Coupling Strategies

The PDF reference material defines three strategies for linking objects across domains. Each offers a different balance of simplicity vs. independence:

### 3a. Weak Separation — Direct Reference

The simplest approach: one object directly references another.

```text
+---------------+         +---------------+
|   Object A    |-------->|   Object B    |
|               |  @ref   |               |
+---------------+         +---------------+
```

| | |
|---|---|
| ✅ **Pros** | Easy to understand; clear and direct; low complexity |
| ❌ **Cons** | Object A or B must change when the relationship changes; creates coupling between domains |

**NeTEx example — Block directly references ServiceJourney:**

```xml
<!-- Vehicle operations domain directly references the traveler domain -->
<Block id="ERP:Block:TB_601" version="1">
  <Name>Block for IC 601</Name>
  <journeys>
    <VehicleJourneyRef ref="ERP:ServiceJourney:SJ_001"/>  <!-- direct coupling -->
  </journeys>
</Block>
```

> This is the simplest approach: the Block in the vehicle domain references a ServiceJourney in the traveler domain. Easy to read, but if the ServiceJourney changes (e.g., splits into two), the Block must be updated immediately.

---

### 3b. Favoring Separation — Link Owned by One Side

An intermediate object (link) connects A and B, but the link is managed by one domain's system.

```text
+---------------+    +---------------+    +---------------+
|   Object A    |<---|  Objects Link |--->|   Object B    |
|               |    |  (owned by B) |    |               |
+---------------+    +---------------+    +---------------+
```

| | |
|---|---|
| ✅ **Pros** | Still readable for humans; Object A doesn't need to know about B |
| ❌ **Cons** | Favors the system that owns the link; B's system has extra responsibility |

**NeTEx example — DatedServiceJourney as coupling:**

```xml
<!-- DatedServiceJourney lives in TimetableFrame (traveler domain) -->
<!-- It links to the vehicle domain via BlockRef -->
<DatedServiceJourney id="ERP:DatedServiceJourney:DSJ_001" version="1">
  <BlockRef ref="ERP:Block:TB_601"/>                        <!-- vehicle domain -->
  <ServiceJourneyRef ref="ERP:ServiceJourney:SJ_001"/>     <!-- traveler domain -->
  <OperatingDayRef ref="ERP:OperatingDay:2026-03-12"/>
</DatedServiceJourney>
```

> ⚠️ **Note:** The object structure of DatedServiceJourney *could* support strong separation — it references both domains independently. However, because DSJ lives in **TimetableFrame**, the timetable system controls the coupling, indirectly **favoring the traveler domain**. Additionally, DSJ carries date-specific runtime data (real-time, cancellations, reinforcements), creating a risk of **semantic overload**.

---

### 3c. Strong Separation — Independent Link

The link object is fully independent — owned by neither A's nor B's system. Only the link needs to change when relationships shift.

```text
+---------------+    +---------------+    +---------------+
|   Object A    |<---|  Objects Link |--->|   Object B    |
|               |    | (independent) |    |               |
+---------------+    +---------------+    +---------------+
```

| | |
|---|---|
| ✅ **Pros** | Only the link changes when relationships change; easy to substitute objects on either side; maximum domain independence |
| ❌ **Cons** | Harder for humans to follow; requires managing a third object |

**NeTEx example — Independent association link:**

```xml
<!-- Independent link connecting traveler and vehicle domains -->
<!-- Neither ServiceJourney nor Block contains this reference -->
<ServiceBlockAssociation id="ERP:ServiceBlockAssociation:SJ1_TB601" version="1">
  <ServiceJourneyRef ref="ERP:ServiceJourney:SJ_001"/>     <!-- traveler domain -->
  <BlockRef ref="ERP:Block:TB_601"/>                        <!-- vehicle domain -->
  <ValidBetween>
    <FromDate>2026-03-01T00:00:00Z</FromDate>
    <ToDate>2026-12-14T00:00:00Z</ToDate>
  </ValidBetween>
</ServiceBlockAssociation>
```

---

### Strategy Comparison

| Aspect | 🔵 Weak | 🟡 Favoring | 🟢 Strong |
|--------|---------|-------------|-----------|
| **Complexity** | Low | Medium | High |
| **Domain independence** | Low | Medium | High |
| **Who changes on update?** | A or B | Link + B's system | Link only |
| **Best for** | Simple systems, public-facing hints | Medium complexity, one dominant system | Complex multi-stakeholder environments |
| **NeTEx pattern** | Direct `*Ref` | DatedServiceJourney with cross-refs | Independent association object |

---

## 4. 📐 The Three-Domain View in Practice

The full picture shows how **ObjectsLink** patterns connect all three domains while keeping them independent:

```text
   Infrastructure              Vehicle Operations           Traveler Information
+---------------------+    +---------------------+    +---------------------+
|                     |    |                     |    |                     |
|  Infrastructure     |    |  Vehicle journey    |    |  ServiceJourney     |
|  availability       |    |  (Block/TrainBlock) |    |                     |
|                     |    |                     |    |                     |
+--------+------------+    +------+------+-------+    +----------+----------+
         |                       |      |                        |
         |    +------------------+      +----------------+       |
         |    |                                          |       |
    +----v----v----+                                +----v-------v---+
    |              |                                |                |
    | Objects Link |                                |  Objects Link  |
    |              |                                |                |
    +--------------+                                +----------------+
  Infra <-> Vehicle link                         Vehicle <-> Traveler link
```

Each domain publishes its data in its own frame within a [CompositeFrame](../../Frames/CompositeFrame/Description_CompositeFrame.md). The link objects can live in the domain they serve or in a separate assignment frame, depending on the chosen separation level.

> 💡 **Tip:** For most implementations, **a mix of strategies** is appropriate. Use *weak separation* for simple passenger-facing hints (VehicleTypeRef) and *strong separation* for operational assignments between vehicle scheduling and timetable planning.

---

## 5. 🚆 Vehicle Operations Domain — Key Patterns

### Block and TrainBlock

The vehicle operations domain uses **Block** (or **TrainBlock** for rail) to represent the planned assignment of vehicles to journeys:

```xml
<VehicleScheduleFrame id="ERP:VehicleScheduleFrame:1" version="1">
  <blocks>
    <Block id="ERP:Block:TB_601" version="1">
      <Name>Block for IC 601</Name>
      <journeys>
        <VehicleJourneyRef ref="ERP:ServiceJourney:SJ_001"/>
      </journeys>
    </Block>
  </blocks>
</VehicleScheduleFrame>
```

### TrainParts with Identical Composition

Rail operations sometimes split a journey into multiple **TrainParts** even when the rolling stock composition is identical — for reasons like crew changes, regulatory segments, or different train numbers per section.

```xml
<TrainBlock id="ERP:TrainBlock:GA_601" version="1">
  <trainParts>
    <TrainPartRef ref="ERP:TrainPart:GA_601_1"/>  <!-- Oslo – Kongsberg -->
    <TrainPartRef ref="ERP:TrainPart:GA_601_2"/>  <!-- Kongsberg – Kristiansand -->
  </trainParts>
</TrainBlock>
```

**Can you merge them?** For passenger-facing displays, yes — if all of these hold:

| Check | Condition |
|-------|-----------|
| ✅ Same rolling stock | Identical materialComposition across segments |
| ✅ No splitting/merging | The train set stays together for the entire route |
| ✅ No segment-specific disruptions | No per-segment cancellations or delays |
| ✅ Same validity | Identical operating period and context |

If any condition fails, keep the TrainParts separate.

---

## 6. ✅ Best Practices

1. **Choose the right coupling level for your context.** Simple bus networks may need only weak separation. Multi-stakeholder rail environments benefit from strong separation.

2. **Keep the traveler domain clean.** ServiceJourney should describe the passenger opportunity — don't leak operational details (vehicle IDs, block assignments, crew schedules) into the timetable.

3. **Use VehicleTypeRef for passenger hints only.** It tells the passenger *what kind* of vehicle to expect, not *which specific vehicle* will run. Keep it optional.

4. **Version frames independently.** A vehicle schedule change should not force a timetable republish if passenger-visible data hasn't changed.

5. **Prefer DatedServiceJourney for date-specific operations** (cancellations, reinforcements, real-time updates) — not as a general-purpose coupling mechanism.

6. **Use independent link objects for complex integrations.** When multiple stakeholders manage different domains, an independent ServiceBlockAssociation (or similar) keeps each domain autonomous.

7. **If TrainPath/Slot is needed, model it separately.** Infrastructure capacity allocation is a different concern from vehicle scheduling — store path references as external references or in a dedicated frame.

---

## 7. 💭 Design Reflections

The PDF reference material captures several important design principles:

- **NeTEx should support different levels of separation.** Not all systems need the same complexity — a simple regional bus operator has different needs than a national rail operator with infrastructure management obligations.

- **NeTEx should not favor one concern over another.** The standard should allow both tight coupling (simple case) and loose coupling (complex case) without making either approach feel like a workaround.

- **SequenceOfJourneys vs. staySeated.** For modeling through-running services, `SequenceOfJourneys` appears to be a better model than `staySeated`, though it historically leans toward the vehicle-centric representation — potentially lowering the separation between vehicle planning and passenger travel opportunity.

---

## 8. 🔗 Related Resources

### Guides
- [CompositeFrame](../../Frames/CompositeFrame/Description_CompositeFrame.md) – How NeTEx frames organize data across domains
- [Get Started](../GetStarted/GetStarted_Guide.md) – Introduction to NeTEx basics

### Frames
- [CompositeFrame](../../Frames/CompositeFrame/Table_CompositeFrame.md) – Groups multiple frames into a single delivery
- [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md) – Traveler domain: journeys and timetables
- [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Table_VehicleScheduleFrame.md) – Vehicle domain: blocks and scheduling
- [ServiceFrame](../../Frames/ServiceFrame/Table_ServiceFrame.md) – Traveler domain: lines, routes, and patterns
- [ResourceFrame](../../Frames/ResourceFrame/Table_ResourceFrame.md) – Shared resources across domains

### Objects
- [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) – Planned journey in the traveler domain
- [DatedServiceJourney](../../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) – Date-specific journey instance
- [TrainBlock](../../Objects/TrainBlock/Table_TrainBlock.md) – Vehicle block assignment for rail
- [VehicleType](../../Objects/VehicleType/Table_VehicleType.md) – Vehicle classification for passenger hints

### Reference Material
- 📎 [Separation of Concerns — Summary of Principles](images/soc_page_1.png) (slide deck, stored in images/)
