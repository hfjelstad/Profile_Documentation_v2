# Repository Navigation Guide (Table of Contents)

This table of contents is intended to help quickly navigate the documentation and resources in this repository.

Quick links:
- [Validate XML](#validate-xml)
- [Interchange only](#interchange-only)
- [Frames](#frames)
- [Objects](#objects)
- [Examples](#examples)

## Root
High-level entry points to the repository.
- [README.md](../README.md)
- [TableOfContents.md](TableOfContents.md) (you are here)

## Guides
How-to guides, conceptual overviews, and validation instructions.
- [README](../Guides/README.md) — overview of the guides section.
- [Get Started Guide](../Guides/GetStarted_Guide.md) — minimal steps to begin working with the profile.
- [Frames Overview](../Guides/FramesOverview.md) — explains the purpose and relationships of the various Frames.
- [Validation](../Guides/Validation.md) — how to validate NeTEx XML against schemas and rules.
- [Separation of Concerns](../Guides/SeparationOfConcerns.md) — clarifies responsibilities and boundaries between components.
- Interchange Only
  - [README](../Guides/InterchangeOnly/README.md) — scope and intent of the Interchange-only profile.
  - [Mandatory Interchange Guide](../Guides/InterchangeOnly/MandatoryInterchange_Guide.md) — required elements and constraints.

## Frames
Model-specific frame directories used to organize data and documentation.
- [FareFrame](../Frames/FareFrame/)
- [ResourceFrame](../Frames/ResourceFrame/)
- [ServiceCalendarFrame](../Frames/ServiceCalendarFrame/)
- [ServiceFrame](../Frames/ServiceFrame/)
- [SiteFrame](../Frames/SiteFrame/)
- [TimetableFrame](../Frames/TimetableFrame/)
- [VehicleScheduleFrame](../Frames/VehicleScheduleFrame/)

## Objects
Core NeTEx object categories, grouped for discoverability.
- [Authority](../Objects/Authority/)
- [Codespace](../Objects/Codespace/)
- [DatedServiceJourney](../Objects/DatedServiceJourney/)
- [DayType](../Objects/DayType/)
- [Interchange](../Objects/Interchange/)
- [JourneyPattern](../Objects/JourneyPattern/)
- [Line](../Objects/Line/)
- [Operator](../Objects/Operator/)
- [PassengerStopAssignment](../Objects/PassengerStopAssignment/)
- [Quay](../Objects/Quay/)
- [Route](../Objects/Route/)
- [ScheduledStopPoint](../Objects/ScheduledStopPoint/)
- [ServiceJourney](../Objects/ServiceJourney/)
- [StopPlace](../Objects/StopPlace/)
- [TrainBlock](../Objects/TrainBlock/)
- [Vehicle](../Objects/Vehicle/)
- [VehicleType](../Objects/VehicleType/)

## LLM
AI assistance materials and examples that complement the documentation.
- [Table of Examples](TableOfExamples.md) — prompt and response examples for common tasks.
- [Validated XML Example](Validatet_XML_Example.xml) — a small, valid NeTEx XML snippet for reference/testing.

## XSD 2.0
Schemas and related assets for validation and development.
- [README](../XSD%202.0/README.md) — overview of the XSD package.
- [Readme.md.htm](../XSD%202.0/Readme.md.htm) — HTML-rendered readme.
- [change_log.md](../XSD%202.0/change_log.md) — detailed change log.
- [CHANGELOG.md](../XSD%202.0/CHANGELOG.md) — alternative change log.
- [LICENSE](../XSD%202.0/LICENSE) — license information.
- [NeTEx.spp](../XSD%202.0/NeTEx.spp) — project file.
- [NeTEx.xpr](../XSD%202.0/NeTEx.xpr) — project file.
- [xsd/](../XSD%202.0/xsd/) — schema files.
- [examples/](../XSD%202.0/examples/) — sample data.
- [scripts/](../XSD%202.0/scripts/) — helper scripts.

## Continuous Integration
Automation for validating XML and ensuring quality.
- GitHub Actions: [validate-netex-xml.yml](../.github/workflows/validate-netex-xml.yml)

---

## Validate XML
- How-to: see [Validation guide](../Guides/Validation.md).
- Sample: use [Validated XML Example](Validatet_XML_Example.xml).
- CI: run or inspect [.github/workflows/validate-netex-xml.yml](../.github/workflows/validate-netex-xml.yml).
- Schemas: see [XSD folder](../XSD%202.0/xsd/).

## Interchange only
- Overview: [Interchange-only README](../Guides/InterchangeOnly/README.md).
- Mandatory fields: [Mandatory Interchange Guide](../Guides/InterchangeOnly/MandatoryInterchange_Guide.md).
- Related objects: [Interchange](../Objects/Interchange/) and [ServiceJourney](../Objects/ServiceJourney/).

## Examples
- Prompt and response examples for LLM: [Table of Examples](TableOfExamples.md).
