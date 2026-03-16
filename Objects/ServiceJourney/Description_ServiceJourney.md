# ServiceJourney

## Overview
ServiceJourney represents a planned public-transport vehicle journey within the timetable. It provides the operational intent for a journey pattern with timing at stops and references to related operational concepts.

## Scope and Dependencies
This description follows the repository’s Object Description Template and complements the attribute-level specification in the table file.
- Conformance template: ../../LLM/Templates/Object_Description_Template.md
- Attribute/table reference: ./Table_ServiceJourney.md

## Relationships
- JourneyPattern
  - ServiceJourney shall reference the JourneyPattern that defines the ordered sequence of ScheduledStopPoints used by this journey.
- Calls and TimetabledPassingTimes
  - The set of Calls associated with a ServiceJourney must be consistent with the JourneyPattern’s stop sequence. TimetabledPassingTimes should specify the timing at each call as required by the profile.
- DayType / ServiceCalendar
  - Operating days are governed by DayType assignments and/or ServiceCalendar constructs as profiled. ServiceJourney is realized on actual dates through dated instances.
- DatedServiceJourney
  - A DatedServiceJourney is the dated realization of a ServiceJourney. See: ../DatedServiceJourney/Description_DatedServiceJourney.md
- Line / Route / Operator
  - ServiceJourney may reference the producing Operator and be associated with a Line/Route according to profile rules.
- Blocks / Interlining (if applicable in the profile)
  - Where supported, ServiceJourney may participate in a Block to indicate vehicle workings across multiple journeys.

## Key Constraints in this Profile
The following constraints summarize expected minimums for the profile. See the table file for exact cardinalities and field-level rules.
- Identification and versioning must follow the repository’s ID/version conventions.
- JourneyPatternRef: required; the referenced JourneyPattern defines the stop sequence.
- Calls/TimetabledPassingTimes must align with the JourneyPattern’s ScheduledStopPoints and be provided per profile timing rules (arrival/departure, layover/runtime, and handling of after-midnight times as applicable).
- Association to operating days via DayType/ServiceCalendar must follow the profile’s rules for when the journey runs.
- References to Line, Route, and Operator should be provided when mandated by the profile’s usage context.

## Examples
- Minimal example:
  - File: ./Example_ServiceJourney_MIN.xml
  - Demonstrates only the mandatory elements and references for a valid ServiceJourney in this profile.
- Normal profile example:
  - File: ./Example_ServiceJourney_NP.xml
  - Demonstrates common optional fields and typical cross-references beyond the minimum.

## See also
- Table (attributes and rules): ./Table_ServiceJourney.md
- Dated realization: ../DatedServiceJourney/Description_DatedServiceJourney.md

## Versioning and References
- Standard context: NeTEx Part 2 (timetable and journey definitions)
- Schema baseline used by this repository: NeTEx 2.0 (see XSD directory for details)
- This document conforms to the Object Description Template and repository documentation rules.
