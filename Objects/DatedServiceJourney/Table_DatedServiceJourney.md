# DatedServiceJourney — Field Table

This table documents the key elements of DatedServiceJourney and their constraints as used in the ERP profile.

| Element | Cardinality | Description | Requirement |
|---|---|---|---|
| ServiceJourneyRef | 1..1 | Reference to the base ServiceJourney. | Must resolve in the same dataset (PublicationDelivery), across frames within the same CompositeFrame. |
| OperatingDayRef | 1..1 | Reference to the OperatingDay, which resides in ServiceCalendarFrame. | Must resolve in the same dataset (PublicationDelivery), across frames within the same CompositeFrame. Note: Cross-frame resolution is expected for OperatingDayRef. |
| ServiceAlteration | 0..1 | Indicates an alteration of the base service (e.g., extraJourney, cancellation, replacement). | When set to extraJourney (reinforcement), the journey is an addition to the base plan. |
| replacedJourneys | 0..1 | References journeys that are replaced by this DatedServiceJourney. | Recommended when ServiceAlteration = extraJourney to make replacement semantics explicit, but optional (0..1). |

Notes
- All references must be stable within the ERP codespace and use the ERP namespace (e.g., ERP:SJ:..., ERP:OD:...).
- The resolution scope for references is the PublicationDelivery payload, and references may cross frames as long as they are within the same CompositeFrame.
