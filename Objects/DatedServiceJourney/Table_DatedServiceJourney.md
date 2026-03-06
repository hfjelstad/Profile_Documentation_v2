# DatedServiceJourney — Schema vs Profile requirements

This table explicitly distinguishes the NeTEx XSD (schema) cardinality from the profile-level requirements used for day-specific timetable publications.

| Element | XSD cardinality | ERP cardinality | Description |
|---|---|---|---|
| @id | 1..1 | 1..1 | ERP scoped identifier, e.g. ERP:DatedServiceJourney:2026-01-01-12345 |
| @version | 1..1 | 1..1 | Use profile-compliant versioning. |
| JourneyRef | 1..1 | 1..1 | Reference to the underlying ServiceJourney. |
| OperatingDayRef | 1..1 | 1..1 | Operating day of this DatedServiceJourney. |
| ServiceAlteration | 0..1 | 0..1 | Status of the journey (e.g. cancellation, replacement, reinforcement). |
| DatedCalls | 0..1 | TBD..TBD | Container for one or more DatedCall elements. |
| DatedCall | 0..* | TBD..TBD | Stop-level dated timing and references. |
