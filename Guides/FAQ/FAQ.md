# Frequently Asked Questions

> A quick-reference Q&A for anyone encountering NeTEx, SIRI, or European public-transport data standards for the first time.

---

## The Standards in a Nutshell

### What is NeTEx?

**NeTEx** (Network Timetable Exchange) is a CEN Technical Standard ([CEN/TS 16614](https://www.transmodel-cen.eu/standards/)) for exchanging public-transport **planned data** as XML. It covers three broad areas:

| Part | Scope | Key objects |
|------|-------|-------------|
| **Part 1 – Network** | Stops, lines, routes, journey patterns | `StopPlace`, `Line`, `Route`, `ServiceJourneyPattern` |
| **Part 2 – Timetable** | Journeys, calendars, vehicle schedules | `ServiceJourney`, `DayType`, `Block` |
| **Part 3 – Fares** | Tariffs, fare products, sales | `FareZone`, `FareProduct`, `SalesOfferPackage` |

### What is SIRI?

**SIRI** (Service Interface for Real-Time Information, [CEN/TS 15531](https://www.transmodel-cen.eu/standards/)) is the real-time counterpart to NeTEx. Where NeTEx describes the **plan** ("Bus 42 is _scheduled_ to depart at 08:15"), SIRI tells you **what is happening now** ("Bus 42 is running 3 minutes late").

| SIRI service | Purpose |
|--------------|---------|
| **ET** – Estimated Timetable | Real-time arrival/departure predictions |
| **SM** – Stop Monitoring | Departures from a specific stop |
| **VM** – Vehicle Monitoring | Live vehicle positions |
| **SX** – Situation Exchange | Disruption and incident messages |
| **PT** – Production Timetable | Near-real-time timetable updates |

SIRI messages reference NeTEx identifiers (`LineRef`, `StopPointRef`, `DatedVehicleJourneyRef`), so consuming SIRI normally requires familiarity with the planned NeTEx data.

### What is Transmodel?

[Transmodel](https://transmodel-cen.eu/) is the **conceptual reference model** (EN 12896) that defines the vocabulary and relationships NeTEx and SIRI are built on. Think of it as the "data dictionary": it defines concepts like _Journey_, _Stop_, _Line_, _DayType_ and the rules for how they relate. NeTEx is an XML serialisation of a subset of Transmodel.

### How does NeTEx relate to GTFS?

| Aspect | GTFS | NeTEx |
|--------|------|-------|
| Format | CSV (flat files in a ZIP) | XML |
| Scope | Basic schedules + fares | Full Transmodel scope (network, schedules, fares, accessibility, vehicle types, etc.) |
| Governance | Google-initiated, community-driven | CEN standards body (European) |
| Adoption | Global, de-facto for journey planners | EU regulatory standard |
| Real-time pair | GTFS-realtime (Protobuf) | SIRI (XML / JSON) |
| Expressiveness | Limited extensibility | Full inheritance, versioning, profiles |

**They are not competitors.** Many systems produce both formats. Some National Access Points convert NeTEx to GTFS automatically.

---

## Where to Find Things

### Where is the official XSD schema?

The official NeTEx XML Schema is maintained on GitHub:

- **Repository:** <https://github.com/NeTEx-CEN/NeTEx>
- **Schema entry point:** `xsd/NeTEx_publication.xsd` (for `PublicationDelivery` documents)
- **Alternative entry point:** `xsd/NeTEx_publication_noPTI.xsd` (same, without PTI code lists)

> [!TIP]
> This workspace includes a local copy of the XSD under the `XSD/` folder. See the [Tools Guide](/Guides/Tools/Tools_Guide.md) for editor setup instructions.

### Where is the official documentation?

| Resource | URL |
|----------|-----|
| NeTEx CEN GitHub (specs + XSD) | <https://github.com/NeTEx-CEN/NeTEx> |
| Transmodel website | <https://transmodel-cen.eu/> |
| SIRI CEN GitHub | <https://github.com/SIRI-CEN/SIRI> |
| NeTEx UML diagrams | Included in the CEN GitHub under `doc/` |
| EU EPIP (European Passenger Information Profile) | <https://data4pt-project.eu/> |
| Nordic NeTEx Profile | <https://enturas.atlassian.net/wiki/spaces/PUBLIC/overview> |
| French NeTEx Profile (_Profil France_) | <https://normes.transport.data.gouv.fr/> |
| DGITM interactive training (Livebook) | <https://github.com/etalab/netex-france-formation/> |

### Where can I find real NeTEx data?

Most EU Member States publish NeTEx data through their **National Access Point (NAP)** as required by [EU Delegated Regulation 2017/1926](https://eur-lex.europa.eu/eli/reg_del/2017/1926/oj). Here are the major ones:

| Country | NAP | NeTEx available | URL |
|---------|-----|-----------------|-----|
| Norway | Entur | Yes (Nordic Profile) | <https://developer.entur.org/> |
| France | transport.data.gouv.fr | Yes (Profil France) | <https://transport.data.gouv.fr/> |
| UK | BODS | Yes (EPIP-based) | <https://data.bus-data.dft.gov.uk/> |
| Netherlands | NDOV / openOV | Yes | <https://ndovloket.nl/> |
| Finland | Fintraffic / Digitransit | Yes (Nordic Profile variant) | <https://www.fintraffic.fi/en/fintraffic/open-data> |
| Sweden | Trafiklab | Yes | <https://www.trafiklab.se/> |
| Germany | DELFI / NAP-DE | Yes (NeTEx-DE) | <https://www.opendata-oepnv.de/> |
| Switzerland | opentransportdata.swiss | Yes | <https://opentransportdata.swiss/> |
| Belgium | TEC / SNCB | Partial | Various regional portals |
| EU aggregator | EU NAP status overview | — | <https://transport.ec.europa.eu/transport-themes/intelligent-transport-systems/road/action-plan-and-directive/national-access-points_en> |

> [!NOTE]
> Data formats and profiles vary by country. Always check which NeTEx profile a dataset follows (EPIP, Nordic, French, etc.) before parsing.

---

## Validation

### How do I do a simple XSD validation?

The fastest path on any OS:

**1. Using `xmllint` (pre-installed on most Linux/macOS):**

```bash
xmllint --noout --schema path/to/xsd/NeTEx_publication.xsd your_file.xml
```

**2. Using Python + lxml:**

```python
from lxml import etree

schema = etree.XMLSchema(etree.parse("path/to/xsd/NeTEx_publication.xsd"))
doc = etree.parse("your_file.xml")

if schema.validate(doc):
    print("Valid ✓")
else:
    for error in schema.error_log:
        print(error)
```

**3. In VS Code:**

Install the [XML extension by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml), point `xml.fileAssociations` at the NeTEx XSD, and get in-editor validation as you type.

> [!TIP]
> For a full walkthrough including CI pipeline setup, see the [Validation Guide](/Guides/Validation/Validation.md) and [Tools Guide](/Guides/Tools/Tools_Guide.md).

### What are the most common validation errors?

| Error | Cause | Fix |
|-------|-------|-----|
| `Element X is not expected` | Wrong element order (XML Schema uses `xs:sequence`) | Reorder child elements to match the XSD |
| `Element x not found` | Incorrect casing (`Stopplace` instead of `StopPlace`) | NeTEx is case-sensitive, use exact casing |
| `value is not valid` | Invalid enum value (e.g., `Bus` instead of `bus`) | Check the XSD for allowed values |
| `Missing child element` | A required element was omitted | Add the mandatory element |
| `xxx is not a valid value of the atomic type` | Type mismatch (e.g., text in a numeric field) | Check and fix the data type |

See the [Validation Guide](/Guides/Validation/Validation.md) for detailed examples with fixes.

---

## Profiles

### What is a NeTEx Profile?

NeTEx is deliberately broad. A **profile** constrains it to a specific use case or country by:

- Making some optional elements **mandatory**
- **Excluding** unused elements
- Fixing **ID format** conventions
- Specifying which **frames** are expected

### Which profiles exist?

| Profile | Scope | Maintained by |
|---------|-------|---------------|
| **EPIP** (European Passenger Information Profile) | EU-wide baseline for passenger information | EU / Data4PT |
| **Nordic Profile** | Norway, Sweden, Finland, … | Entur / Nordic countries |
| **Profil France** | France | Transport.data.gouv.fr / DGITM |
| **NeTEx-DE** | Germany | DELFI |
| **UK BODS Profile** | United Kingdom | DfT |
| **NL NeTEx Profile** | Netherlands | NDOV |

> [!NOTE]
> This documentation follows the **Nordic Profile (NP)** and the **European Reference Profile (ERP)** unless stated otherwise. See the [Get Started Guide](/Guides/GetStarted/GetStarted_Guide.md) for an introduction.

---

## Data Structure

### What is a `PublicationDelivery`?

Every NeTEx XML file is wrapped in a `PublicationDelivery` — the outermost envelope that carries metadata (who published, when, which participant) and the actual data in one or more **Frames**.

### What are Frames?

Frames group related NeTEx objects by domain:

| Frame | Contains |
|-------|----------|
| `ResourceFrame` | Organisations, responsibility sets, vehicle types, codespaces |
| `SiteFrame` | Stop places, parking, points of interest |
| `ServiceFrame` | Lines, routes, journey patterns, scheduled stop points, connections |
| `ServiceCalendarFrame` | Day types, operating periods, day-type assignments |
| `TimetableFrame` | Service journeys (the actual timetable), passing times |
| `VehicleScheduleFrame` | Blocks, vehicle schedules |
| `FareFrame` | Fare zones, tariffs, fare products, validity conditions |
| `SalesTransactionFrame` | Fare contracts, sales transactions |

Frames are typically wrapped in a `CompositeFrame` grouping them under a common `ValidityCondition`.

### How do NeTEx references work?

NeTEx objects link to each other through `Ref` elements. For example, a `ServiceJourney` references a `ServiceJourneyPattern` via `JourneyPatternRef`, which in turn references a `Route` via `RouteRef`, which references a `Line` via `LineRef`.

The reference chain for a timetable typically looks like:

```
ServiceJourney → ServiceJourneyPattern → Route → Line
                         ↓
              StopPointInJourneyPattern → ScheduledStopPoint
                                                ↓
                                    PassengerStopAssignment → StopPlace / Quay
```

See the [NeTEx Conventions Guide](/Guides/NeTExConventions/NeTEx_Conventions.md) for ID format and versioning rules.

---

## Working with NeTEx

### What tools do I need to get started?

At minimum:

1. **A text/XML editor** — VS Code (free) with the Red Hat XML extension is recommended
2. **The XSD schema** — Clone or download from [NeTEx-CEN/NeTEx](https://github.com/NeTEx-CEN/NeTEx)
3. **A sample file** — Download from any NAP listed above, or use the examples in this repository

For a complete setup guide, see the [Tools Guide](/Guides/Tools/Tools_Guide.md).

### Where do I go from here?

| I want to… | Read this |
|------------|-----------|
| Understand NeTEx from scratch | [Get Started Guide](/Guides/GetStarted/GetStarted_Guide.md) |
| Set up editing and validation tools | [Tools Guide](/Guides/Tools/Tools_Guide.md) |
| Learn NeTEx naming and ID conventions | [NeTEx Conventions](/Guides/NeTExConventions/NeTEx_Conventions.md) |
| Validate my XML files | [Validation Guide](/Guides/Validation/Validation.md) |
| Understand EU regulatory requirements | [Regulatory Compliance Guide](/Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md) |
| Parse NeTEx data as a developer | [Developer Quickstart](/Guides/DeveloperQuickstart/DeveloperQuickstart_Guide.md) |
| Build a journey planner or MaaS platform | [MaaS Consumers Guide](/Guides/MaaSConsumers/MaaSConsumers_Guide.md) |
| Validate and control NAP data as an authority | [MMTIS Control Authority Kit](/Guides/MMTISControlKit/MMTISControlKit_Guide.md) |
| Learn about stop infrastructure | [Stop Infrastructure Guide](/Guides/StopInfrastructure/StopInfrastructure_Guide.md) |
| Model fares | [Fare Modelling Guide](/Guides/FareModelling/FareModelling_Guide.md) |
