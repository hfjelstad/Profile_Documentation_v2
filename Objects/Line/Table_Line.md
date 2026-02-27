# Line – NeTEx 2.0 Validation Status

Validation summary
- Entry point schema: XSD 2.0/xsd/NeTEx_publication_timetable.xsd
- Codespace used in examples: ERP
- How to validate: see Guides/Validation.md
- Example envelope: Frames/Example_PublicationDelivery.xml

Pass/Fail table (per example)

| Example | Result | Notes |
|---|---|---|
| Objects/Line/Example_Line.xml | Fail | XML fragment; not a complete PublicationDelivery/ServiceFrame. For a green check, wrap inside a PublicationDelivery with a ServiceFrame that contains the Line, and include a resolvable Operator in a ResourceFrame. See Guides/Validation.md and Frames/Example_PublicationDelivery.xml. |

Changelog
- 2026-02-27: Added validation status row for Example_Line.xml.
