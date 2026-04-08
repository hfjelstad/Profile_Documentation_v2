## Structure Overview

```text
DayType
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 └─ properties (0..1)
    └─ PropertyOfDay (0..n)
       └─ DaysOfWeek (0..1)
```

## Table

| Element | Type | XSD | ERP | NP | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the DayType | DayType/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | DayType/@version |
| Name | String | 0..1 | 1..1 |  | Human-readable name of the day classification | DayType/Name |
| Description | String | 0..1 |  |  | Additional description of the DayType | DayType/Description |
| PropertyOfDay | Element | 0..n |  | 0..n | Operational characteristic of the day type | DayType/properties/PropertyOfDay |
| DaysOfWeek | String | 0..1 |  | 0..1 | Space-separated list of day names (Monday Tuesday Wednesday Thursday Friday Saturday Sunday) | DayType/properties/PropertyOfDay/DaysOfWeek |
