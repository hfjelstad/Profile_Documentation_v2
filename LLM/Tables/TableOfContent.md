# Table of Content

## Guides

How-to guides, conceptual overviews, and reference material:

- [GetStarted](../../Guides/GetStarted/GetStarted_Guide.md) – Minimal steps to begin working with the profile
- [NeTExConventions](../../Guides/NeTExConventions/NeTEx_Conventions.md) – Casing rules, naming patterns, and a minimal example
- [SeparationOfConcerns](../../Guides/SeparationOfConcerns/SeparationOfConcerns.md) – Domain separation, coupling strategies, and cross-frame patterns
- [Tools](../../Guides/Tools/Tools_Guide.md) – Editors, plugins, validators, and development workflow
- [Validation](../../Guides/Validation/Validation.md) – How to validate NeTEx XML against schemas and rules
- [Interchange](../../Guides/InterchangeOnly/Interchange_Guide.md) – Planned transfers, guaranteed connections, and interchangeOnly stops
- [OrganisationalGovernance](../../Guides/OrganisationalGovernance/OrganisationalGovernance_Guide.md) – Authority, Operator, Contract, and ResponsibilitySet
- [StopInfrastructure](../../Guides/StopInfrastructure/StopInfrastructure_Guide.md) – Logical stops, physical platforms, and the PassengerStopAssignment bridge
- [JourneyLifecycle](../../Guides/JourneyLifecycle/JourneyLifecycle_Guide.md) – Line → Route → JourneyPattern → ServiceJourney → DatedServiceJourney
- [VehicleScheduling](../../Guides/VehicleScheduling/VehicleScheduling_Guide.md) – Blocks, VehicleType, Vehicle, and fleet assignment
- [PassengerInformation](../../Guides/PassengerInformation/PassengerInformation_Guide.md) – DestinationDisplay, Notice, and FlexibleServiceProperties
- [Accessibility](../../Guides/Accessibility/Accessibility_Guide.md) – AccessibilityAssessment, equipment, and indoor navigation paths
- [FareModelling](../../Guides/FareModelling/FareModelling_Guide.md) – Products, zones, tariffs, and sales offer packages
- [DecisionMakers](../../Guides/DecisionMakers/DecisionMakers_Guide.md) – NeTEx overview for decision makers and stakeholders
- [RegulatoryCompliance](../../Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md) – Delegated Regulation 2017/1926 requirements and NAP submission
- [MaaSConsumers](../../Guides/MaaSConsumers/MaaSConsumers_Guide.md) – Consuming NeTEx datasets as a MaaS platform
- [NetworkTimetable](../../Guides/NetworkTimetable/NetworkTimetable_Guide.md) – Producing and consuming NeTEx timetable datasets (shared + line file split, reference linking, versioning)
- [ExtendedSales_and_DeviationHandling](../../Guides/ExtendedSales_and_DeviationHandling/ExtendedSales_and_DeviationHandling_Guide.md) – Extended sales window beyond IM approval, DatedServiceJourney.id as sales key, deviation handling (cancellations, replacements, reinforcements, supplementary journeys)
- [Calendar](../../Guides/Calendar/Calendar_Guide.md) – DayType, OperatingPeriod, DayTypeAssignment, OperatingDay — when services operate, exception handling, pattern-based vs date-based scheduling

## Frames

Documentation for NeTEx frames (containers):

- [CompositeFrame](../../Frames/CompositeFrame/Description_CompositeFrame.md) – Container frame grouping multiple frames into a single delivery
- [FareFrame](../../Frames/FareFrame/Description_FareFrame.md) – Fares, tariffs and fare products
- [ResourceFrame](../../Frames/ResourceFrame/Description_ResourceFrame.md) – Organizations and resources
- [SalesTransactionFrame](../../Frames/SalesTransactionFrame/Description_SalesTransactionFrame.md) – Sales transaction data
- [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Description_ServiceCalendarFrame.md) – Service calendars and day types
- [ServiceFrame](../../Frames/ServiceFrame/Description_ServiceFrame.md) – Lines, routes and patterns
- [SiteFrame](../../Frames/SiteFrame/Description_SiteFrame.md) – Stop places and physical infrastructure
- [TimetableFrame](../../Frames/TimetableFrame/Description_TimetableFrame.md) – Service journeys and vehicle schedules
- [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Description_VehicleScheduleFrame.md) – Vehicle scheduling and assignments

## Objects

Detailed documentation for NeTEx objects:

- [AlternativeName](../../Objects/AlternativeName/Description_AlternativeName.md) – Alternative names for objects
- [AlternativeText](../../Objects/AlternativeText/Description_AlternativeText.md) – Alternative text representations
- [Authority](../../Objects/Authority/Description_Authority.md) – Transit authority organization
- [Codespace](../../Objects/Codespace/Description_Codespace.md) – XML namespace mapping definitions
- [Contract](../../Objects/Contract/Description_Contract.md) – Agreements and contracts
- [DatedServiceJourney](../../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) – Service journeys for specific dates
- [DayType](../../Objects/DayType/Description_DayType.md) – Day type definitions (weekdays, holidays, etc.)
- [DayTypeAssignment](../../Objects/DayTypeAssignment/Description_DayTypeAssignment.md) – Binds DayTypes to dates or OperatingPeriods
- [DestinationDisplay](../../Objects/DestinationDisplay/Description_DestinationDisplay.md) – Destination display content
- [FareContract](../../Objects/FareContract/Description_FareContract.md) – Fare contract definitions
- [FareZone](../../Objects/FareZone/Description_FareZone.md) – Tariff zones for fares
- [FlexibleServiceProperties](../../Objects/FlexibleServiceProperties/Description_FlexibleServiceProperties.md) – Flexible transport properties
- [GroupOfLines](../../Objects/GroupOfLines/Description_GroupOfLines.md) – Grouping of transport lines
- [Interchange](../../Objects/Interchange/Description_Interchange.md) – Service interchanges and transfers
- [JourneyPattern](../../Objects/JourneyPattern/Description_JourneyPattern.md) – Route patterns with ordered stops
- [Line](../../Objects/Line/Description_Line.md) – Public transport lines
- [LinkSequenceProjection](../../Objects/LinkSequenceProjection/Description_LinkSequenceProjection.md) – Link sequence projections
- [Notice](../../Objects/Notice/Description_Notice.md) – Notices and information
- [OperatingDay](../../Objects/OperatingDay/Description_OperatingDay.md) – Specific calendar dates for DatedServiceJourney
- [OperatingPeriod](../../Objects/OperatingPeriod/Description_OperatingPeriod.md) – Operating period definitions
- [Operator](../../Objects/Operator/Description_Operator.md) – Transport operators/companies
- [Parking](../../Objects/Parking/Description_Parking.md) – Parking facilities
- [PassengerStopAssignment](../../Objects/PassengerStopAssignment/Description_PassengerStopAssignment.md) – Passenger to quay assignments
- [PurposeOfGrouping](../../Objects/PurposeOfGrouping/Description_PurposeOfGrouping.md) – Grouping purposes and types
- [Quay](../../Objects/Quay/Description_Quay.md) – Boarding and alighting points
- [ResponsibilitySet](../../Objects/ResponsibilitySet/Description_ResponsibilitySet.md) – Organization responsibilities
- [Route](../../Objects/Route/Description_Route.md) – Transport routes
- [SanitaryEquipment](../../Objects/SanitaryEquipment/Description_SanitaryEquipment.md) – Sanitary facilities at stops
- [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Description_ScheduledStopPoint.md) – Stop points in journey patterns
- [ServiceJourney](../../Objects/ServiceJourney/Description_ServiceJourney.md) – Service journeys and schedules
- [ShelterEquipment](../../Objects/ShelterEquipment/Description_ShelterEquipment.md) – Waiting shelters at stops
- [StopPlace](../../Objects/StopPlace/Description_StopPlace.md) – Stop places and physical infrastructure
- [TariffZone](../../Objects/TariffZone/Description_TariffZone.md) – Fare calculation zones
- [TicketingEquipment](../../Objects/TicketingEquipment/Description_TicketingEquipment.md) – Ticketing and validation equipment
- [TopographicPlace](../../Objects/TopographicPlace/Description_TopographicPlace.md) – Geographic locations and place names
- [TrainBlock](../../Objects/TrainBlock/Description_TrainBlock.md) – Train block assignments
- [Vehicle](../../Objects/Vehicle/Description_Vehicle.md) – Rolling stock and vehicles
- [VehicleType](../../Objects/VehicleType/Description_VehicleType.md) – Vehicle classifications
- [WaitingRoomEquipment](../../Objects/WaitingRoomEquipment/Description_WaitingRoomEquipment.md) – Waiting room facilities
