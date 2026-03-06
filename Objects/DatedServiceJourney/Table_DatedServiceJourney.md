# DatedServiceJourney – Table

The table below separates structural cardinality defined by the CEN NeTEx XSD from profile-specific constraints defined by ERP (European Recommended Profile). Use both columns together: XSD expresses what the schema allows; ERP expresses what the profile requires within those bounds.

| Field | Description | Type | Cardinality (XSD) | Cardinality (ERP) |
|---|---|---|---|---|
| id | Globally unique identifier of the DatedServiceJourney | Attribute | 1..1 | 1..1 |
| version | Version of the element instance | Attribute | 0..1 | 1..1 |
| Name | Human-readable name of the dated journey | Element | 0..1 | 0..1 |
| PrivateCode | Private operator code for the dated journey | Element | 0..1 | 0..1 |
| ServiceJourneyRef | Reference to the planned ServiceJourney instantiated on this date | Reference | 1..1 | 1..1 |
| OperatingDayRef | Reference to the OperatingDay this dated journey runs on | Reference | 1..1 | 1..1 |
| OperatorRef | Reference to the operating company for this dated journey | Reference | 0..1 | 0..1 |
| ResponsibilitySetRef | Reference to the responsibility set applicable to this dated journey | Reference | 0..1 | 0..1 |
| TrainBlockRef | Reference to a Block/Train grouping if applicable | Reference | 0..1 | 0..1 |
| NoticeAssignment | Notices linked to the dated journey | Collection | 0..n | 0..n |
| KeyList/Key | Key-value pairs for extensible metadata | Collection | 0..n | 0..n |

Notes
- Cardinality (XSD) reflects the structural constraints of the CEN NeTEx schema.
- Cardinality (ERP) reflects additional profile constraints and must be respected by ERP-compliant data producers.
- Descriptions are semantic; do not duplicate cardinality or requiredness in the Description column.
