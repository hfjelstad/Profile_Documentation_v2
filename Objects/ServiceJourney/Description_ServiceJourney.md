# ServiceJourney — Description

Purpose
- This document describes the ServiceJourney object in the profile and how it relates to adjacent objects. It follows the documentation structure defined in LLM/README.md and delegates attribute-level rules to the Attribute Table.

Scope
- What is covered: conceptual description, key relationships, placement in the model, and references to authoritative tables and examples.
- Out of scope: full attribute specification, cardinalities, and validation rules (see the Attribute Table).

Authoritative attribute specification
- See the Attribute Table for all fields, cardinality, constraints, and profile-specific rules:
  - ./Table_ServiceJourney.md

Structure overview
- ServiceJourney represents a scheduled vehicle journey running along a JourneyPattern that is associated with a Route and a Line. It is typically activated by DayType/ServiceCalendar conditions and may be grouped into operational Blocks. The Operator provides the service, and additional operational context can be attached via Notices and ServiceFacilitySets (profile dependent).
- Key relationships:
  - JourneyPattern → defines the ordered StopPoints and timing links that the ServiceJourney follows.
  - Route and Line → provide routing and product/branding context for the ServiceJourney.
  - DayType / ServiceCalendar → determine the days on which the ServiceJourney operates.
  - Block → operational chaining of consecutive ServiceJourneys for vehicle/crew planning.
  - Operator → the service provider responsible for operating the ServiceJourney.
  - DatedServiceJourney → instantiates a ServiceJourney on a specific service date, including operational adjustments.

Key XML path overview (informative)
- ServiceJourney located under:
  - CompositeFrame / ServiceFrame / ServiceJourneys / ServiceJourney
- Common references (profile-dependent, indicative only):
  - ServiceJourney / JourneyPatternRef
  - ServiceJourney / LineRef
  - ServiceJourney / OperatorRef
  - ServiceJourney / DayTypeRefs / DayTypeRef
  - ServiceJourney / BlockRef

Examples
- Full examples are maintained as separate XML files:
  - Minimal example: ./Example_ServiceJourney_MIN.xml
  - Normal profile example: ./Example_ServiceJourney_NP.xml
- Notes:
  - XML examples are authoritative for illustrating correct linking and minimal vs. normal payloads, but attribute constraints remain defined by the Attribute Table.

Related documentation
- Attribute table: ./Table_ServiceJourney.md
- DatedServiceJourney — Description: ../DatedServiceJourney/Description_DatedServiceJourney.md

References (informative)
- NeTEx XSD (local copy):
  - ../../XSD 2.0/xsd/netex_part_2/part2_journeyTimes/netex_serviceJourney_support.xsd
  - ../../XSD 2.0/xsd/netex_part_2/part2_journeyTimes/netex_serviceJourney_version.xsd

Change history
- 2026-03-16: Aligned with repository documentation template. Added structure overview, relative links to table and related objects, example references, and informative XSD links.
