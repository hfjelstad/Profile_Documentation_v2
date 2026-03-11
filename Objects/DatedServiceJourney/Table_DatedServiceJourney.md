# Table: DatedServiceJourney

| Element | Type | MIN Cardinality | ERP Cardinality | NP Cardinality | Description |
|---|---|---|---|---|---|
| @id | xsd:NMTOKEN | 1..1 | 1..1 | 1..1 | Unique identifier of the DatedServiceJourney within its codespace. |
| @version | xsd:integer | 1..1 | 1..1 | 1..1 | Version number of the DatedServiceJourney object. |
| ServiceJourneyRef | ServiceJourneyRef | 1..1 | 1..1 | 1..1 | Reference to the generic ServiceJourney from which journey details (e.g., JourneyPatternRef, passingTimes) are derived. |
| OperatingDayRef | OperatingDayRef | 1..1 | 1..1 | 1..1 | Reference to the OperatingDay that specifies the date this DatedServiceJourney runs. |