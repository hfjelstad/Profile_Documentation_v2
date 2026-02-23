# TrainBlock

Short definition and purpose
- TrainBlock is a rail-specific specialisation of a Block that represents an operational context for a single train. It may consist of one or more ServiceJourney or DatedServiceJourney instances that are operated as one operational run for a train on a given day.

Relationship to Block/VehicleBlock
- TrainBlock is a rail variant/subclass of Block in this profile. It can be used as the target of DatedServiceJourney.BlockRef. Generic Block (or VehicleBlock where applicable) remains valid; TrainBlock narrows the semantics to rail operations.

Cardinality and usage in the profile
- DatedServiceJourney.BlockRef [0..1] may reference either a Block or a TrainBlock. If provided, it identifies the operational grouping the journey belongs to for the operating day. Absence means the journey is not assigned to any operational block in the profile.

Key elements and references
- id (required): Stable identifier of the TrainBlock.
- version (required): Version of the TrainBlock object.
- Name (optional): Human-readable name.
- PublicCode (optional): Short code used for communication.
- OperatorRef (optional): Reference to the operating organisation.
- Associations: One or more ServiceJourney and/or DatedServiceJourney instances can reference the TrainBlock via BlockRef.

XSD pointer
- BlockRef element: DatedServiceJourney/BlockRef of type BlockRefStructure as defined by NeTEx (Public Transport Timetable and Scheduling). In this profile, BlockRef accepts references to Block or TrainBlock.
  Example path: PublicationDelivery/dataObjects/*Frame/vehicleJourneys/DatedServiceJourney/BlockRef

Minimal XML example
- See Objects/TrainBlock/Example_TrainBlock.xml for a minimal PublicationDelivery containing:
  a) A TrainBlock defined in a VehicleSchedulingFrame (with id and version), and
  b) A DatedServiceJourney that refers to the TrainBlock through BlockRef, with mandatory ServiceJourneyRef and OperatingDayRef supplied.

Validation rules and consistency checklist
- Id uniqueness: Every TrainBlock id must be globally unique within the dataset/context.
- Resolvable references: All BlockRef occurrences from DatedServiceJourney must resolve to either a Block or a TrainBlock that exists in the same PublicationDelivery or its referenced dataset.
- Version coherence: If versions are used for TrainBlock, ensure references point to compatible or intended versions.
- Profile rule: DatedServiceJourney.BlockRef cardinality is [0..1]. Do not include more than one BlockRef per DatedServiceJourney.

Common pitfalls and recommendations
- Reuse the same TrainBlock for contiguous train runs of the same physical train on the same operating day instead of creating many tiny blocks.
- Do not confuse TrainBlock (vehicle/operation-level grouping) with Duty (crew/roster-level assignment). They are different concepts and live in separate domains.
- For multi-day operations, use distinct TrainBlock instances per operating day or use dated blocks; avoid mixing days within a single TrainBlock.
