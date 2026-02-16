# PassengerStopAssignment Attribute Table

| **Name**                        | **Description**                                      | **Type**   | **Usage**     |
|---------------------------------|------------------------------------------------------|------------|---------------|
| id                              | Unique identifier for the assignment                | Identifier | Mandatory     |
| version                         | Version of the element                              | String     | Mandatory     |
| order                           | Sequence number (technical, no business meaning)    | Integer    | Mandatory     |
| ScheduledStopPointRef           | Reference to the logical stop                       | Reference  | Mandatory     |
| QuayRef                         | Reference to the physical quay                      | Reference  | Mandatory     |
| StopPlaceRef                    | Reference to the stop place                         | Reference  | Optional      |
| ForDatedVehicleJourneyRef       | Reference to a specific DatedServiceJourney         | Reference  | Optional      |
