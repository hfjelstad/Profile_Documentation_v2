# Description: ServiceJourney

This page describes the ServiceJourney object (planned trip) as used in the profile. It mirrors the structure and level of detail from the DatedServiceJourney description, but adapts the content to planned (non-dated) trips.

Purpose: Provide a concise, operational overview of what a ServiceJourney is, how it connects to related objects, and which fields are central. Detailed field descriptions can be found in the ServiceJourney table.

Related documents:
- Table for ServiceJourney: Objects/ServiceJourney/Table_ServiceJourney.md
- Dated instance of a trip: Objects/DatedServiceJourney/Description_DatedServiceJourney.md

## What is a ServiceJourney?
A ServiceJourney represents a planned trip in the timetable. It references a JourneyPattern to define the stop sequence, and it contains metadata such as operator, codes, and optional linkage to a block/roster. Planned stop times are expressed using passingTimes (TimetabledPassingTime) associated to StopPointInJourneyPattern entries. The dated variant (DatedServiceJourney) expresses the same trip for a specific operating day.

## Key relationships
- Line/Route: Associates the trip to a line/route via references.
- JourneyPattern: Provides the stop sequence and structure used by the trip.
- Operator: The operator performing the trip.
- Block/VehicleJourneyGroup (if used): Optional linkage to a vehicle block/roster to ensure continuity between subsequent trips.
- DayType/OperatingProfile: Specifies on which days the trip normally operates (per-date execution belongs to the dated instances and/or production rules).

## Central fields
See the table Objects/ServiceJourney/Table_ServiceJourney.md for a complete list and cardinalities. Typical identifiers and references include:
- id, version
- privateCode/publicCode
- journeyPatternRef (selected pattern)
- lineRef/routeRef (owning line/route)
- operatorRef
- dayTypeRefs/operatingProfile (days of operation)
- blockRef (optional roster linkage)
- passingTimes (list of TimetabledPassingTime) with StopPointInJourneyPatternRef and ArrivalTime/DepartureTime

## Business rules (overview)
- A ServiceJourney must reference exactly one valid JourneyPattern. The pattern's stop sequence is authoritative for the trip.
- A ServiceJourney should belong to a single line/route; inconsistent cross-line references are not allowed.
- If block/roster is used, trips in the same block must be time-compatible without overlap for the same vehicle.
- DayType/OperatingProfile governs planned operation; per-date deviations are handled at the DatedServiceJourney level.

## Comparison with DatedServiceJourney
- ServiceJourney = template/plan for a trip without a concrete date.
- DatedServiceJourney = concrete instance of a trip on a given date, with potential alterations (replacement, reinforcement, etc.).
- Date-specific fields (e.g., ServiceAlteration on a specific day) belong to DatedServiceJourney, not ServiceJourney.

## Data quality and validation (recommendations)
- Validate that journeyPatternRef, lineRef, and operatorRef exist and are consistent.
- Ensure that DayType/OperatingProfile covers the expected timetable without conflicts.
- Use privateCode/publicCode consistently for traceability and presentation.
- Ensure passingTimes are present and aligned with the referenced StopPointInJourneyPattern sequence, using ArrivalTime and/or DepartureTime as appropriate.

## Example
See Objects/ServiceJourney/Example_ServiceJourney.xml for a minimal example including passingTimes.

## Changelog
- 2026-02-13: Initial version in English, adapted from the DatedServiceJourney template; added note on passingTimes.
