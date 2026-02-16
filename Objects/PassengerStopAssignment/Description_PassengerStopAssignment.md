# PassengerStopAssignment

**Purpose and Usage**
PassengerStopAssignment is used to specify the exact passenger facility (typically a Quay) to be used for a planned stop in a journey. It links a ScheduledStopPoint to a physical platform within a StopPlace, ensuring accurate passenger information and operational planning.

**Key Points:**
- Defines the physical quay for a logical stop.
- Can be applied as a default for a JourneyPattern or overridden for specific departures.
- Improves clarity for passengers and operators.

**Relationships:**
- **ScheduledStopPointRef**: Logical stop in the timetable.
- **QuayRef**: Physical platform.
- **StopPlaceRef**: Optional reference to the stop place.

**Validation Rules:**
- QuayRef must belong to StopPlaceRef if provided.
- All references must be resolvable within the same frame.
