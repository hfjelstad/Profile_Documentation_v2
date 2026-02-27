| Element | Path | Type / Values | Card. | Notes |
|---|---|---|---|---|
| ServiceCalendarFrame.id | /CompositeFrame/frames/ServiceCalendarFrame/@id | Identifier (ERP codespace) | 1 | Example: ERP:ServiceCalendarFrame:1 |
| ServiceCalendarFrame.version | @version | String | 1 | Profile uses simple numeric versions |
| dayTypes | ServiceCalendarFrame/dayTypes | Container | 0..1 | Holds DayType elements |
| DayType.id | dayTypes/DayType/@id | Identifier (ERP) | 1 | Example: ERP:DayType:WKD |
| DayType.version | @version | String | 1 |  |
| Name | DayType/Name | xs:string | 0..1 | Human-readable label (English preferred) |
| properties | DayType/properties | Container | 0..1 |  |
| PropertyOfDay | properties/PropertyOfDay | Element | 0..* |  |
| DaysOfWeek | PropertyOfDay/DaysOfWeek | Enumeration list | 1 | One or more of: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Weekdays, Weekend, Everyday, none. No alias values like MondayToFriday |
| operatingPeriods | ServiceCalendarFrame/operatingPeriods | Container | 0..1 | Holds OperatingPeriod elements |
| OperatingPeriod.id | operatingPeriods/OperatingPeriod/@id | Identifier (ERP) | 1 | Example: ERP:OperatingPeriod:2026H1 |
| OperatingPeriod.version | @version | String | 1 |  |
| FromDate | OperatingPeriod/FromDate | xs:dateTime | 1 | Must include time and timezone, e.g., 2026-01-01T00:00:00Z |
| ToDate | OperatingPeriod/ToDate | xs:dateTime | 0..1 | Optional end boundary |
| dayTypeAssignments | ServiceCalendarFrame/dayTypeAssignments | Container | 0..1 | Holds DayTypeAssignment elements |
| DayTypeAssignment.id | dayTypeAssignments/DayTypeAssignment/@id | Identifier (ERP) | 1 | Example: ERP:DTA:WKD_2026H1 |
| DayTypeAssignment.version | @version | String | 1 |  |
| DayTypeRef | DayTypeAssignment/DayTypeRef/@ref | IdentifierRef | 1 | Must resolve to DayType in this dataset |
| OperatingPeriodRef | DayTypeAssignment/OperatingPeriodRef/@ref | IdentifierRef | 0..1 | Alternative: OperatingDayRef |
| OperatingDayRef | DayTypeAssignment/OperatingDayRef/@ref | IdentifierRef | 0..1 | Alternative: OperatingPeriodRef |
| isAvailable | DayTypeAssignment/isAvailable | xs:boolean | 1 | true when services run; false for exceptions |
