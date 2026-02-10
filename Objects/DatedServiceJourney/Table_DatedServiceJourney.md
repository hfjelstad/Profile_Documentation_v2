# DatedServiceJourney – Fields (Profile: next)

| Type      | Name                     | Description                                                                                     | Cardinality |
|-----------|---------------------------|-------------------------------------------------------------------------------------------------|-------------|
| Attribute | **version**               | Object version number                                                                           | 1:1         |
| Attribute | **id**                    | Unique identifier                                                                               | 1:1         |
| Attribute | **created**               | Timestamp when the object was created                                                           | 0:1         |
| Element   | **ServiceAlteration**     | Indicates if the journey is planned, replaced, or extraJourney (default = planned)              | 0:1         |
| Reference | **BlockRef**              | Reference to a Block or TrainBlock                                                              | 0:1         |
| Reference | **ServiceJourneyRef**     | Reference to the underlying `ServiceJourney` template                                           | 1:1         |
| Element   | **replacedJourneys**      | Container for references to dated journeys being replaced or reinforced                         | 0:1         |
| Reference | **DatedVehicleJourneyRef**| References to *dated journeys* being replaced/reinforced. May still use DatedServiceJourney IDs | 0..*        |

> **Note:**  
> `DatedServiceJourneyRef` has been **removed** in the `next` profile branch and replaced by:  
> `replacedJourneys → DatedVehicleJourneyRef`.