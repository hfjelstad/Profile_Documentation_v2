## Structure Overview

```text
DayTypeAssignment
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ @order (1..1)
 ├─ OperatingPeriodRef/@ref (0..1)
 ├─ Date (0..1)
 ├─ DayTypeRef/@ref (1..1)
 └─ isAvailable (1..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the assignment | DayTypeAssignment/@id |
| @version | String | 1..1 | Version label | DayTypeAssignment/@version |
| @order | xsd:integer | 1..1 | Evaluation precedence — higher order overrides lower for the same DayType | DayTypeAssignment/@order |
| [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md)/@ref | OperatingPeriodRef | 0..1 | Reference to a date range. Mutually exclusive with Date | OperatingPeriodRef/@ref |
| Date | xsd:date | 0..1 | Specific date (YYYY-MM-DD). Mutually exclusive with OperatingPeriodRef | Date |
| [DayType](../DayType/Table_DayType.md)/@ref | DayTypeRef | 0..1 | Reference to the DayType being assigned | DayTypeRef/@ref |
| isAvailable | xsd:boolean | 0..1 | `true` = DayType is active; `false` = DayType is suppressed on this date/period | isAvailable |
