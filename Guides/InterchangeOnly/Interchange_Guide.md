# 🔄 Interchange & InterchangeOnly Guide

## 1. 🎯 Introduction

When passengers transfer between services — say from a bus to a train — the connection needs to be planned, communicated, and sometimes guaranteed. NeTEx models these transfers using **ServiceJourneyInterchange** and optionally marks stops that exist *only* for transferring with `StopUse = interchangeOnly`.

This guide explains when and how to model planned interchanges, with practical examples covering both minimal and full-featured configurations.

In this guide you will learn:
- 🔗 What a ServiceJourneyInterchange is and where it lives
- 🚏 How `StopUse = interchangeOnly` marks transfer-only stops
- ⏱️ How to add timing constraints and guarantees
- 📝 Practical XML examples from minimal to full

---

## 2. 🔗 Core Concepts

### What Is an Interchange?

An **interchange** is a planned transfer opportunity between two ServiceJourneys — a **feeder** (the arriving service) and a **distributor** (the departing service). It answers the question: *"Can a passenger get off journey A and onto journey B at this location?"*

```text
  Feeder journey                            Distributor journey
+--------------------+                    +--------------------+
| ServiceJourney A   |                    | ServiceJourney B   |
| (Bus line 100)     |                    | (Train RE 10)      |
+--------+-----------+                    +-----------+--------+
         |                                            |
         |  arrives at stop                departs from stop
         v                                            ^
    +----+--------------------------------------------+----+
    |                  Transfer stop                        |
    |            (e.g., Asker station)                      |
    +------------------------------------------------------+
```

### Key Properties

| Property | Type | Purpose |
|----------|------|---------|
| **FromJourneyRef** | Reference | The feeder journey passengers arrive on |
| **ToJourneyRef** | Reference | The distributor journey passengers transfer to |
| **FromPointRef** | Reference | The stop on the feeder journey (optional) |
| **ToPointRef** | Reference | The stop on the distributor journey (optional) |
| **Guaranteed** | Boolean | Whether the distributor waits for the feeder |
| **MaximumWaitTime** | Duration | How long the distributor will wait (e.g., `PT10M`) |
| **MinimumTransferTime** | Duration | Minimum time needed for a safe transfer (e.g., `PT5M`) |
| **StaySeated** | Boolean | Whether passengers can remain seated (through-running) |

> 💡 **Tip:** An interchange is **one-directional** (From → To). For bidirectional transfers, create two separate ServiceJourneyInterchange elements.

### Where Does It Live?

ServiceJourneyInterchange elements are placed in the **TimetableFrame** under the `journeyInterchanges` collection:

```text
TimetableFrame
 ├─ vehicleJourneys
 │   ├─ ServiceJourney (feeder)
 │   └─ ServiceJourney (distributor)
 └─ journeyInterchanges
     └─ ServiceJourneyInterchange
```

---

## 3. 🚏 StopUse = interchangeOnly

Sometimes a stop on a journey exists solely for transfer purposes — passengers are not expected to board or alight there for its own sake. NeTEx models this with the `StopUse` element on `StopPointInJourneyPattern`:

```xml
<StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:2" version="1" order="2">
  <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Asker"/>
  <ForAlighting>true</ForAlighting>
  <ForBoarding>false</ForBoarding>
  <StopUse>interchangeOnly</StopUse>
</StopPointInJourneyPattern>
```

### When to Use interchangeOnly

| Scenario | Use interchangeOnly? |
|----------|---------------------|
| Bus terminates at a rail station purely for train connections | Yes |
| Express train stops only to enable transfers to local services | Yes |
| Regular stop where passengers also board/alight normally | No |
| Hub station with many connections but also local demand | No |

> ⚠️ **Note:** `StopUse` is a property of the stop *within a specific journey pattern*, not of the stop itself. The same ScheduledStopPoint can be `interchangeOnly` on one journey and a regular stop on another.

---

## 4. 📝 Practical Examples

### 4a. Minimal Interchange (MIN profile)

The simplest valid interchange — just two journey references:

```xml
<TimetableFrame id="ERP:TimetableFrame:1" version="1">
  <vehicleJourneys>
    <ServiceJourney id="ERP:ServiceJourney:Bus_100" version="1">
      <Name>Bus 100 Drammen - Asker</Name>
    </ServiceJourney>
    <ServiceJourney id="ERP:ServiceJourney:RE_10" version="1">
      <Name>RE 10 Asker - Oslo</Name>
    </ServiceJourney>
  </vehicleJourneys>
  <journeyInterchanges>
    <!-- Minimal: only the two mandatory journey references -->
    <ServiceJourneyInterchange id="ERP:ServiceJourneyInterchange:Bus100_to_RE10" version="1">
      <FromJourneyRef ref="ERP:ServiceJourney:Bus_100"/>
      <ToJourneyRef ref="ERP:ServiceJourney:RE_10"/>
    </ServiceJourneyInterchange>
  </journeyInterchanges>
</TimetableFrame>
```

> 📄 **Full example:** [Example_Interchange_ERP.xml](../../Objects/Interchange/Example_Interchange_ERP.xml)

### 4b. Guaranteed Interchange with Timing (NP profile)

A guaranteed connection with stop references and timing constraints:

```xml
<TimetableFrame id="NP:TimetableFrame:ic:1" version="1">
  <journeyInterchanges>
    <ServiceJourneyInterchange id="NP:ServiceJourneyInterchange:1330756_1_1" version="1">
      <!-- Guarantee: the train waits for the bus -->
      <Guaranteed>true</Guaranteed>
      <MaximumWaitTime>PT10M</MaximumWaitTime>
      <MinimumTransferTime>PT3M</MinimumTransferTime>

      <!-- Stop references: where the transfer happens -->
      <FromPointRef ref="NP:ScheduledStopPoint:9060006_1"/>
      <ToPointRef ref="NP:ScheduledStopPoint:9060006_1"/>

      <!-- Journey references: feeder and distributor -->
      <FromJourneyRef ref="NP:ServiceJourney:15044_371"/>
      <ToJourneyRef ref="NP:ServiceJourney:15045_372"/>
    </ServiceJourneyInterchange>
  </journeyInterchanges>
</TimetableFrame>
```

> 📄 **Full example:** [Example_Interchange_NP.xml](../../Objects/Interchange/Example_Interchange_NP.xml)

### 4c. Interchange with interchangeOnly Stop

Combining the interchange with a transfer-only stop in the journey pattern:

```xml
<!-- Journey pattern: the bus stops at Asker only for transfers -->
<JourneyPattern id="ERP:JourneyPattern:Bus_Drammen_Asker" version="1">
  <pointsInSequence>
    <StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:1" version="1" order="1">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Drammen"/>
      <ForAlighting>false</ForAlighting>
      <ForBoarding>true</ForBoarding>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:2" version="1" order="2">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Asker"/>
      <ForAlighting>true</ForAlighting>
      <ForBoarding>false</ForBoarding>
      <!-- This stop exists only for the transfer to the train -->
      <StopUse>interchangeOnly</StopUse>
    </StopPointInJourneyPattern>
  </pointsInSequence>
</JourneyPattern>

<!-- The interchange linking the two journeys at Asker -->
<ServiceJourneyInterchange id="ERP:ServiceJourneyInterchange:Bus100_to_RE10" version="1">
  <Guaranteed>true</Guaranteed>
  <MaximumWaitTime>PT10M</MaximumWaitTime>
  <FromPointRef ref="ERP:ScheduledStopPoint:Asker"/>
  <ToPointRef ref="ERP:ScheduledStopPoint:Asker"/>
  <FromJourneyRef ref="ERP:ServiceJourney:Bus_100"/>
  <ToJourneyRef ref="ERP:ServiceJourney:RE_10"/>
</ServiceJourneyInterchange>
```

> 📄 **Full example:** [Example_Interchange.xml](Example_Interchange.xml) — A complete PublicationDelivery with stop points, journey patterns (including `interchangeOnly`), ServiceJourneys, and both guaranteed and non-guaranteed interchanges.

---

## 5. ✅ Best Practices

1. **Use `ServiceJourneyInterchange`**, not `Interchange`, as the XML element name. The schema expects the full name.

2. **Always set `Guaranteed` and `MaximumWaitTime` together.** A guaranteed interchange without a wait limit leaves operations undefined.

3. **Include `FromPointRef` / `ToPointRef`** when the feeder or distributor serves multiple stops — it removes ambiguity about *where* the transfer happens.

4. **One interchange = one direction.** For round-trip connections (A→B and B→A), create two separate elements.

5. **Use `interchangeOnly` sparingly.** It signals to journey planners and passengers that a stop has no standalone value on this journey — only apply it when that is genuinely the case.

6. **Place interchanges in the same TimetableFrame** as the journeys they reference, or in a shared TimetableFrame within the same CompositeFrame.

7. **Use ISO 8601 durations** for all time properties — `PT5M` (5 minutes), `PT1H` (1 hour), not raw numbers.

---

## 6. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| `<Interchange id="...">` | Wrong element name | Use `<ServiceJourneyInterchange>` |
| Missing `FromJourneyRef` or `ToJourneyRef` | Both are mandatory | Always provide both references |
| `Guaranteed = true` without `MaximumWaitTime` | Operationally undefined | Add `<MaximumWaitTime>PT10M</MaximumWaitTime>` |
| Setting `StopUse` on ScheduledStopPoint | StopUse belongs on StopPointInJourneyPattern | Move it to the journey pattern level |
| Same interchange for both directions | Each interchange is unidirectional | Create two separate elements |

---

## 7. 🔗 Related Resources

### Guides
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) -- Domain separation and coupling strategies
- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) -- ID format, casing, and element ordering rules

### Frames & Objects
- [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md) -- Where interchanges are placed
- [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) -- The feeder and distributor journeys
- [Interchange](../../Objects/Interchange/Table_Interchange.md) -- Attribute specification table
- [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) -- Contains StopPointInJourneyPattern
- [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) -- The transfer location

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification
