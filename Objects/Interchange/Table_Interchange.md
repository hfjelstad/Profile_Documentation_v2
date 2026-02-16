# Interchange Attributes Table

| **Attribute**           | **Type**   | **Usage**       | **Description** |
|--------------------------|-----------|-----------------|-----------------|
| **id**                  | String    | Mandatory       | Unique identifier for the Interchange element. |
| **version**             | String    | Mandatory       | Version of the element. |
| **FromJourneyRef**      | Reference | Mandatory       | Reference to the originating ServiceJourney. |
| **ToJourneyRef**        | Reference | Mandatory       | Reference to the destination ServiceJourney. |
| **Guaranteed**          | Boolean   | Mandatory       | Indicates if the transfer is guaranteed (true/false). |
| **MinimumTransferTime** | Duration  | Optional        | Minimum time required for the transfer (e.g., PT5M). |
| **MaximumWaitTime**     | Duration  | Optional        | Maximum waiting time for the second journey (e.g., PT10M). |
| **StaySeated**          | Boolean   | Optional        | Indicates if passengers can remain seated during the transfer. |

## Relationships
- **Interchange** links two ServiceJourneys.
- **Guaranteed** ensures operational coordination between journeys.