# Description — ServiceJourney

## Purpose
This document describes the ServiceJourney object as used in the profile, clarifies its role in the data model, and outlines required/optional content, relationships, and business rules. It complements the attribute overview in the associated table specification.

## Scope
ServiceJourney defines a planned operational journey that is intended to run repeatedly according to a timetable (e.g., every weekday). It is distinct from DatedServiceJourney, which represents a concrete run on a specific operating day.

## Definition
A ServiceJourney is a planned run of a public transport vehicle over a sequence of stops, typically derived from a JourneyPattern and bound to a DayType/ServiceCalendar. It contains timing information (e.g., departure/arrival times) and references to operational and customer-facing context such as Line, Route, JourneyPattern, and Operator.

Key characteristics:
- Represents the planned (recurring) instance of a journey.
- References the topology and timing pattern that define stop sequencing and scheduled times.
- Is the source for generating DatedServiceJourney instances for specific dates.

## Attributes and cardinality
For the complete list of attributes, data types, and cardinality, see the object table:
- Table — ServiceJourney: ./Table_ServiceJourney.md

## Relationships
- JourneyPattern: Provides the stop sequence and timing pattern applied by the ServiceJourney.
- Route: The path over which the ServiceJourney operates.
- Line: Customer-facing grouping for ServiceJourneys belonging to the same service.
- DayType / ServiceCalendar: Determines which operating days the ServiceJourney is planned to run.
- Operator (and optionally Authority): Operational responsibility for the ServiceJourney.
- DatedServiceJourney: Instances materialized from a ServiceJourney for specific operating dates.

## Business rules and constraints
- A ServiceJourney MUST reference a Line and either a JourneyPattern or sufficient timing data to infer stop sequencing.
- If a JourneyPattern is referenced, the ServiceJourney’s passing times MUST be consistent with the JourneyPattern’s StopPoints.
- ServiceJourney SHOULD be associated with one or more DayTypes (or equivalent calendar rules) to express planned operating days.
- Where block or vehicle scheduling is applied, a ServiceJourney MAY be linked to Block/VehicleJourney associations in downstream planning layers; such links are outside the scope of this document but must not contradict the ServiceJourney timing.

## XML representation
The XML structure of ServiceJourney follows NeTEx 2.0. Examples specific to ServiceJourney may be added alongside this document when available. For concrete-dated examples, refer to DatedServiceJourney examples under Objects/DatedServiceJourney.

## Cross-references
- DatedServiceJourney — Description: ../DatedServiceJourney/Description_DatedServiceJourney.md
- DatedServiceJourney — Table: ../DatedServiceJourney/Table_DatedServiceJourney.md
- ServiceJourney — Table: ./Table_ServiceJourney.md

## Version history
- 2026-03-16: Revised description aligned with current structure.
