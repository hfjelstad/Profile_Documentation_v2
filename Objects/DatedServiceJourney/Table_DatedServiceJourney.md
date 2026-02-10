# DatedServiceJourney – Fields

| Type      | Name                        | Description                                                                           | Cardinality |

|-----------|-----------------------------|---------------------------------------------------------------------------------------|-------------|
| Attribute | **version**                 | Object version numbering                                                              | 1:1         |
| Attribute | **id**                      | Identifier                                                                            | 1:1         |
| Attribute | **created**                 | DateTime when the object was created                                                  | 0:1         |
| Element   | **ServiceAlteration**       | Enumeration: `[planned, replaced, extraJourney]` (default: `planned`)                 | 0:1         |
| Reference | **BlockRef**                | Reference to Block or TrainBlock                                                      | 0:1         |
| Reference | **ServiceJourneyRef**       | Reference to the `ServiceJourney` template                                            | 1:1         |
| List      | **replacedJourneys**        | Container for references to journeys being replaced/reinforced                        | 0:1         |
| Reference | **DatedVehicleJourneyRef**  | Reference inside `replacedJourneys` to a **dated journey** being replaced/reinforced. | 0:*         |