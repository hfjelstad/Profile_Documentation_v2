# ServiceJourney

> Authoritative description for the ServiceJourney object in this profile. This page follows the Object_Description_Template and provides a concise, task‑oriented description with cross‑references to structure, tables, and validated XML examples.

## Purpose
A ServiceJourney represents a planned public transport vehicle journey that performs passenger services along a JourneyPattern on a specific Line. It defines the stop visits and timing, and references operational context such as DayType, Operator and ResponsibilitySet where applicable.

## When to use
Use ServiceJourney to describe a customer‑facing journey that can be offered in timetables and journey planning. It should be used together with JourneyPattern, Route, Line and related operational objects to form a coherent, schedulable service.

## Core characteristics
- Identifies the journey by id and version.
- References Line, JourneyPattern, Operator and other context objects as needed.
- Contains ServiceJourneyPatternTiming elements through stop assignments and run times according to the profile.
- Can be associated with DayType/OperatingPeriod via DatedServiceJourney or validity constructs, depending on publication scope.

## Profile rules and constraints
This profile may restrict which elements are mandatory and how references are formed. Refer to the structure and table overview for the normative list of elements, cardinalities, allowed values and cross‑object references.

- Structure and attribute table: ./Table_ServiceJourney.md

## Examples
The following example files illustrate minimal and normal profile (NP) variants. They are maintained with this object and are expected to be valid against NeTEx 2.0 as published in this repository.

- Minimal profile example: ./Example_ServiceJourney_MIN.xml
- Normal profile example: ./Example_ServiceJourney_NP.xml

## Related objects
For complete context and referential integrity, see the descriptions and tables for the objects commonly referenced by ServiceJourney:
- Line (object description and table)
- JourneyPattern (object description and table)
- DatedServiceJourney (object description and table)
- DayType (object description and table)

Note: Use relative links following the profile’s linking rules when navigating between these objects.

## Notes and guidance
- Ensure identifiers are unique and follow the repository codespace rules.
- Keep ServiceJourney focused on passenger‑carrying operations; use other objects for operational coupling, block working and non‑passenger movements.
- Validate any new or modified XML examples before committing (the existing examples are assumed validated).

## Change log
- Aligned content, sections and cross‑references with Object_Description_Template; clarified purpose, usage and references; added explicit links to structure table and examples.
