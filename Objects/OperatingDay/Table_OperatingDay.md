## Structure Overview

```text
OperatingDay
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ CalendarDate (1..1)
 ├─ Name
 └─ EarliestTime
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the OperatingDay | OperatingDay/@id |
| @version | String | 1..1 | Version label | OperatingDay/@version |
| CalendarDate | xsd:date | 1..1 | The specific calendar date (YYYY-MM-DD) | OperatingDay/CalendarDate |
| Name | String | 0..1 | Optional human-readable label for the day | OperatingDay/Name |
| EarliestTime | xsd:time | 0..1 | Earliest departure time when service day spans past midnight | OperatingDay/EarliestTime |
