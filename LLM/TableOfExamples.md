# Table of Examples

This index lists example collections and their NeTEx 2.0 validation status.

DatedServiceJourney
- Objects/DatedServiceJourney/Table_DatedServiceJourney.md
- Cases and notes:
  - Example_DatedServiceJourney.xml — Fail (fragment; add PublicationDelivery envelope for XSD resolution)
  - Example_DatedServiceJourney_Extended_01_Reinforcement.xml — Fail (fragment; add envelope and appropriate frame)
  - Example_DatedServiceJourney_Extended_02_Replacement.xml — Fail (fragment; add envelope and appropriate frame)
  - Example_DatedServiceJourney_Extended_03_BlockLinked.xml — Fail (fragment; add envelope and appropriate frame)
  - Example_DatedServiceJourney_Extended_04_MultiRef.xml — Fail (fragment; add envelope and appropriate frame)

Line
- Objects/Line/Table_Line.md
- Cases and notes:
  - Example_Line.xml — Fail (fragment; wrap in PublicationDelivery + ServiceFrame and include a resolvable Operator in ResourceFrame for green validation). See Guides/Validation.md and Frames/Example_PublicationDelivery.xml.

See also: Guides/Validation.md for how to run schema validation locally.
