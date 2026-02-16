# Guide: Modeling Mandatory Interchanges in NeTEx

## 1. Core Elements
To model a **mandatory interchange** (e.g., bus replacement for part of a train route), the following NeTEx elements are essential:

- **ServiceJourney**: Represents an actual vehicle journey (e.g., Bus Drammen → Asker, Train Asker → Oslo Lufthavn).
- **ServiceJourneyPattern**: Defines the sequence of stops for a ServiceJourney.
- **StopPointInJourneyPattern**: Each stop in the pattern; can include restrictions.
- **Interchange**: Represents a planned connection between two journeys.
- **StopUse = interchangeOnly**: Indicates that a stop is only for interchange, not for regular boarding/alighting.
- **Boarding/Alighting flags**: `forBoarding` and `forAlighting` can restrict boarding or alighting at specific stops.

---

## 2. When to Use Interchange + StopUse vs. AccessRightAssignment
- **Interchange + StopUse**: Recommended for most cases. It clearly models a planned, guaranteed connection and restricts stop usage to interchange only.
- **AccessRightAssignment**: Use only if you need to enforce complex access rules (e.g., only passengers with a specific fare product). This adds complexity and is rarely needed for simple mandatory interchanges.

---

## 3. XML Examples

### 3.1 Bus → Train (Mandatory Interchange at Asker)
```xml
<ServiceJourneyPattern id="ERP:SJP:Bus_Drammen_Asker">
  <StopPointsInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPJP:1" order="1">
      <ScheduledStopPointRef ref="ERP:SSP:Drammen"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPJP:2" order="2">
      <ScheduledStopPointRef ref="ERP:SSP:Asker"/>
      <StopUse>interchangeOnly</StopUse>
    </StopPointInJourneyPattern>
  </StopPointsInJourneyPattern>
</ServiceJourneyPattern>

<Interchange id="ERP:IC:BusToTrain_Asker">
  <FromJourneyRef ref="ERP:SJ:Bus_1"/>
  <ToJourneyRef ref="ERP:SJ:Train_1"/>
  <Planned>true</Planned>
  <Guaranteed>true</Guaranteed>
</Interchange>
```

### 3.2 Train → Bus (Mandatory Interchange at Asker)
```xml
<ServiceJourneyPattern id="ERP:SJP:Train_Drammen_Asker">
  <StopPointsInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPJP:1" order="1">
      <ScheduledStopPointRef ref="ERP:SSP:Drammen"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPJP:2" order="2">
      <ScheduledStopPointRef ref="ERP:SSP:Asker"/>
      <StopUse>interchangeOnly</StopUse>
    </StopPointInJourneyPattern>
  </StopPointsInJourneyPattern>
</ServiceJourneyPattern>

<Interchange id="ERP:IC:TrainToBus_Asker">
  <FromJourneyRef ref="ERP:SJ:Train_123"/>
  <ToJourneyRef ref="ERP:SJ:Bus_456"/>
  <Planned>true</Planned>
  <Guaranteed>true</Guaranteed>
</Interchange>
```

---

## 4. Best Practices and Recommendations
- Use **Interchange** to explicitly model planned and guaranteed connections.
- Apply **StopUse = interchangeOnly** on stops that should not allow regular boarding/alighting.
- Avoid unnecessary complexity: do not introduce AccessRightAssignment unless required for fare or entitlement logic.
- If normal boarding is allowed in one direction, do not set StopUse on that stop; instead, use boarding/alighting flags where needed.
- Keep the model semantically clear: Interchange + StopUse is usually sufficient for mandatory transfers.

---

**Summary:** For mandatory interchanges, the simplest and most robust approach is to use **Interchange** combined with **StopUse = interchangeOnly** on the relevant stop points. This ensures clarity for journey planners and operational systems.