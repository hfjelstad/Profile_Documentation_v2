# 🚌 Journey Lifecycle — From Line to Departure

## 1. 🎯 Introduction

The journey lifecycle is the core workflow of NeTEx — it describes how a public transport service goes from an abstract line definition all the way to a concrete departure on a specific date. Understanding this chain is essential: every timetable you publish follows it.

In this guide you will learn:
- 🔗 The five-object chain: Line → Route → JourneyPattern → ServiceJourney → DatedServiceJourney
- 📐 What each object owns and what it references
- 📅 How DayType and OperatingDay control when journeys run
- 📝 A complete worked example building the chain step by step

---

## 2. 🔗 The Chain

```text
Line           "Bus 100"              What passengers see
  │
  v
Route          "100 Outbound"         The geographic path (ordered stops)
  │
  v
JourneyPattern "100 Full Run"         Which stops are served + boarding rules
  │
  v
ServiceJourney "100 dep. 07:30"       The template: times, operator, day types
  │
  v
DatedServiceJourney "100 on 18 Mar"   The concrete instance on a specific date
```

Each level adds specificity:

| Object | Lives in | Adds |
|--------|----------|------|
| **Line** | ServiceFrame | Operator, transport mode, visual identity |
| **Route** | ServiceFrame | Ordered stop sequence, direction |
| **JourneyPattern** | ServiceFrame | Stop variants, boarding/alighting rules, destination display |
| **ServiceJourney** | TimetableFrame | Passing times, day types, operator override |
| **DatedServiceJourney** | TimetableFrame | Specific date, alterations, block assignment |

> 💡 **Tip:** Think of it as progressive refinement. Line says *what* runs. Route says *where*. JourneyPattern says *which stops*. ServiceJourney says *when*. DatedServiceJourney says *on which specific day*.

---

## 3. 📐 Step by Step

### Step 1 — Define the Line

The Line is the passenger-facing identity. It references the Operator (from the [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) guide).

```xml
<Line id="ERP:Line:100" version="1">
  <Name>Bus 100</Name>
  <TransportMode>bus</TransportMode>
  <PublicCode>100</PublicCode>
  <OperatorRef ref="ERP:Operator:Unibuss"/>
</Line>
```

### Step 2 — Define the Route

The Route describes the geographic path as an ordered sequence of ScheduledStopPoints. It references the Line.

```xml
<Route id="ERP:Route:100_Out" version="1">
  <Name>100 Drammen - Asker - Oslo</Name>
  <LineRef ref="ERP:Line:100"/>
  <DirectionType>outbound</DirectionType>
  <pointsInSequence>
    <PointOnRoute id="ERP:PointOnRoute:100_Out_1" version="1" order="1">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Drammen"/>
    </PointOnRoute>
    <PointOnRoute id="ERP:PointOnRoute:100_Out_2" version="1" order="2">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Asker"/>
    </PointOnRoute>
    <PointOnRoute id="ERP:PointOnRoute:100_Out_3" version="1" order="3">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:OsloS"/>
    </PointOnRoute>
  </pointsInSequence>
</Route>
```

### Step 3 — Define the Journey Pattern

The JourneyPattern is an operational variant of the Route. It specifies which stops are served and adds boarding/alighting rules and destination displays.

```xml
<JourneyPattern id="ERP:JourneyPattern:100_Out_Full" version="1">
  <Name>100 Full Run Outbound</Name>
  <RouteRef ref="ERP:Route:100_Out"/>
  <pointsInSequence>
    <StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:100_1" version="1" order="1">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Drammen"/>
      <ForAlighting>false</ForAlighting>
      <ForBoarding>true</ForBoarding>
      <DestinationDisplayRef ref="ERP:DestinationDisplay:OsloS"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:100_2" version="1" order="2">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:Asker"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:StopPointInJourneyPattern:100_3" version="1" order="3">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:OsloS"/>
      <ForAlighting>true</ForAlighting>
      <ForBoarding>false</ForBoarding>
    </StopPointInJourneyPattern>
  </pointsInSequence>
</JourneyPattern>
```

> 💡 **Tip:** Multiple JourneyPatterns can reference the same Route. A "short run" pattern might skip the last stop, while the "full run" serves all of them.

### Step 4 — Define the ServiceJourney

The ServiceJourney adds the schedule: passing times and the days it operates.

```xml
<ServiceJourney id="ERP:ServiceJourney:100_0730" version="1">
  <Name>Bus 100 dep. 07:30</Name>
  <JourneyPatternRef ref="ERP:JourneyPattern:100_Out_Full"/>
  <OperatorRef ref="ERP:Operator:Unibuss"/>
  <dayTypes>
    <DayTypeRef ref="ERP:DayType:Weekdays"/>
  </dayTypes>
  <passingTimes>
    <TimetabledPassingTime>
      <StopPointInJourneyPatternRef ref="ERP:StopPointInJourneyPattern:100_1"/>
      <DepartureTime>07:30:00</DepartureTime>
    </TimetabledPassingTime>
    <TimetabledPassingTime>
      <StopPointInJourneyPatternRef ref="ERP:StopPointInJourneyPattern:100_2"/>
      <ArrivalTime>07:55:00</ArrivalTime>
      <DepartureTime>07:56:00</DepartureTime>
    </TimetabledPassingTime>
    <TimetabledPassingTime>
      <StopPointInJourneyPatternRef ref="ERP:StopPointInJourneyPattern:100_3"/>
      <ArrivalTime>08:25:00</ArrivalTime>
    </TimetabledPassingTime>
  </passingTimes>
</ServiceJourney>
```

### Step 5 — (Optional) Date it

For date-specific operations — reinforcements, cancellations, or block assignment — create a DatedServiceJourney:

```xml
<DatedServiceJourney id="ERP:DatedServiceJourney:100_0730_20260318" version="1">
  <ServiceJourneyRef ref="ERP:ServiceJourney:100_0730"/>
  <OperatingDayRef ref="ERP:OperatingDay:2026-03-18"/>
  <ServiceAlteration>planned</ServiceAlteration>
</DatedServiceJourney>
```

---

## 4. 📅 Calendar: DayType vs OperatingDay

Two different mechanisms control *when* journeys run:

| Mechanism | Object | Used by | Example |
|-----------|--------|---------|---------|
| **Pattern-based** | DayType | ServiceJourney | "Weekdays", "Saturdays" |
| **Date-based** | OperatingDay | DatedServiceJourney | "2026-03-18" |

**DayType** defines a recurring pattern (e.g., "Weekdays"). It needs a **DayTypeAssignment** to bind it to actual calendar dates via an **OperatingPeriod**. Without this binding, ServiceJourneys referencing the DayType will have no operating days.

**OperatingDay** defines a single calendar date. It is referenced by **DatedServiceJourney** for date-specific operations: cancellations, replacements, reinforcements, and block assignments.

> 📖 **Full coverage:** The [Calendar Guide](../Calendar/Calendar_Guide.md) covers all four calendar objects in depth — including the `isAvailable=false` exception pattern for holidays, a decision flowchart, and worked XML examples.

---

## 5. ✅ Best Practices

1. **Follow the chain.** Every ServiceJourney must reference a JourneyPattern, which must reference a Route, which must reference a Line. Skipping a level creates orphaned data.

2. **Don't duplicate stop sequences.** Route defines the geographic path; JourneyPattern defines variants. Don't repeat the same stops in both — JourneyPattern references the Route via `RouteRef`.

3. **Passing times belong to ServiceJourney only.** JourneyPattern defines *which stops* are served; ServiceJourney defines *when* they are served. Don't put ArrivalTime/DepartureTime on JourneyPattern.

4. **Use DayType for recurring schedules, DatedServiceJourney for exceptions.** DayType handles "every weekday"; DatedServiceJourney handles "cancelled on 18 March".

5. **First stop: DepartureTime only. Last stop: ArrivalTime only.** The first stop has no arrival (journey starts there); the last has no departure (journey ends there).

6. **Keep @order sequential** in both Route (`PointOnRoute`) and JourneyPattern (`StopPointInJourneyPattern`). Start at 1, increment by 1, no gaps.

---

## 6. ❌ Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|-------------|-----|
| ServiceJourney without JourneyPatternRef | No stop sequence defined | Always reference a JourneyPattern |
| JourneyPattern without RouteRef | No geographic path context | Always reference a Route |
| Route without LineRef | Orphaned route | Always reference a Line |
| Stop times on JourneyPattern | Wrong object | Move passing times to ServiceJourney |
| DayType without DayTypeAssignment | No operating dates resolved | Create a DayTypeAssignment in ServiceCalendarFrame |
| Confusing DayType with OperatingDay | Different mechanisms | DayType = pattern; OperatingDay = specific date |
| @order gaps (1, 3, 5) | Breaks sequence parsing | Use sequential 1, 2, 3 |

---

## 7. 📄 Full Example

> 📄 **Full example:** [Example_JourneyLifecycle.xml](Example_JourneyLifecycle.xml) — Complete PublicationDelivery building the chain from Line through to DatedServiceJourney.

---

## 8. 🔗 Related Resources

### Guides
- [Calendar](../Calendar/Calendar_Guide.md) -- DayType, OperatingPeriod, DayTypeAssignment, OperatingDay — when services operate
- [Organisational Governance](../OrganisationalGovernance/OrganisationalGovernance_Guide.md) -- Authority and Operator (required before defining Lines)
- [Stop Infrastructure](../StopInfrastructure/StopInfrastructure_Guide.md) -- ScheduledStopPoint and physical stop mapping
- [Interchange](../InterchangeOnly/Interchange_Guide.md) -- Planned transfers between ServiceJourneys
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) -- Domain separation strategies

### Frames & Objects
- [ServiceFrame](../../Frames/ServiceFrame/Table_ServiceFrame.md) -- Line, Route, JourneyPattern, ScheduledStopPoint
- [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md) -- ServiceJourney, DatedServiceJourney
- [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Table_ServiceCalendarFrame.md) -- DayType, DayTypeAssignment
- [Line](../../Objects/Line/Table_Line.md) | [Route](../../Objects/Route/Table_Route.md) | [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) | [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) | [DatedServiceJourney](../../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) | [DayType](../../Objects/DayType/Table_DayType.md)

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) -- Official specification
