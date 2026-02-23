# TrainBlock — Table

Context
- Frame: VehicleScheduleFrame
- Purpose: Rail-specific specialisation of Block used as operational grouping for a single train on a given operating day.

Key elements

| Element                                    | Cardinality | Type/Ref                  | Profile rule and notes |
|--------------------------------------------|-------------|---------------------------|------------------------|
| Block (TrainBlock in this profile)         | 1           | Block                     | Represented as a Block element with rail semantics (TrainBlock). Lives in VehicleScheduleFrame/blocks. |
| @id                                        | 1           | Identifier                | Globally unique within the dataset/context. Prefix with codespace (e.g., ERP:TrainBlock:…). |
| @version                                   | 1           | Version                   | Version of the Block/TrainBlock object. |
| Name                                       | 0..1        | xs:string                 | Human-readable label. |
| PublicCode                                 | 0..1        | xs:string                 | Short code for operational communication. |
| OperatorRef                                | 0..1        | OperatorRefStructure      | Reference to the operating organisation (optional). |
| Referenced by DatedServiceJourney.BlockRef | 0..1        | BlockRefStructure         | DatedServiceJourney may reference either a Block or a TrainBlock in this profile. |

XSD pointer
- DatedServiceJourney/BlockRef is of type BlockRefStructure in NeTEx and accepts references to Block (including the TrainBlock specialisation used by this profile).
- Typical path: PublicationDelivery/dataObjects/*Frame/vehicleJourneys/DatedServiceJourney/BlockRef

Cardinality and usage
- DatedServiceJourney.BlockRef: [0..1] — at most one per DatedServiceJourney.

Notes
- TrainBlock is a rail specialisation. Generic Block/VehicleBlock remain valid; TrainBlock narrows the semantics to rail operations.
