# PassengerStopAssignment — Table

This table describes the core elements used to assign a planned stop to a specific passenger facility (Quay).

| Property | Type | Card. | Description | Notes |
|---|---|---:|---|---|
| id | Identifier | 1..1 | NeTEx identifier for the PassengerStopAssignment. | Use codespace/namespace "ERP" in identifiers, e.g. ERP:PassengerStopAssignment:PSA1. |
| version | Version | 1..1 | Version of the PassengerStopAssignment. | String or integer, follows NeTEx conventions. |
| ScheduledStopPointRef | Reference | 1..1 | Reference to the planned stop in the stop sequence. | Must resolve to an existing ScheduledStopPoint in the same logical context (e.g., ServiceFrame/TimetableFrame). |
| QuayRef | Reference | 1..1 | Reference to the concrete platform/edge (Quay) used. | Must resolve to a Quay. |
| StopPlaceRef | Reference | 0..1 | Reference to the StopPlace that the Quay belongs to. | Optional. If present, QuayRef must belong to this StopPlace. |

Constraints and validation
- QuayRef must belong to the referenced StopPlace (if StopPlaceRef is provided).
- Exactly one default assignment per ScheduledStopPoint within a pattern is recommended.
- Overrides for specific dated or time-bounded journeys should be modeled as separate assignments with appropriate scoping.

Frame context
- PassengerStopAssignment instances are typically included in a ServiceFrame (or TimetableFrame) alongside the referenced ScheduledStopPoints.

Operational guidance
- Ensure quay choices match on-site signage and wayfinding to improve passenger information consistency.
