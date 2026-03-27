# ServiceCalendar

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#servicecalendar)*

## 1. Purpose

A **ServiceCalendar** is a self-contained container that bundles DayTypes, OperatingDays, OperatingPeriods, and DayTypeAssignments into a single reusable object. While these calendar elements can be placed individually in a ServiceCalendarFrame, the ServiceCalendar object wraps them together for convenient referencing — a TimetableFrame or individual ServiceJourney can reference a ServiceCalendar to inherit its entire calendar definition in one step.

The French profile uses ServiceCalendar as the primary container for all calendar data (placed inside a GeneralFrame with TypeOfFrame NETEX_CALENDRIER). The Nordic profile tends to use ServiceCalendarFrame directly. Both approaches are valid NeTEx.

## 2. Structure Overview

```text
📄 ServiceCalendar
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 FromDate (1..1)
  ├─ 📄 ToDate (1..1)
  ├─ 📁 dayTypes (0..1)
  │  └─ 📄 DayType (0..n)
  ├─ 📁 operatingDays (0..1)
  │  └─ 📄 OperatingDay (0..n)
  ├─ 📁 operatingPeriods (0..1)
  │  └─ 📄 OperatingPeriod (0..n)
  └─ 📁 dayTypeAssignments (0..1)
     └─ 📄 DayTypeAssignment (0..n)
```

## 3. Key Elements

- **FromDate / ToDate**: The overall validity period of this calendar. All contained OperatingPeriods and assignments should fall within this range.
- **dayTypes**: Inline collection of DayType definitions (e.g., Weekdays, Saturday, Holidays). These may also be listed separately in the frame; inline inclusion makes the ServiceCalendar self-contained.
- **operatingDays**: Inline collection of OperatingDay objects for individual calendar dates (used by DatedServiceJourney).
- **operatingPeriods**: Inline collection of OperatingPeriod date ranges referenced by DayTypeAssignments.
- **dayTypeAssignments**: The bindings that connect DayTypes to dates or OperatingPeriods.

## 4. References

- [DayType](../DayType/Table_DayType.md) – Day classifications contained in or referenced by this calendar
- [DayTypeAssignment](../DayTypeAssignment/Table_DayTypeAssignment.md) – Bindings between DayTypes and dates/periods
- [OperatingPeriod](../OperatingPeriod/Table_OperatingPeriod.md) – Date ranges used by assignments
- [OperatingDay](../OperatingDay/Table_OperatingDay.md) – Individual calendar dates

## 5. Usage Notes

### 5a. Consistency Rules

- ServiceCalendar can appear inside a ServiceCalendarFrame.
- All DayTypeAssignments inside the calendar should reference DayTypes that are either inline in the same calendar or resolvable from the broader dataset.
- FromDate/ToDate define the validity window but are not automatically enforced — assignments outside this range are not invalid, just semantically questionable.

### 5b. Validation Requirements

- **FromDate and ToDate are mandatory** — they define the calendar's validity period.
- **@id must follow codespace conventions** — e.g., `ENT:ServiceCalendar:2025`.

### 5c. Common Pitfalls

> [!WARNING]
> - **ServiceCalendar vs. ServiceCalendarFrame**: ServiceCalendar is a data object (like an Entity). ServiceCalendarFrame is a packaging frame. You can put a ServiceCalendar *inside* a ServiceCalendarFrame, or you can put DayTypes/Assignments directly in the frame without a ServiceCalendar wrapper. Both are valid.
> - **Duplicate calendar entities**: If you define DayTypes both inline in the ServiceCalendar and separately in the frame, ensure IDs are consistent — duplicate IDs with different content will cause validation errors.
> - **FromDate/ToDate mismatch**: If a DayTypeAssignment references an OperatingPeriod that extends beyond FromDate/ToDate, the ServiceCalendar's bounds don't automatically clip it.

## 6. Additional Information

See [Table_ServiceCalendar.md](Table_ServiceCalendar.md) for detailed attribute specifications.

Example XML: [Example_ServiceCalendar_FR.xml](Example_ServiceCalendar_FR.xml)

For the frame-level documentation, see [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Description_ServiceCalendarFrame.md).
