## Structure Overview

```text
FareZone
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 └─ members (0..1)
    └─ ScheduledStopPointRef/@ref (0..n)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the fare zone | FareZone/@id |
| @version | String | 1..1 | Version label | FareZone/@version |
| Name | String | 0..1 | Human-readable zone name | FareZone/Name |
| Description | String | 0..1 | Optional description of the zone's scope | FareZone/Description |
| members | Container | 0..1 | Collection of stop points in this zone | FareZone/members |
| [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)/@ref | ScheduledStopPointRef | 0..n | Reference to a stop point belonging to this zone | FareZone/members/ScheduledStopPointRef/@ref |
