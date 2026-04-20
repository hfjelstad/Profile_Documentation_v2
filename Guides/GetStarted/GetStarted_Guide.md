# 🚀 Get Started with NeTEx

![Parent and child waiting for a train](../../assets/images/Holding_Your_Hand.png)

## 1. 🎯 Introduction

This guide is for anyone working with public transport data — whether you're a developer integrating timetable feeds, a data manager at a transport authority, or an analyst exploring how NeTEx structures information.

Public transport systems across Europe need to exchange planned data — timetables, stop infrastructure, fares, vehicle schedules — between authorities, operators, and journey planners. [NeTEx](https://github.com/NeTEx-CEN/NeTEx) provides a single, standardised XML format for all of this, eliminating custom integrations and making data interoperable across borders.

By the end of this guide, you'll understand where NeTEx comes from, how it's structured, and how to read a real NeTEx document.

In this guide you will learn:
- 🌍 What Transmodel is and how NeTEx implements it
- 📄 The anatomy of a NeTEx document
- 🏗️ How frames organize data into domains
- 🔍 How to read a real example step by step

---

## 2. 🌍 The Standards Family

NeTEx is one piece of a European standards ecosystem. Understanding where it fits helps you know what NeTEx covers — and what it doesn't.

### The Big Picture

NeTEx doesn't exist in isolation — it's part of a European standards family for public transport:

```mermaid
flowchart TD
    TM["<b>TRANSMODEL</b><br/>EN 12896 — Conceptual Reference Model<br/><i>Defines the concepts: Line, Journey,<br/>StopPlace, Operator, DayType…</i>"]

    TM -->|"implemented as XML by"| NeTEx
    TM -->|"implemented as XML by"| SIRI
    TM -->|"implemented as XML by"| OpRa

    NeTEx["<b>NeTEx</b><br/>CEN/TS 16614<br/><br/>Planned data:<br/>timetables, fares, stops"]
    SIRI["<b>SIRI</b><br/>CEN/TS 15531<br/><br/>Real-time data:<br/>vehicle positions,<br/>delays, alerts"]
    OpRa["<b>OpRa</b><br/>CEN, in dev.<br/><br/>Historical data:<br/>operational raw data,<br/>KPIs"]

    NeTEx -->|"profiled by"| PROF

    PROF["<b>Profile</b><br/><br/>Selects which NeTEx<br/>elements to use and how"]

    click TM "https://www.transmodel-cen.eu/" _blank
    click NeTEx "https://www.netex-cen.eu/" _blank
    click SIRI "https://www.siri-cen.eu/" _blank

    style TM fill:#0D47A1,stroke:#0D47A1,color:#fff
    style NeTEx fill:#1565C0,stroke:#1565C0,color:#fff
    style SIRI fill:#1976D2,stroke:#1976D2,color:#fff
    style OpRa fill:#1E88E5,stroke:#1E88E5,color:#fff
    style PROF fill:#42A5F5,stroke:#42A5F5,color:#fff
```

> [!TIP]
> Click any box to visit its standard. When you see a NeTEx element like `ServiceJourney`, it maps directly to the Transmodel concept of a "SERVICE JOURNEY". Transmodel defines the semantics, NeTEx defines the XML.

---

## 3. 📄 Anatomy of a NeTEx Document

Once you know the outer structure, every NeTEx file becomes predictable. Here's the pattern they all follow:

```mermaid
flowchart TD
    PD["<b>PublicationDelivery</b><br/><i>The envelope: who sent this, when?</i>"]
    DO["dataObjects"]
    CF["<b>CompositeFrame</b><br/><i>Groups all frames into one delivery</i>"]
    CS["codespaces<br/><i>Declares namespace prefixes, e.g. ERP</i>"]
    FR["frames"]

    RF["🏢 <b>ResourceFrame</b><br/>Organizations, operators"]
    SF["📍 <b>SiteFrame</b><br/>Stop places, facilities"]
    SCF["📅 <b>ServiceCalendarFrame</b><br/>Day types, calendars"]
    SVF["🚌 <b>ServiceFrame</b><br/>Lines, routes, patterns"]
    TF["🕐 <b>TimetableFrame</b><br/>Journeys, timetables"]
    VSF["🚃 <b>VehicleScheduleFrame</b><br/>Vehicle blocks"]
    FF["💰 <b>FareFrame</b><br/>Fares and tariffs"]

    PD --> DO --> CF
    CF --> CS
    CF --> FR
    FR --> RF
    FR --> SF
    FR --> SCF
    FR --> SVF
    FR --> TF
    FR --> VSF
    FR --> FF

    style PD fill:#0D47A1,stroke:#0D47A1,color:#fff
    style DO fill:#1565C0,stroke:#1565C0,color:#fff
    style CF fill:#1565C0,stroke:#1565C0,color:#fff
    style CS fill:#1976D2,stroke:#1976D2,color:#fff
    style FR fill:#1976D2,stroke:#1976D2,color:#fff
    style RF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style SF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style SCF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style SVF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style TF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style VSF fill:#42A5F5,stroke:#42A5F5,color:#fff
    style FF fill:#42A5F5,stroke:#42A5F5,color:#fff
```

### Key Concepts

**PublicationDelivery** is always the root element. It contains metadata (timestamp, participant) and wraps all data in `dataObjects`.

**CompositeFrame** groups multiple frames into a single delivery unit. Think of it as a "package" — all frames inside can reference each other.

**Frames** separate data by domain. Each frame type holds a specific kind of data. This separation means you can update timetables without touching stop data, or change fares without republishing routes.

For details, see the [CompositeFrame documentation](../../Frames/CompositeFrame/Description_CompositeFrame.md).

---

## 4. 🏗️ Frames and What They Contain

Each frame type owns a specific domain of transport data. You only include the frames your delivery needs.

| Frame | Transmodel Domain | What It Holds | Example Objects |
|-------|-------------------|---------------|-----------------|
| [ResourceFrame](../../Frames/ResourceFrame/Description_ResourceFrame.md) | Organizations | Shared resources used by all other frames | Operator, Authority, VehicleType |
| [SiteFrame](../../Frames/SiteFrame/Description_SiteFrame.md) | Fixed Objects | Physical infrastructure | StopPlace, Quay, Parking |
| [ServiceCalendarFrame](../../Frames/ServiceCalendarFrame/Description_ServiceCalendarFrame.md) | Calendar | When services operate | DayType, OperatingDay, OperatingPeriod |
| [ServiceFrame](../../Frames/ServiceFrame/Description_ServiceFrame.md) | Network | Route structure and stop assignments | Line, Route, JourneyPattern, ScheduledStopPoint |
| [TimetableFrame](../../Frames/TimetableFrame/Description_TimetableFrame.md) | Timetable | Journey scheduling | ServiceJourney, DatedServiceJourney |
| [VehicleScheduleFrame](../../Frames/VehicleScheduleFrame/Description_VehicleScheduleFrame.md) | Vehicle Planning | Vehicle assignments | Block, TrainBlock |
| [FareFrame](../../Frames/FareFrame/Description_FareFrame.md) | Fares | Pricing and products | FareZone, TariffZone |

> [!TIP]
> You don't need all frames in every delivery. A stop registry might only use SiteFrame. A timetable exchange might use ServiceCalendarFrame + ServiceFrame + TimetableFrame. Include only what's relevant.

---

![Getting on the bike](../../assets/images/getting_on_the_bike.png)

## 5. 🔍 Reading Your First Example

The best way to learn NeTEx is to read real XML. Let's walk through a minimal delivery with four frames and see how they connect:

📄 **Full file:** [Example_CompositeFrame.xml](../../Frames/CompositeFrame/Example_CompositeFrame.xml)

### The Envelope

```xml
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" version="2.0">
  <PublicationTimestamp>2026-03-18T00:00:00Z</PublicationTimestamp>
  <ParticipantRef>EuPro</ParticipantRef>
  <dataObjects>
    <CompositeFrame id="ERP:CompositeFrame:1" version="1">
```

- `PublicationDelivery` — always the root element, with the NeTEx namespace
- `ParticipantRef` — identifies who created this delivery
- `CompositeFrame` — wraps all frames; the `id` uses the format `Codespace:Type:Identifier`

> [!NOTE]
> All NeTEx identifiers follow the pattern `Codespace:ObjectType:Identifier` — for example `ERP:DayType:WKD` or `NP:ServiceJourney:15044`. The codespace declares who owns the data. See the [NeTEx Conventions guide](../NeTExConventions/NeTEx_Conventions.md) for the full rules.

### Shared Resources (ResourceFrame)

```xml
<ResourceFrame id="ERP:ResourceFrame:1" version="1">
  <organisations>
    <Authority id="ERP:Authority:AUT_001" version="1">
      <Name>Example Authority</Name>
    </Authority>
    <Operator id="ERP:Operator:OP_001" version="1">
      <Name>Example Operator</Name>
    </Operator>
  </organisations>
</ResourceFrame>
```

- **Authority** — the public body responsible for transport (Transmodel: AUTHORITY)
- **Operator** — the company running the vehicles (Transmodel: OPERATOR)
- Other frames reference these by `id` — they don't repeat the definitions

### Calendar (ServiceCalendarFrame)

```xml
<ServiceCalendarFrame id="ERP:ServiceCalendarFrame:1" version="1">
  <dayTypes>
    <DayType id="ERP:DayType:WKD" version="1">
      <Name>Weekdays</Name>
      <properties>
        <PropertyOfDay>
          <DaysOfWeek>Monday Tuesday Wednesday Thursday Friday</DaysOfWeek>
        </PropertyOfDay>
      </properties>
    </DayType>
  </dayTypes>
</ServiceCalendarFrame>
```

- **DayType** defines *when* services operate (Transmodel: DAY TYPE)
- Journeys reference DayTypes to say "I run on weekdays" without hardcoding dates

### Network (ServiceFrame)

```xml
<ServiceFrame id="ERP:ServiceFrame:1" version="1">
  <lines>
    <Line id="ERP:Line:L1" version="1">
      <Name>Line 1</Name>
      <PublicCode>1</PublicCode>
      <OperatorRef ref="ERP:Operator:OP_001"/>
    </Line>
  </lines>
</ServiceFrame>
```

- **Line** — a group of routes marketed as one service (Transmodel: LINE)
- `OperatorRef` points back to the ResourceFrame — this is how frames cross-reference

### Timetable (TimetableFrame)

```xml
<TimetableFrame id="ERP:TimetableFrame:1" version="1">
  <vehicleJourneys>
    <ServiceJourney id="ERP:ServiceJourney:SJ_001" version="1">
      <Name>Morning departure</Name>
      <dayTypes>
        <DayTypeRef ref="ERP:DayType:WKD"/>
      </dayTypes>
      <LineRef ref="ERP:Line:L1"/>
    </ServiceJourney>
  </vehicleJourneys>
</TimetableFrame>
```

- **ServiceJourney** — a planned trip (Transmodel: SERVICE JOURNEY)
- `DayTypeRef` links to the calendar, `LineRef` links to the network
- Everything connects through references, never by duplicating data

### How the References Connect

```mermaid
flowchart LR
    SJ["ServiceJourney"] -->|LineRef| L["Line"]
    SJ -->|DayTypeRef| DT["DayType"]
    L -->|OperatorRef| OP["Operator"]

    subgraph TimetableFrame
        SJ
    end
    subgraph ServiceFrame
        L
    end
    subgraph ServiceCalendarFrame
        DT
    end
    subgraph ResourceFrame
        OP
    end

    style SJ fill:#42A5F5,stroke:#42A5F5,color:#fff
    style L fill:#42A5F5,stroke:#42A5F5,color:#fff
    style DT fill:#42A5F5,stroke:#42A5F5,color:#fff
    style OP fill:#42A5F5,stroke:#42A5F5,color:#fff
```

This is the core pattern in NeTEx: objects live in their own frame and connect through `*Ref` elements. Data is defined once and referenced everywhere.

---

## 6. 🧭 Where to Go Next

You now have the foundation — here's where to go depending on what you need.

**Deepen your understanding:**

- [NeTEx Conventions](../NeTExConventions/NeTEx_Conventions.md) — casing, IDs, versioning
- [Separation of Concerns](../SeparationOfConcerns/SeparationOfConcerns.md) — how domains stay independent
- [Calendar Guide](../Calendar/Calendar_Guide.md) — DayType, OperatingDay, exceptions
- [Table of Contents](../../LLM/Indexes/TableOfContent.md) — browse all frames and objects

**Start working:**

- [Tools Guide](../Tools/Tools_Guide.md) — editors, plugins, and validation setup
- [Validation Guide](../Validation/Validation.md) — validate XML against the schema
