# Mandatory Interchange Guide

This guide explains how to model mandatory interchanges in NeTEx using **Interchange** and **StopUse**.

## Key Principles
- Use **Interchange** to define a planned and guaranteed connection between two journeys.
- Use **StopUse = interchangeOnly** on the stop where the interchange occurs to indicate that the stop is only for transfers.

## Example
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

## When to Use
- When a stop should only be used for transfers between specific journeys.
- When you need to enforce a planned and guaranteed connection between two services.
