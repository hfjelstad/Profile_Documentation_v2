## Structure Overview

```text
Block (TrainBlock)
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ Description (0..1)
 ├─ OperatorRef/@ref (0..1)
 └─ journeys (0..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the TrainBlock | Block/@id |
| @version | String | 1..1 | Version label | Block/@version |
| Name | String | 0..1 | Human-readable label | Block/Name |
| Description | String | 0..1 | Free-text description of the block | Block/Description |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | 0..1 | Reference to the operating organisation | Block/OperatorRef/@ref |
| journeys | Container | 0..1 | Container for VehicleJourneyRef elements linking journeys to this block | Block/journeys |
