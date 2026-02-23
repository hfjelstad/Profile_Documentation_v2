# Objects documentation overview

This repository section contains the object documentation for the profile. All object docs follow a uniform structure and conventions to ensure consistency and easy navigation.

Standard structure per object
- Files per object (all in English):
  - Description_<Object>.md
  - Table_<Object>.md (columns: Property | XPath | Card. | Type/Values | Example)
  - Example_<Object>.xml (minimal example)
  - Optional: Example_<Object>_Extended_XX_<Scenario>.xml for scenario-specific cases

Language and conventions
- English only for documentation text.
- ERP as the codespace/namespace for all identifiers and references.
- Cardinality format: 0..1, 1..1, 0..*.
- NeTEx default namespace; examples are wrapped in PublicationDelivery.
- Place elements in their relevant Frames (e.g., ServiceFrame, TimetableFrame, ResourceFrame) within examples.

Table standard
- Table_<Object>.md MUST use the following column order:
  - Property | XPath | Card. | Type/Values | Example
- Include at the end of the table file:
  - Validation rules: bullet list of key checks applicable to the object.
  - Related documents: links to Description_* and related objects.

Example standard
- PublicationDelivery envelope with ERP:ParticipantRef.
- All references MUST be resolvable within the same delivery (or via referenced Frames in the delivery).
- Provide a minimal example and add scenario-specific variants where relevant.

Nomenclature and consistency
- Use consistent terms across documents: OperatingDay vs DayType, JourneyPattern, Block/TrainBlock, etc.
- File naming uses American English spelling and consistent casing; for instance, use Lifecycle_* (not Lifecylce_*).

Index of objects and links
- Authority
  - Description: Objects/Authority/Description_Authority.md
  - Table: Objects/Authority/Table_Authority.md
  - Example: Objects/Authority/Example_Authority.xml
- DayType
  - Description: Objects/DayType/Description_DayType.md
  - Table: Objects/DayType/Table_DayType.md
  - Example: Objects/DayType/Example_DayType.xml
- DatedServiceJourney
  - Description: Objects/DatedServiceJourney/Description_DatedServiceJourney.md
  - Table: Objects/DatedServiceJourney/Table_DatedServiceJourney.md
  - Example (minimal): Objects/DatedServiceJourney/Example_DatedServiceJourney.xml
  - Extended examples (scenarios):
    - Reinforcement: Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_01_Reinforcement.xml
    - Replacement: Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_02_Replacement.xml
    - Block-linked: Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_03_BlockLinked.xml
    - Multiple replacements: Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_04_MultiRef.xml
  - Lifecycle: Objects/DatedServiceJourney/Lifecycle_DatedServiceJourney.md
- Interchange
  - Description: Objects/Interchange/Description_Interchange.md
  - Table: Objects/Interchange/Table_Interchange.md
  - Example: Objects/Interchange/Example_Interchange.xml
- JourneyPattern
  - Description: Objects/JourneyPattern/Description_JourneyPattern.md
  - Table: Objects/JourneyPattern/Table_JourneyPattern.md
  - Example: Objects/JourneyPattern/Example_JourneyPattern.xml
- Line
  - Description: Objects/Line/Description_Line.md
  - Table: Objects/Line/Table_Line.md
  - Example: Objects/Line/Example_Line.xml
- Operator
  - Description: Objects/Operator/Description_Operator.md
  - Table: Objects/Operator/Table_Operator.md
  - Example: Objects/Operator/Example_Operator.xml
- PassengerStopAssignment
  - Description: Objects/PassengerStopAssignment/Description_PassengerStopAssignment.md
  - Table: Objects/PassengerStopAssignment/Table_PassengerStopAssignment.md
  - Example: Objects/PassengerStopAssignment/Example_PassengerStopAssignment.xml
- Quay
  - Description: Objects/Quay/Description_Quay.md
  - Table: Objects/Quay/Table_Quay.md
  - Example: Objects/Quay/Example_Quay.xml
- Route
  - Description: Objects/Route/Description_Route.md
  - Table: Objects/Route/Table_Route.md
  - Example: Objects/Route/Example_Route.xml
- ScheduledStopPoint
  - Description: Objects/ScheduledStopPoint/Description_ScheduledStopPoint.md
  - Table: Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md
  - Example: Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml
- ServiceJourney
  - Description: Objects/ServiceJourney/Description_ServiceJourney.md
  - Table: Objects/ServiceJourney/Table_ServiceJourney.md
  - Example: Objects/ServiceJourney/Example_ServiceJourney.xml
- StopPlace
  - Description: Objects/StopPlace/Description_StopPlace.md
  - Table: Objects/StopPlace/Table_StopPlace.md
  - Example: Objects/StopPlace/Example_StopPlace.xml
- TrainBlock
  - Description: Objects/TrainBlock/Description_TrainBlock.md
  - Table: Objects/TrainBlock/Table_TrainBlock.md
  - Example: Objects/TrainBlock/Example_TrainBlock.xml
- Vehicle
  - Description: Objects/Vehicle/Description_Vehicle.md
  - Table: Objects/Vehicle/Table_Vehicle.md
  - Example: Objects/Vehicle/Example_Vehicle.xml
- VehicleType
  - Description: Objects/VehicleType/Description_VehicleType.md
  - Table: Objects/VehicleType/Table_VehicleType.md
  - Example: Objects/VehicleType/Example_VehicleType.xml

Notes
- If any file is missing for an object, create it following this structure and conventions.
- Keep commits one file per commit on branch EnStandardBranch and open/attach to a pull request against review.
