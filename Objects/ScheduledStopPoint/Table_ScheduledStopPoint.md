# ScheduledStopPoint – Property specification table

This table defines the required and optional properties for a ScheduledStopPoint in the profile. All identifiers MUST use the ERP codespace.

Columns
- Property: Logical name in the profile
- XPath: Location in the NeTEx document
- Card.: Cardinality
- Type/Values: Datatype and allowed values or constraints
- Example: Example value using ERP namespace

| Property | XPath | Card. | Type/Values | Example |
|---|---|---:|---|---|
| id | ServiceFrame/scheduledStopPoints/ScheduledStopPoint/@id | 1..1 | ERP-scoped identifier | ERP:ScheduledStopPoint:1001 |
| version | ServiceFrame/scheduledStopPoints/ScheduledStopPoint/@version | 1..1 | Positive integer or semantic version | 1 |
| Name | ServiceFrame/scheduledStopPoints/ScheduledStopPoint/Name | 0..1 | String | SSP A |
| TimingPointStatus | ServiceFrame/scheduledStopPoints/ScheduledStopPoint/TimingPointStatus | 0..1 | Enumeration (e.g., timingPoint, notTimingPoint) | timingPoint |

Related references
- StopPointInJourneyPattern/ScheduledStopPointRef references a ScheduledStopPoint.
- PassengerStopAssignment links a ScheduledStopPoint to a Quay (physical platform) via QuayRef.

Validation rules
- The combination of id and version uniquely identifies a ScheduledStopPoint within the dataset.
- Each ScheduledStopPoint used in timetables SHOULD have a PassengerStopAssignment to an existing Quay.
- All IDs and references MUST be ERP-scoped (prefix ERP:...).

Related documents
- Objects/ScheduledStopPoint/Description_ScheduledStopPoint.md – narrative description and business rules.
- Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml – minimal NeTEx example using ERP codespace.
