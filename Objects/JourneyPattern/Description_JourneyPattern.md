# Description: JourneyPattern

This page describes the JourneyPattern object (stop sequence pattern) as used in the profile. A JourneyPattern defines the ordered sequence of stops for a trip and is referenced by ServiceJourney.

Purpose: Provide an operational overview of JourneyPattern, its key relations, and central fields. The dated execution of a trip is described by DatedServiceJourney; the stop times remain attached to ServiceJourney through passingTimes.

Key relationships
- ServiceJourney: References the chosen JourneyPattern to derive the stop sequence used for passingTimes.
- Route (optional): Associates the pattern with a higher-level path.
- StopPointInJourneyPattern: The ordered list of points (stops) that constitute the pattern; each points to a ScheduledStopPoint.

Central fields
- id, version, Name
- routeRef (optional)
- pointsInSequence (list of StopPointInJourneyPattern)
  - StopPointInJourneyPattern: id, order, ScheduledStopPointRef, ForBoarding/ForAlighting (optional)

Business rules (overview)
- A JourneyPattern should contain at least two StopPointInJourneyPattern entries and be internally consistent and ordered.
- StopPointInJourneyPattern must reference valid ScheduledStopPoint objects.
- ForBoarding/ForAlighting flags (if provided) should be consistent with operational intent and passenger information.

Example
See Objects/JourneyPattern/Example_JourneyPattern.xml for a minimal example (ERP codespace) that matches the ServiceJourney example using JP_001 and StopPointInJourneyPattern refs :1..3.

Changelog
- 2026-02-13: Initial version in English, aligned with ServiceJourney example (ERP:JourneyPattern:JP_001).
