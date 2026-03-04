# XML Examples Index

This document lists all Example_*.xml files in the repository. For each entry, the full relative path is provided along with a short description and links to the corresponding Description and Table documents for the object. All examples use the ERP codespace.

| Example (relative path) | Short description | Description | Table |
| --- | --- | --- | --- |
| Objects/Authority/Example_Authority.xml | ERP sample for Authority | [Description_Authority.md](../Objects/Authority/Description_Authority.md) | [Table_Authority.md](../Objects/Authority/Table_Authority.md) |
| Objects/DayType/Example_DayType.xml | ERP sample for DayType | [Description_DayType.md](../Objects/DayType/Description_DayType.md) | [Table_DayType.md](../Objects/DayType/Table_DayType.md) |
| Objects/DatedServiceJourney/Example_DatedServiceJourney.xml | ERP sample for DatedServiceJourney | [Description_DatedServiceJourney.md](../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) | [Table_DatedServiceJourney.md](../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) |
| Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_01_Reinforcement.xml | Extended ERP example: Reinforcement | [Description_DatedServiceJourney.md](../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) | [Table_DatedServiceJourney.md](../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) |
| Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_02_Replacement.xml | Extended ERP example: Replacement | [Description_DatedServiceJourney.md](../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) | [Table_DatedServiceJourney.md](../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) |
| Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_03_BlockLinked.xml | Extended ERP example: Block linked | [Description_DatedServiceJourney.md](../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) | [Table_DatedServiceJourney.md](../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) |
| Objects/DatedServiceJourney/Example_DatedServiceJourney_Extended_04_MultiRef.xml | Extended ERP example: MultiRef | [Description_DatedServiceJourney.md](../Objects/DatedServiceJourney/Description_DatedServiceJourney.md) | [Table_DatedServiceJourney.md](../Objects/DatedServiceJourney/Table_DatedServiceJourney.md) |
| Objects/Interchange/Example_Interchange.xml | ERP sample for Interchange | [Description_Interchange.md](../Objects/Interchange/Description_Interchange.md) | [Table_Interchange.md](../Objects/Interchange/Table_Interchange.md) |
| Objects/JourneyPattern/Example_JourneyPattern.xml | ERP sample for JourneyPattern | [Description_JourneyPattern.md](../Objects/JourneyPattern/Description_JourneyPattern.md) | [Table_JourneyPattern.md](../Objects/JourneyPattern/Table_JourneyPattern.md) |
| Objects/Line/Example_Line.xml | ERP sample for Line | [Description_Line.md](../Objects/Line/Description_Line.md) | [Table_Line.md](../Objects/Line/Table_Line.md) |
| Objects/Operator/Example_Operator.xml | ERP sample for Operator | [Description_Operator.md](../Objects/Operator/Description_Operator.md) | [Table_Operator.md](../Objects/Operator/Table_Operator.md) |
| Objects/PassengerStopAssignment/Example_PassengerStopAssignment.xml | ERP sample for PassengerStopAssignment | [Description_PassengerStopAssignment.md](../Objects/PassengerStopAssignment/Description_PassengerStopAssignment.md) | [Table_PassengerStopAssignment.md](../Objects/PassengerStopAssignment/Table_PassengerStopAssignment.md) |
| Objects/Quay/Example_Quay.xml | ERP sample for Quay | [Description_Quay.md](../Objects/Quay/Description_Quay.md) | [Table_Quay.md](../Objects/Quay/Table_Quay.md) |
| Objects/Route/Example_Route.xml | ERP sample for Route | [Description_Route.md](../Objects/Route/Description_Route.md) | [Table_Route.md](../Objects/Route/Table_Route.md) |
| Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml | ERP sample for ScheduledStopPoint | [Description_ScheduledStopPoint.md](../Objects/ScheduledStopPoint/Description_ScheduledStopPoint.md) | [Table_ScheduledStopPoint.md](../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) |
| Objects/ServiceJourney/Example_ServiceJourney.xml | ERP sample for ServiceJourney | [Description_ServiceJourney.md](../Objects/ServiceJourney/Description_ServiceJourney.md) | [Table_ServiceJourney.md](../Objects/ServiceJourney/Table_ServiceJourney.md) |
| Objects/StopPlace/Example_StopPlace.xml | ERP sample for StopPlace | [Description_StopPlace.md](../Objects/StopPlace/Description_StopPlace.md) | [Table_StopPlace.md](../Objects/StopPlace/Table_StopPlace.md) |
| Objects/TrainBlock/Example_TrainBlock.xml | ERP sample for TrainBlock | [Description_TrainBlock.md](../Objects/TrainBlock/Description_TrainBlock.md) | [Table_TrainBlock.md](../Objects/TrainBlock/Table_TrainBlock.md) |
| Objects/Vehicle/Example_Vehicle.xml | ERP sample for Vehicle | [Description_Vehicle.md](../Objects/Vehicle/Description_Vehicle.md) | [Table_Vehicle.md](../Objects/Vehicle/Table_Vehicle.md) |
| Objects/VehicleType/Example_VehicleType.xml | ERP sample for VehicleType | [Description_VehicleType.md](../Objects/VehicleType/Description_VehicleType.md) | [Table_VehicleType.md](../Objects/VehicleType/Table_VehicleType.md) |

## How to maintain this list

- When adding a new object under Objects/<ObjectName>, ensure there is at least one XML example named Example_<ObjectName>.xml (using codespace ERP), plus Description_<ObjectName>.md and Table_<ObjectName>.md following the master template.
- Update this file by adding a new row with the full relative path to the example and links to the corresponding Description and Table documents.
- Keep entries alphabetically sorted by object name, and when applicable by example filename within the same object (e.g., extended examples).
- Verify that all links resolve correctly in the EnStandardBranch before opening a pull request.
