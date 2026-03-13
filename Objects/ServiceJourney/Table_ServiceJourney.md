# Table — ServiceJourney

## Structure Overview

```text
ServiceJourney
 ├─ @id
 ├─ @version
 ├─ Name
 ├─ PrivateCode
 ├─ Description
 ├─ TransportMode
 ├─ TransportSubmode
 │   ├─ BusSubmode
 │   └─ RailSubmode
 ├─ JourneyPatternRef/@ref
 ├─ LineRef/@ref
 ├─ FlexibleLineRef/@ref
 ├─ OperatorRef/@ref
 ├─ dayTypes
 │   └─ DayTypeRef/@ref (0..*)
 ├─ passingTimes
 │   └─ TimetabledPassingTime (1..*)
 │       ├─ @id
 │       ├─ StopPointInJourneyPatternRef/@ref
 │       ├─ ArrivalTime
 │       ├─ DepartureTime
 │       ├─ ArrivalDayOffset
 │       ├─ DepartureDayOffset
 │       ├─ EarliestDepartureTime
 │       └─ LatestArrivalTime
 ├─ keyList
 │   └─ KeyValue (0..*)
 ├─ parts
 │   └─ JourneyPart (0..*)
 └─ BlockRef/@ref
```
## Flat Table

| Element | Type | MIN | ERP | NP | Description | Path |
|--------|------|-----:|:--:|:--:|-------------|------|
| @id | xsd:ID | 1..1 |  |  | Unique identifier following {CODESPACE}:ServiceJourney:{LocalId} | ServiceJourney/@id |
| @version | xsd:string | 1..1 |  |  | Version label (e.g., "1"). Increment on changes. | ServiceJourney/@version |
| Name | xsd:string | 0..1 |  |  | Human‑readable name of the journey | Name |
| PrivateCode | xsd:normalizedString | 0..1 |  |  | Internal non‑public code (e.g., trip or train number) | PrivateCode |
| Description | xsd:string | 0..1 |  |  | Free‑text description | Description |
| TransportMode | TransportModeEnumeration | 0..1 |  |  | Public transport mode (e.g., bus, rail) | TransportMode |
| BusSubmode | BusSubmodeEnumeration | 0..1 |  |  | Submode for bus services | TransportSubmode/BusSubmode |
| RailSubmode | RailSubmodeEnumeration | 0..1 |  |  | Submode for rail services | TransportSubmode/RailSubmode |
| JourneyPatternRef | VersionedRef | 1..1 |  |  | Reference to a JourneyPattern defining the stop sequence | JourneyPatternRef/@ref |
| LineRef | VersionedRef | 0..1 |  |  | Reference to the served Line | LineRef/@ref |
| FlexibleLineRef | VersionedRef | 0..1 |  |  | Reference to a FlexibleLine (on‑demand services) | FlexibleLineRef/@ref |
| OperatorRef | VersionedRef | 0..1 |  |  | Reference to an Operator | OperatorRef/@ref |
| DayTypeRef | VersionedRef | 0..* |  |  | DayType(s) on which the journey operates | dayTypes/DayTypeRef/@ref |
| TimetabledPassingTime | TimetabledPassingTime | 1..* |  |  | Collection of scheduled passing/stop times | passingTimes/TimetabledPassingTime |
| TimetabledPassingTime/@id | xsd:ID | 0..1 |  |  | Optional identifier for the TimetabledPassingTime element | passingTimes/TimetabledPassingTime/@id |
| StopPointInJourneyPatternRef | VersionedRef | 1..1 |  |  | Reference to a StopPointInJourneyPattern in the JourneyPattern | passingTimes/TimetabledPassingTime/StopPointInJourneyPatternRef/@ref |
| ArrivalTime | xsd:time | 0..1 |  |  | Planned arrival time at the stop | passingTimes/TimetabledPassingTime/ArrivalTime |
| DepartureTime | xsd:time | 0..1 |  |  | Planned departure time from the stop | passingTimes/TimetabledPassingTime/DepartureTime |
| ArrivalDayOffset | xsd:integer | 0..1 |  |  | Day offset applied to ArrivalTime (e.g., +1 for next‑day arrival) | passingTimes/TimetabledPassingTime/ArrivalDayOffset |
| DepartureDayOffset | xsd:integer | 0..1 |  |  | Day offset applied to DepartureTime | passingTimes/TimetabledPassingTime/DepartureDayOffset |
| EarliestDepartureTime | xsd:time | 0..1 |  |  | Earliest allowed pick‑up time (flexible journeys) | passingTimes/TimetabledPassingTime/EarliestDepartureTime |
| LatestArrivalTime | xsd:time | 0..1 |  |  | Latest allowed drop‑off time (flexible journeys) | passingTimes/TimetabledPassingTime/LatestArrivalTime |
| KeyValue | KeyValue | 0..* |  |  | Arbitrary key/value metadata for the journey | keyList/KeyValue |
| JourneyPart | JourneyPart | 0..* |  |  | Used for combined/split journeys | parts/JourneyPart |
| BlockRef | VersionedRef | 0..1 |  |  | Reference to a Block or TrainBlock (vehicle working) | Block

Identifier and codespace conventions
- Use a single codespace consistently across PublicationDelivery.
- Recommended pattern for @id: {CODESPACE}:ServiceJourney:{LocalId}
- ParticipantRef in PublicationDelivery must equal the dataset codespace.

Validation rule
- Always validate raw XML examples against NeTEx 2.0 XSD prior to publication.

Cross‑references
- JourneyPattern: defines the ordered stop sequence for the ServiceJourney
- DayType: dates on which the ServiceJourney runs
- Operator and Line: operator and public‑facing line context
