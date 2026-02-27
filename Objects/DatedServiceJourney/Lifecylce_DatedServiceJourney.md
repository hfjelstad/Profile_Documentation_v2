# DatedServiceJourney — Lifecycle

This document describes the lifecycle considerations for DatedServiceJourney in the ERP profile.

Scope of reference resolution
- ServiceJourneyRef (1..1) must resolve in the same dataset (PublicationDelivery), across frames within the same CompositeFrame.
- OperatingDayRef (1..1) must resolve in the same dataset (PublicationDelivery), across frames within the same CompositeFrame.
  Note: Cross-frame resolution is expected for OperatingDayRef because OperatingDay resides in ServiceCalendarFrame.

ServiceAlteration and replacements
- ServiceAlteration (0..1) indicates an alteration to the base ServiceJourney (e.g., extraJourney, cancellation, replacement).
- When ServiceAlteration = extraJourney (reinforcement), the DatedServiceJourney adds capacity in addition to the base plan.
- replacedJourneys (0..1) is recommended when ServiceAlteration = extraJourney to make replacement semantics explicit, but it remains optional.

Identifiers and codespace
- All identifiers should use the ERP codespace (e.g., ERP:SJ:..., ERP:OD:...) and be stable within the PublicationDelivery payload.
