# PassengerStopAssignment

Purpose
- Specifies the exact passenger facility (typically a platform edge, Quay) to be used for a planned stop in a journey. It links a planned stop (ScheduledStopPoint) to a physical platform edge within a stop place (StopPlace), so that passengers and operators know precisely where boarding and alighting occur.

Position in the model
- Used together with the planned stop sequence of a line pattern/service to describe the actual platform for each stop. A default assignment can be expressed as part of the planned pattern and may be overridden for specific departures when needed.

Key references and fields
- ScheduledStopPointRef: references the planned stop in the sequence.
- QuayRef: references the concrete platform/edge used.
- StopPlaceRef (optional): references the StopPlace the quay belongs to.
- Standard metadata (id, version) follow the normal NeTEx conventions.

Typical use cases
- Disambiguate which platform applies at complex interchanges with multiple quays.
- Separate default usage from exceptions/variations for specific dated or time-based departures.
- Improve customer information, signage planning, and operations by providing a clear link from the planned stop to the physical location.

Common patterns
- One assignment per planned stop in a pattern (one-to-one between ScheduledStopPoint and Quay).
- Overrides for selected departures when the platform varies by time or due to operational measures.

Consistency and validation
- QuayRef must belong to the referenced StopPlace (if StopPlaceRef is used).
- References should reside in the same frame context (e.g., TimetableFrame/ServiceFrame) so they can be resolved consistently.
- There should not be multiple conflicting assignments for the same planned stop and departure.

Notes
- For customer-facing outputs, ensure the chosen quay is aligned with real-world signage and wayfinding.
- Operators may manage seasonal or disruption-related quay changes through temporary overrides rather than editing the default assignment.
