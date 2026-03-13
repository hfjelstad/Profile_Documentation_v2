# Table — ServiceJourney

ServiceJourney
 ├─ @id
 ├─ @version
 ├─ Name
 ├─ PrivateCode
 ├─ Description
 ├─ TransportMode
 ├─ TransportSubmode
 │    ├─ BusSubmode
 │    └─ RailSubmode
 ├─ JourneyPatternRef/@ref
 ├─ LineRef/@ref
 ├─ FlexibleLineRef/@ref
 ├─ OperatorRef/@ref
 ├─ dayTypes
 │    └─ DayTypeRef/@ref (0..*)
 ├─ passingTimes
 │    └─ TimetabledPassingTime (1..*)
 │          ├─ @id
 │          ├─ StopPointInJourneyPatternRef/@ref
 │          ├─ ArrivalTime
 │          ├─ DepartureTime
 │          ├─ ArrivalDayOffset
 │          ├─ DepartureDayOffset
 │          ├─ EarliestDepartureTime
 │          └─ LatestArrivalTime
 ├─ keyList
 │    └─ KeyValue (0..*)
 └─ parts
      └─ JourneyPart (0..*)
 └─ BlockRef/@ref

| Element | Type | MIN | ERP | NP | Description |
|---|---|---:|:--:|:--:|---|
| ServiceJourney/@id | xsd:ID | 1..1 |  |  | Unique identifier following {CODESPACE}:ServiceJourney:{LocalId} |
| ServiceJourney/@version | xsd:string | 1..1 |  |  | Version label (e.g., "1"). Increment on changes. |
| Name | xsd:string | 0..1 |  |  | Human‑readable name of the journey |
| PrivateCode | xsd:normalizedString | 0..1 |  |  | Internal non‑public code (e.g., trip or train number) |
| Description | xsd:string | 0..1 |  |  | Free‑text description |
| TransportMode | TransportModeEnumeration | 0..1 |  |  | Public transport mode (e.g., bus, rail) |
| TransportSubmode/BusSubmode | BusSubmodeEnumeration | 0..1 |  |  | Submode for bus services |
| TransportSubmode/RailSubmode | RailSubmodeEnumeration | 0..1 |  |  | Submode for rail services |
| JourneyPatternRef/@ref | VersionedRef | 1..1 |  |  | Reference to a JourneyPattern that defines the stop sequence |
| LineRef/@ref | VersionedRef | 0..1 |  |  | Reference to the served Line |
| FlexibleLineRef/@ref | VersionedRef | 0..1 |  |  | Reference to a FlexibleLine (for on‑demand services) |
| OperatorRef/@ref | VersionedRef | 0..1 |  |  | Reference to an Operator |
| dayTypes/DayTypeRef/@ref | VersionedRef | 0..* |  |  | DayType(s) on which the journey operates |
| passingTimes/TimetabledPassingTime | TimetabledPassingTime | 1..* |  |  | Collection of scheduled passing/stop times |
| passingTimes/TimetabledPassingTime/@id | xsd:ID | 0..1 |  |  | Optional identifier for the TimetabledPassingTime element |
| passingTimes/TimetabledPassingTime/StopPointInJourneyPatternRef/@ref | VersionedRef | 1..1 |  |  | Reference to a StopPointInJourneyPattern in the JourneyPattern |
| passingTimes/TimetabledPassingTime/ArrivalTime | xsd:time | 0..1 |  |  | Planned arrival time at the stop |
| passingTimes/TimetabledPassingTime/DepartureTime | xsd:time | 0..1 |  |  | Planned departure time from the stop |
| passingTimes/TimetabledPassingTime/ArrivalDayOffset | xsd:integer | 0..1 |  |  | Day offset applied to ArrivalTime (e.g., 1 if arrival is on the next day) |
| passingTimes/TimetabledPassingTime/DepartureDayOffset | xsd:integer | 0..1 |  |  | Day offset applied to DepartureTime |
| passingTimes/TimetabledPassingTime/EarliestDepartureTime | xsd:time | 0..1 |  |  | Earliest pick‑up time (often used for flexible/on‑demand) |
| passingTimes/TimetabledPassingTime/LatestArrivalTime | xsd:time | 0..1 |  |  | Latest drop‑off time (often used for flexible/on‑demand) |
| keyList/KeyValue | KeyValue | 0..* |  |  | Arbitrary key/value metadata on the journey |
| parts/JourneyPart | JourneyPart | 0..* |  |  | Used for combined journeys or split/merge operations |
| BlockRef/@ref | VersionedRef | 0..1 |  |  | Reference to a Block or TrainBlock for vehicle working |

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
