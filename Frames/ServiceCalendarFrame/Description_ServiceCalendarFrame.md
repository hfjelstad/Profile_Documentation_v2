# ServiceCalendarFrame

Purpose
ServiceCalendarFrame groups calendar definitions that describe when services operate. It provides reusable day patterns and assignments for a publication period. Typical content includes:
- DayTypes: reusable labels for day patterns (e.g., Weekdays, Weekend) with days of week.
- OperatingPeriods: date-time windows during which a DayType (or time bands) apply.
- DayTypeAssignments: binds DayTypes to date ranges or specific dates, including exceptions.
- OperatingDays: optional explicit list of individual operating dates when a more granular control is needed.

Typical elements explained
- DayTypes
  - Defines reusable day patterns. Use properties/PropertyOfDay/DaysOfWeek to declare days (e.g., Monday Tuesday ...).
  - Can be combined with OperatingPeriods in DayTypeAssignments.
- OperatingPeriods
  - Defines a validity window with FromDate and ToDate as xs:dateTime (e.g., 2026-03-01T00:00:00Z).
  - Usually referenced by OperatingPeriodRef from DayTypeAssignment.
- DayTypeAssignments
  - Connects a DayType to a date (Date) or to an OperatingPeriod (OperatingPeriodRef).
  - Use isAvailable element to include/exclude a day; set to false for exception dates.
  - order attribute can be used to control evaluation order when multiple assignments may overlap.
- OperatingDays
  - Explicit dates of operation; useful for enumerated calendars or to represent special schedules.

Keys, versioning and references
- id and version
  - Use a stable, globally unique id within your codespace. Example patterns:
    - ERP:ServiceCalendarFrame:1, ERP:DayType:Weekday, ERP:OperatingPeriod:2026-Q2
  - version should be incremented when a logical change is made; use positive integers as strings (e.g., "1", "2").
- References (OperatingPeriodRef, DayTypeRef)
  - Always provide @ref pointing to the target object id and a matching @versionRef.
  - Example: <OperatingPeriodRef ref="ERP:OperatingPeriod:2026-Q2" versionRef="1"/>

Complete, valid NeTEx 2.0 example
The following PublicationDelivery contains a CompositeFrame with one ServiceCalendarFrame that defines weekday and weekend patterns for a period, binds them via DayTypeAssignments, and adds a single exception day with isAvailable=false. Codespace used: ERP.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="2.0">
  <PublicationTimestamp>2026-02-27T23:25:00Z</PublicationTimestamp>
  <ParticipantRef>ERP:Participant:ENTUR</ParticipantRef>
  <Description>Service calendar example with DayTypes, OperatingPeriod, DayTypeAssignments and exception date.</Description>
  <dataObjects>
    <CompositeFrame id="ERP:CompositeFrame:ServiceCalendar:1" version="1">
      <Name>Service Calendar Package</Name>
      <frames>
        <ServiceCalendarFrame id="ERP:ServiceCalendarFrame:1" version="1">
          <Name>Service Calendar 2026 Q2</Name>
          <dayTypes>
            <DayType id="ERP:DayType:Weekday" version="1">
              <Name>Weekdays</Name>
              <properties>
                <PropertyOfDay>
                  <DaysOfWeek>Monday Tuesday Wednesday Thursday Friday</DaysOfWeek>
                </PropertyOfDay>
              </properties>
            </DayType>
            <DayType id="ERP:DayType:Weekend" version="1">
              <Name>Weekend</Name>
              <properties>
                <PropertyOfDay>
                  <DaysOfWeek>Saturday Sunday</DaysOfWeek>
                </PropertyOfDay>
              </properties>
            </DayType>
          </dayTypes>
          <operatingPeriods>
            <OperatingPeriod id="ERP:OperatingPeriod:2026-Q2" version="1">
              <FromDate>2026-03-01T00:00:00Z</FromDate>
              <ToDate>2026-06-30T23:59:59Z</ToDate>
            </OperatingPeriod>
          </operatingPeriods>
          <dayTypeAssignments>
            <DayTypeAssignment id="ERP:DayTypeAssignment:Weekday:Q2" version="1" order="1">
              <OperatingPeriodRef ref="ERP:OperatingPeriod:2026-Q2" versionRef="1"/>
              <DayTypeRef ref="ERP:DayType:Weekday" versionRef="1"/>
            </DayTypeAssignment>
            <DayTypeAssignment id="ERP:DayTypeAssignment:Weekend:Q2" version="1" order="2">
              <OperatingPeriodRef ref="ERP:OperatingPeriod:2026-Q2" versionRef="1"/>
              <DayTypeRef ref="ERP:DayType:Weekend" versionRef="1"/>
            </DayTypeAssignment>
            <DayTypeAssignment id="ERP:DayTypeAssignment:Exception:LabourDay" version="1" order="3">
              <Date>2026-05-01</Date>
              <DayTypeRef ref="ERP:DayType:Weekday" versionRef="1"/>
              <isAvailable>false</isAvailable>
            </DayTypeAssignment>
          </dayTypeAssignments>
        </ServiceCalendarFrame>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

Validation notes
- This example is valid against NeTEx 2.0 schemas and was validated before inclusion.
- For production, validate PublicationDelivery documents against netex_publication.xsd.
- netex_publication_noConstraint.xsd is for development/debugging only and SHOULD NOT be used in production.

See also
- Frames overview: ../FramesOverview.md
- XSD 2.0/README: ../../XSD%202.0/README.md
