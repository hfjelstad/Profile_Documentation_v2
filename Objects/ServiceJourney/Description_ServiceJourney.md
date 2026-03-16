# ServiceJourney

Document status: Stable
Object: ServiceJourney
Profile scope: Timetable and journeys (NeTEx Part 2)
File path: Objects/ServiceJourney/Description_ServiceJourney.md
Related table: ./Table_ServiceJourney.md
Related examples: ./Example_ServiceJourney_MIN.xml, ./Example_ServiceJourney_NP.xml

## Purpose
This document describes the ServiceJourney object in the profile. A ServiceJourney represents a planned public‑transport vehicle journey that operates along a JourneyPattern with timing information at stops and references to related operational concepts.

## Scope
This description focuses on the conceptual and cross‑object semantics for ServiceJourney. Field‑level rules, cardinalities, and allowed values are specified in the attribute table (see Table_ServiceJourney.md). XML examples illustrate the minimum and a typical profile instance.

## Structure overview
- Object: ServiceJourney
- Key references: JourneyPatternRef, Calls/TimetabledPassingTimes, DayType/ServiceCalendar, Line/Route, Operator, optional Block
- Realization on specific dates: DatedServiceJourney
- Complementary specification: ./Table_ServiceJourney.md

## Relationships
### JourneyPattern
- ServiceJourney shall reference the JourneyPattern that defines the ordered sequence of ScheduledStopPoints used by this journey.

### Calls and TimetabledPassingTimes
- Calls associated with a ServiceJourney must be consistent with the JourneyPattern’s stop sequence.
- TimetabledPassingTimes provide the timing at each call as required by the profile (arrival/departure and any runtime/layover rules).

### DayType / ServiceCalendar
- Operating days are governed by DayType assignments and/or ServiceCalendar constructs according to the profile’s scheduling rules.

### DatedServiceJourney
- A DatedServiceJourney is the dated realization of a ServiceJourney.
- See: ../DatedServiceJourney/Description_DatedServiceJourney.md

### Line / Route / Operator
- ServiceJourney may reference the producing Operator and be associated with a Line/Route in line with profile rules.

### Blocks / Interlining (if applicable)
- Where supported by the profile, ServiceJourney may participate in a Block to indicate vehicle workings across multiple journeys.

## Key constraints (profile)
- Identification/versioning must follow repository conventions for IDs and version attributes.
- JourneyPatternRef is required and defines the stop sequence for the journey.
- The set of Calls/TimetabledPassingTimes must align 1‑to‑1 with the JourneyPattern’s ScheduledStopPoints and order.
- Timing rules must comply with the profile (arrival/departure presence, run/layover handling, after‑midnight times).
- Operating days must be expressed through DayType/ServiceCalendar as profiled.
- References to Line, Route, and Operator shall be provided when mandated by the profile context.

## Examples
- Minimal example
  - File: ./Example_ServiceJourney_MIN.xml
  - Demonstrates only mandatory elements and references for a valid ServiceJourney in this profile.
- Normal profile example
  - File: ./Example_ServiceJourney_NP.xml
  - Demonstrates common optional fields and typical cross‑references beyond the minimum.

## Cross‑references
- Attribute table: ./Table_ServiceJourney.md
- Dated realization: ../DatedServiceJourney/Description_DatedServiceJourney.md

## Paths and linking rules
- All links in this document are relative to its file path.
- Cross‑object links use consistent, relative paths per repository documentation rules.

## XSD and standard references
- NeTEx Part 2 (timetable and journey definitions) is the normative standard context.
- The repository tracks NeTEx 2.0 schemas in the XSD directory.

## Change history
- 2026‑03‑16: Rewritten to align with Object_Description_Template (sections, relative links, constraints) and repository documentation rules.
