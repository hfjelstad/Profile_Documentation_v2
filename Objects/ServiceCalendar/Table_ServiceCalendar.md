## Structure Overview

```text
ServiceCalendar
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ FromDate (1..1)
 ├─ ToDate (1..1)
 ├─ dayTypes (0..1)
 │  └─ DayType (0..n)
 ├─ operatingDays (0..1)
 │  └─ OperatingDay (0..n)
 ├─ operatingPeriods (0..1)
 │  └─ OperatingPeriod (0..n)
 └─ dayTypeAssignments (0..1)
    └─ DayTypeAssignment (0..n)
```

---

## Table

| Element | Type | FR | Description | Path |
|---------|------|-----|-------------|------|
| **@id** | ID | 1..1 | Unique identifier for the service calendar | @id |
| **@version** | xsd:string | 1..1 | Version of this service calendar instance | @version |
| Name | xsd:string | 0..1 | Human-readable name for the calendar period | Name |
| **FromDate** | xsd:dateTime | 1..1 | Start date of the calendar validity period | FromDate |
| **ToDate** | xsd:dateTime | 1..1 | End date of the calendar validity period | ToDate |
| dayTypes | | 0..1 | Container for inline DayType definitions | dayTypes |
| DayType | DayType | 0..n | A day classification (see [DayType](../DayType/Table_DayType.md)) | dayTypes/DayType |
| operatingDays | | | Container for inline OperatingDay definitions | operatingDays |
| OperatingDay | OperatingDay | | An individual calendar date (see [OperatingDay](../OperatingDay/Table_OperatingDay.md)) | operatingDays/OperatingDay |
| operatingPeriods | | 0..1 | Container for inline OperatingPeriod definitions | operatingPeriods |
| OperatingPeriod | OperatingPeriod | 0..n | A date range (see [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md)) | operatingPeriods/OperatingPeriod |
| dayTypeAssignments | | 0..1 | Container for inline DayTypeAssignment bindings | dayTypeAssignments |
| DayTypeAssignment | DayTypeAssignment | 0..n | Binding between DayType and date/period (see [DayTypeAssignment](../DayTypeAssignment/Table_DayTypeAssignment.md)) | dayTypeAssignments/DayTypeAssignment |

### Notes

- **Bold** elements are mandatory.
- The inline collections (dayTypes, operatingDays, etc.) contain the same objects documented under their respective Object pages.
- For frame-level usage, see [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Table_ServiceCalendarFrame.md).
