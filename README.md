<!-- LLM AGENT: Use LLM/README.md as startingpoint  --> 
# NeTEx Profile Documentation

A practical reference, learning resource, and example library for working with NeTEx.

This repository is a human-friendly entry point to NeTEx: a place to learn the structure of the standard, explore real examples, and understand how frames and objects relate to each other in practice.

- 📘 **Learn** the concepts and structure of NeTEx
- 🧭 **Navigate** frames, objects, and modeling patterns
- 🗂️ **Explore** a high-quality example library validated against the official XSD
- 🔎 **Reference** element ordering, cardinality, and profile-specific requirements

---

## 📚 How to Use This Repository

### Start here

| Step | Where | What you'll find |
|------|-------|-----------------|
| 1 | [`Guides/`](Guides/GetStarted/GetStarted_Guide.md) | Conceptual overviews, conventions, and getting started material |
| 2 | [`Frames/`](Frames/CompositeFrame/Description_CompositeFrame.md) | How data is organized — each Frame groups related objects |
| 3 | [`Objects/`](Objects/Line/Description_Line.md) | Detailed reference for every NeTEx object with examples |

### Quick lookup

- 📋 [**Table of Contents**](LLM/Tables/TableOfContent.md) — Complete index of all Guides, Frames, and Objects
- 📄 [**Table of Examples**](LLM/Tables/TableOfExamples.md) — Every XML example with links and descriptions

---

## 🎯 What This Repository Contains

### 1. **Validated NeTEx examples**
Every XML example is:
- Validated against the NeTEx 2.0 XSD schema
- Designed to illustrate a single concept or object clearly
- Available in multiple profiles (see [Profiles](#-profiles) below)
- Built using the standard NeTEx delivery pattern:

```xml
PublicationDelivery → dataObjects → Frame → …
```

### 2. **Structured documentation per object**
For every frame and object, you will find three files:

| File | Purpose |
|------|---------|
| `Description_<Name>.md` | Purpose, structure overview, key elements, and relationships |
| `Table_<Name>.md` | Element-level specification with types, cardinality per profile, and XSD paths |
| `Example_<Name>_<Profile>.xml` | One or more validated XML examples |

### 3. **Guides**
Each guide lives in its own folder under `Guides/` and can include supporting files (diagrams, XML snippets, etc.):

| Guide | Description |
|-------|-------------|
| [GetStarted](Guides/GetStarted/GetStarted_Guide.md) | Minimal steps to begin working with the profile |
| [NeTExConventions](Guides/NeTExConventions/NeTEx_Conventions.md) | Casing rules, naming patterns, and a minimal example |
| [Glossary](Guides/Glossary/Glossary.md) | Terminology and definitions |
| [Tools](Guides/Tools/Tools_Guide.md) | Editors, plugins, validators, and development workflow |
| [Validation](Guides/Validation/Validation.md) | How to validate NeTEx XML against schemas and rules |
| [OrganisationalGovernance](Guides/OrganisationalGovernance/OrganisationalGovernance_Guide.md) | Authority, Operator, Contract, and ResponsibilitySet |
| [StopInfrastructure](Guides/StopInfrastructure/StopInfrastructure_Guide.md) | Logical stops, physical platforms, and the PassengerStopAssignment bridge |
| [JourneyLifecycle](Guides/JourneyLifecycle/JourneyLifecycle_Guide.md) | Line → Route → JourneyPattern → ServiceJourney → DatedServiceJourney |
| [Calendar](Guides/Calendar/Calendar_Guide.md) | DayType, OperatingPeriod, DayTypeAssignment, OperatingDay — when services operate |
| [Interchange](Guides/InterchangeOnly/Interchange_Guide.md) | Planned transfers, guaranteed connections, and interchangeOnly stops |
| [PassengerInformation](Guides/PassengerInformation/PassengerInformation_Guide.md) | DestinationDisplay, Notice, and FlexibleServiceProperties |
| [VehicleScheduling](Guides/VehicleScheduling/VehicleScheduling_Guide.md) | Blocks, VehicleType, Vehicle, and fleet assignment |
| [SeatingReservation](Guides/SeatingReservation/SeatingReservation_Guide.md) | Reservation policies, accommodation types, and train formations |
| [NetworkTimetable](Guides/NetworkTimetable/NetworkTimetable_Guide.md) | Producing and consuming NeTEx timetable datasets |
| [SeparationOfConcerns](Guides/SeparationOfConcerns/SeparationOfConcerns.md) | Domain separation, coupling strategies, and cross-frame patterns |
| [ExtendedSales & DeviationHandling](Guides/ExtendedSales_and_DeviationHandling/ExtendedSales_and_DeviationHandling_Guide.md) | Extended sales window, DatedServiceJourney.id as sales key, deviation handling |
| [Accessibility](Guides/Accessibility/Accessibility_Guide.md) | AccessibilityAssessment, equipment, and indoor navigation paths |
| [FareModelling](Guides/FareModelling/FareModelling_Guide.md) | Products, zones, tariffs, and sales offer packages |
| [DecisionMakers](Guides/DecisionMakers/DecisionMakers_Guide.md) | NeTEx overview for decision makers and stakeholders |
| [RegulatoryCompliance](Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md) | Delegated Regulation 2017/1926 requirements and NAP submission |
| [MaaSConsumers](Guides/MaaSConsumers/MaaSConsumers_Guide.md) | Consuming NeTEx datasets as a MaaS platform |

---

## 🏷️ Profiles

This repository documents three profiles, each representing a different level of detail:

| Profile | Code | Codespace | Description |
|---------|------|-----------|-------------|
| **Minimum** | `MIN` | `ERP` | Bare minimum elements required |
| **European Recommended** | `ERP` | `ERP` | Full European recommended profile |
| **Nordic** | `NP` | `NP` | Nordic-specific extensions and conventions |

Examples are named by profile: `Example_<Object>_MIN.xml`, `Example_<Object>_NP.xml`, etc.

### Codespace conventions

XML identifiers follow the pattern `<Codespace>:<ObjectType>:<Identifier>`:

```
ERP:DayType:WKD           ← European profile example
NP:ServiceJourney:15044   ← Nordic profile example
NSR:StopPlace:59977       ← Norwegian StopPlace Registry (stop infrastructure)
```

> `NSR` is reserved for stop infrastructure data (StopPlace, Quay, TopographicPlace) in Nordic Profile examples.

The `ParticipantRef` in all examples uses `EuPro` to identify this as European Profile documentation.

---

## 🗂️ Repository Structure

```
Root
├── Guides/                         → Conceptual guides (one folder per guide)
│     └── <GuideName>/
│          ├── <GuideName>.md
│          └── (optional supporting files)
│
├── Frames/                         → Frame-level documentation and examples
│     └── <FrameName>/
│          ├── Description_<FrameName>.md
│          ├── Table_<FrameName>.md
│          └── Example_<FrameName>.xml
│
├── Objects/                        → Object-level documentation and examples
│     └── <ObjectName>/
│          ├── Description_<ObjectName>.md
│          ├── Table_<ObjectName>.md
│          └── Example_<ObjectName>_<Profile>.xml
│
├── LLM/                            → Documentation conventions and indexes
│     ├── README.md                 → Rules and templates for documentation
│     ├── Tables/                   → Table of Contents + Table of Examples
│     ├── Templates/                → Templates for creating new documentation
│     └── AgentGuides/              → Operational guides for AI-assisted workflows
│
├── scripts/                        → Local validation tools
│     └── validate-xml.sh
│
└── .github/workflows/              → CI validation (PR + push)
```

---

## ✨ Interactive Features

The documentation site uses [Docsify](https://docsify.js.org/) with several plugins for an enhanced reading experience:

| Feature | Description |
|---------|-------------|
| **Flexible Alerts** | Styled `> [!WARNING]`, `> [!TIP]`, `> [!NOTE]` callout boxes |
| **Tabs** | `<!-- tabs:start -->` blocks for side-by-side MIN/NP profile examples |
| **Mermaid Diagrams** | Relationship graphs, tree structures, and flowcharts in guides |
| **Glossary Tooltips** | Hover any NeTEx term to see its definition (52-term glossary) |
| **Copy Code** | One-click copy button on every code/XML block |
| **Search** | Full-text search across all documentation |
| **Feedback** | Giscus comment widget at the bottom of every page |

---

## 🧱 Conventions

### File naming

| Type | Pattern | Example |
|------|---------|---------|
| XML examples | `Example_<Name>_<Profile>.xml` | `Example_Line_MIN.xml` |
| Descriptions | `Description_<Name>.md` | `Description_Line.md` |
| Tables | `Table_<Name>.md` | `Table_Line.md` |

### XML structure principles

- Collections use `lowerCamelCase` (`dataObjects`, `vehicleJourneys`, `pointsInSequence`)
- Type elements use `UpperCamelCase` (`ServiceJourney`, `StopPlace`)
- `*Ref` elements express relationships between objects
- Element order must match the NeTEx XSD sequence (inherited elements first)
- Time values use timezone-aware `xs:dateTime` → `2026-02-25T14:22:00Z`
- All examples are validated against the official [NeTEx XSD](https://github.com/NeTEx-CEN/NeTEx) (`NeTEx_publication.xsd`)

---

## ✅ Validation

All XML examples in this repository are validated against the official NeTEx XSD schema, both locally and in CI.

| Method | How |
|--------|-----|
| **Local (bash)** | `./scripts/validate-xml.sh` |
| **Local (changed only)** | `./scripts/validate-xml.sh --changed` |
| **CI (pull request)** | Automatic via `PR_Validator.yml` |
| **CI (push)** | Automatic via `Commit_Validator.yml` on `EnStandardBranch` |

See the [Validation guide](Guides/Validation/Validation.md) for detailed instructions.

---

## ✨ About This Project

This project exists to make NeTEx easier to understand and apply by providing:
- Clear, structured documentation for every object and frame
- A rich library of validated examples across multiple profiles
- Conceptual guides for newcomers and practitioners alike
- Consistent conventions that make the standard predictable and navigable

Whether you're encountering NeTEx for the first time or looking up a specific element's cardinality, this repository is designed to get you to the answer quickly.
