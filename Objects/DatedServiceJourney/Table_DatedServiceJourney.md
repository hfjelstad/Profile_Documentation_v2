# Table: DatedServiceJourney (DatedVehicleJourney)

This table lists attributes and elements observed across the three example inputs and maps their per-example cardinalities. Cells are left blank if the element/attribute is not present in that example file.

Sources considered:
- Example_DatedServiceJourney_MIN.xml (MIN)
- Example_DatedServiceJourney_ERP.xml (ERP)
- Example_DatedServiceJourney_NP.xml (NP)

Columns: Element | Type | MIN Cardinality | ERP Cardinality | NP Cardinality | Description

| Element | Type | MIN Cardinality | ERP Cardinality | NP Cardinality | Description |
|---|---|---|---|---|---|
| @id | xsd:NMTOKEN | 1..1 | 1..1 | 1..1 | Unique identifier for the dated journey instance. |
| @version | xsd:integer |  | 1..1 | 1..1 | Version number of the object. |
| ServiceJourneyRef | ServiceJourneyRef | 1..1 | 1..1 | 1..1 | Reference to the underlying ServiceJourney template. |
| OperatingDayRef | OperatingDayRef | 1..1 | 1..1 | 1..1 | Reference to the OperatingDay that anchors the date of operation. |
| BlockRef | BlockRef |  | 0..1 | 0..1 | Reference to an operational Block/TrainBlock. |
| ServiceAlteration | ServiceAlterationEnumeration |  | 0..1 | 0..1 | Planned/replaced/extraJourney; omitted implies planned. |
| replacedJourneys | replacedJourneys |  |  | 0..1 | Container for references to journeys being replaced or reinforced. |
| replacedJourneys/DatedVehicleJourneyRef | DatedVehicleJourneyRef |  |  | 0..* | Reference(s) to dated journey(ies) being replaced/reinforced. |
| DatedCalls | DatedCalls |  | 1..* | 1..* | Container for one or more DatedCall elements (actual stop calls). |
| DatedCalls/DatedCall | DatedCall |  | 1..* | 1..* | A single call of the dated journey. |
| DatedCall/Order | xsd:positiveInteger |  | 1..1 | 1..1 | The call order in the journey. |
| DatedCall/StopPlaceRef | StopPlaceRef |  | 0..1 | 0..1 | Stop reference by StopPlace/Quay; alternative to StopPointInJourneyPatternRef. |
| DatedCall/StopPointInJourneyPatternRef | StopPointInJourneyPatternRef |  | 0..1 | 0..1 | Stop reference following the JourneyPattern; alternative to StopPlaceRef. |
| DatedCall/DepartureTime | xsd:time |  | 0..1 | 0..1 | Scheduled departure time at this call (if applicable). |
| DatedCall/ArrivalTime | xsd:time |  | 0..1 | 0..1 | Scheduled arrival time at this call (if applicable). |
