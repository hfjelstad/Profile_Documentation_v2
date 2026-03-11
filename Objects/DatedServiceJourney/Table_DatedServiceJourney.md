# Table: DatedServiceJourney (DatedVehicleJourney)

This table lists attributes and elements observed across the three example inputs and maps their per-example cardinalities. Cells are left blank if the element/attribute is not present in that example file.

Sources considered:
- Example_DatedServiceJourney_MIN.xml (MIN)
- Example_DatedServiceJourney_ERP.xml (ERP)
- Example_DatedServiceJourney_NP.xml (NP)

Columns: Element | Type | MIN Cardinality | ERP Cardinality | NP Cardinality | Description

| Element | Type | MIN | ERP | NP | Description |
|---|---|---|---|---|---|
| @id | xsd:NMTOKEN | 1..1 | 1..1 | 1..1 | Unique identifier for the dated journey instance. |
| @version | xsd:integer |  | 1..1 | 1..1 | Version number of the object. |
| ServiceJourneyRef | ServiceJourneyRef | 1..1 | 1..1 | 1..1 | Reference to the underlying ServiceJourney template. |
| OperatingDayRef | OperatingDayRef | 1..1 | 1..1 | 1..1 | Reference to the OperatingDay that anchors the date of operation. |
| BlockRef | BlockRef |  | 0..1 | 0..1 | Reference to an operational Block/TrainBlock. |
| ServiceAlteration | ServiceAlterationEnumeration |  | 0..1 | 0..1 | Planned/replaced/extraJourney; omitted implies planned. |
| replacedJourneys | replacedJourneys |  |  | 0..1 | Container for references to journeys being replaced or reinforced. |
| replacedJourneys/DatedVehicleJourneyRef | DatedVehicleJourneyRef |  |  | 0..* | Reference(s) to dated journey(ies) being replaced/reinforced. |
| DatedCalls | DatedCalls |  |  |  | Container for one or more DatedCall elements (actual stop calls). |
| DatedCalls/DatedCall | DatedCall |  |  |  | A single call of the dated journey. |
| DatedCall/Order | xsd:positiveInteger |  |  |  | The call order in the journey. |
| DatedCall/StopPlaceRef | StopPlaceRef |  |  |  | Stop reference by StopPlace/Quay; alternative to StopPointInJourneyPatternRef. |
| DatedCall/StopPointInJourneyPatternRef | StopPointInJourneyPatternRef |  |  |  | Stop reference following the JourneyPattern; alternative to StopPlaceRef. |
| DatedCall/DepartureTime | xsd:time |  |  |  | Scheduled departure time at this call (if applicable). |
| DatedCall/ArrivalTime | xsd:time |  |  |  | Scheduled arrival time at this call (if applicable). |
