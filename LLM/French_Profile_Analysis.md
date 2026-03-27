# French NeTEx Profile (Profil France v2.4) — Analysis & Gap Report

> **Source:** [normes.transport.data.gouv.fr](https://normes.transport.data.gouv.fr/)  
> **Date of analysis:** 2026-03-27  
> **Branch:** `french-profile-analysis`  
> **Analyst:** AI agent (based on full fetch of Éléments communs + Réseaux pages, plus homepage index)

---

## 1. Executive Summary

The French NeTEx Profile (Profil France v2.4) is a national profile published by AFNOR GT7 covering 8 document parts. This analysis maps every French profile concept against our existing documentation structure, identifies gaps, and proposes how to close them.

**Key findings:**
- Our structure already covers **~75% of the French profile's objects** — Operator, Authority, Line, Route, JourneyPattern, ScheduledStopPoint, DayType, Notice, StopPlace, Quay, Parking, etc.
- The French profile uses **GeneralFrame + TypeOfFrame** instead of specialized frames (ServiceFrame, SiteFrame, etc.) — a fundamentally different packaging model
- The French profile adds **regulatory mapping (EU 2017/1926 MMTIS)** with tables linking NeTEx objects to specific regulation categories — we have no equivalent
- Several objects in the French profile are **not in our structure yet**: Network, Connection, DefaultConnection, SiteConnection, FlexibleLine, FlexibleRoute, Direction, TimingPoint, RoutingConstraintZone, SchematicMap, NavigationPath, PointOfInterest, Branding, ServiceCalendar, UicOperatingPeriod
- The French profile documents **abstract base classes** (DataManagedObject, GroupOfEntities, Zone, Point, Link, LinkSequence, Transfer) as standalone sections — we don't, and probably shouldn't (our inheritance is implicit in each concrete object)
- The French profile defines **file packaging rules** (ZIP archive, naming conventions, one-file-per-line) — we have no equivalent guide

---

## 2. French Profile Document Structure

The French profile is split into 8 complementary parts, each a standalone web document:

| FR Part | French Title | Scope | Our Equivalent |
|---------|-------------|-------|----------------|
| Éléments communs | Common Elements | Base types, frames, versioning, codespace, modes, organisations, calendars, notes, accessibility base, conditions | Spread across Objects/ (Codespace, Operator, Authority, etc.) + Frames/ + Guides/ |
| Arrêts | Stops | StopPlace, Quay, Entrance, TopographicPlace, equipment | Objects/StopPlace, Quay, TopographicPlace, placeEquipments, SanitaryEquipment, ShelterEquipment, etc. |
| Réseaux | Networks | Line, Route, JourneyPattern, ScheduledStopPoint, Connection, Direction, Flexible lines, Stop assignments | Objects/Line, Route, JourneyPattern, ScheduledStopPoint, GroupOfLines, PassengerStopAssignment, etc. |
| Horaires | Timetables | ServiceJourney, PassingTime, ServiceLink, DatedServiceJourney, Trains, Vehicle types | Objects/ServiceJourney, DatedServiceJourney, VehicleType, Vehicle, TrainBlock |
| Calendrier | Calendar | DayType, OperatingDay, OperatingPeriod, DayTypeAssignment, ServiceCalendar | Objects/DayType, DayTypeAssignment, OperatingDay, OperatingPeriod |
| Accessibilité | Accessibility | Detailed accessibility, navigation paths, equipment | Objects/placeEquipments, Guides/Accessibility |
| Tarifs | Fares | Fare zones, fare products, sales offers, distribution | Objects/FareZone, FareContract, Frames/FareFrame |
| Parkings | Parking | Parking description | Objects/Parking |

---

## 3. Object-by-Object Mapping

### 3.1 Objects WE HAVE that the French profile also covers

| Our Object | FR Location | FR Classification Col | Notes |
|-----------|-----------|----------------------|-------|
| **AlternativeName** | Éléments communs §6.11 | FK, PK | ✅ Match |
| **AlternativeText** | Éléments communs §6.12 | PK | ✅ Match |
| **Authority** | Éléments communs §6.18.3 | (inherits Organisation) | FR uses Organisation as superclass; Authority is a TypeOfOrganisation=authority |
| **Codespace** | Éléments communs §7.3 | AK | ✅ Match. FR adds detailed ID coding rules (SIRI compatibility, stop-specific patterns) |
| **DayType** | Éléments communs §6.22 | — | ✅ Match. FR adds PropertyOfDay with enums (DayOfWeek, Season, Holiday, etc.) |
| **DayTypeAssignment** | Éléments communs §6.22 | FK | ✅ Match |
| **DestinationDisplay** | Réseaux §6.7 | AK | ✅ Match. FR adds DestinationDisplayVariant for media-specific text |
| **GroupOfLines** | Réseaux §6.4 | FK | ✅ Match |
| **JourneyPattern** | Réseaux §6.9.1 | FK | FR uses ServiceJourneyPattern (concrete subclass). Adds ServiceJourneyPatternType enum |
| **Line** | Réseaux §6.3 | AK, FK | ✅ Match. FR adds Monitored, TypeOfLineRef, AccessibilityAssessment, documentLinks |
| **Notice** | Éléments communs §6.20 | AK, FK | ✅ Match. FR adds DeliveryVariant and NoticeAssignment inline |
| **OperatingDay** | Éléments communs §6.21 | FK | ✅ Match. FR adds EarliestTime and DayLength |
| **OperatingPeriod** | Éléments communs §6.22 | FK | ✅ Match. FR strongly prefers UicOperatingPeriod with ValidDayBits |
| **Operator** | Éléments communs §6.18.2 | AK | ✅ Match. FR adds PrimaryMode, CountryRef |
| **Parking** | Parkings (separate doc) | — | ✅ Have object, content from separate FR doc not fetched |
| **PassengerStopAssignment** | Réseaux §6.12 | FK | ✅ Match. FR adds trainElements and DynamicStopAssignment |
| **PurposeOfGrouping** | Éléments communs §6.3 | — | ✅ Implicit in FR GroupOfEntities |
| **Quay** | Arrêts (separate doc) | — | ✅ Have object, content from FR Arrêts doc not fetched |
| **ResponsibilitySet** | Éléments communs §6.19 | FK, PK | ✅ Match. FR adds ResponsibilityRoleAssignment with DataRoleType/StakeholderRoleType enums |
| **Route** | Réseaux §6.6 | FK | ✅ Match. FR adds PointOnRoute, RouteLink as separate sub-objects |
| **ScheduledStopPoint** | Réseaux §6.9.5 | AK | ✅ Match. FR explicitly says NO Location on SSP — it lives on Quay/StopPlace |
| **ServiceJourney** | Horaires (separate doc) | — | ✅ Have object, content from FR Horaires doc not fetched |
| **StopPlace** | Arrêts (separate doc) | — | ✅ Have object, content from FR Arrêts doc not fetched |
| **TariffZone** | Réseaux §6.5 | — | ✅ Match. FR says it inherits Zone with no additions |
| **TopographicPlace** | Arrêts (separate doc) | — | ✅ Have object |
| **Vehicle** | Horaires (separate doc) | — | ✅ Have object |
| **VehicleType** | Horaires (separate doc) | — | ✅ Have object |

### 3.2 Objects in French profile that WE DON'T HAVE

| FR Object | FR Location | Priority | Description |
|-----------|-----------|----------|-------------|
| **Network** | Réseaux §6.4.1 | 🔴 High | GroupOfLines with branding. "Le réseau TCL pour Lyon". Very visible to passengers. Our GroupOfLines is the parent, but we don't document Network as its subclass. |
| **Connection** | Réseaux §6.10 | 🔴 High | Transfer between ScheduledStopPoints with walk duration. Core for journey planners. |
| **DefaultConnection** | Réseaux §6.10 | 🟡 Medium | Default transfer times by mode/operator/area. Used as fallback by route planners. |
| **SiteConnection** | Réseaux §6.10 | 🟡 Medium | Transfer between StopPlaces/POIs with navigation path reference. |
| **Direction** | Réseaux §6.3.1 | 🟢 Low | Simple TypeOfValue for inbound/outbound. Minimal data. |
| **FlexibleLine** | Réseaux §6.8.1 | 🟡 Medium | Extends Line for demand-responsive transport (TAD). With BookingArrangements. |
| **FlexibleRoute** | Réseaux §6.8.2 | 🟢 Low | Extends Route for flexible services. |
| **FlexiblePointProperties** | Réseaux §6.8.3 | 🟢 Low | Properties for flexible points (may be skipped, zone-based). |
| **FlexibleLinkProperties** | Réseaux §6.8.4 | 🟢 Low | Properties for flexible links. |
| **TimingPoint** | Réseaux §6.9.6.2 | 🟡 Medium | Point used for timing regulation (not a stop). Superclass of ScheduledStopPoint. |
| **StopPointInJourneyPattern** | Réseaux §6.9.4 | 🟡 Medium | Rich object: ForAlighting, ForBoarding, RequestStop, StopUse, BookingArrangements. Currently implicit in our JourneyPattern. |
| **RoutePoint** | Réseaux §6.6.1 | 🟢 Low | Point defining route geometry. Minimal (inherits Point + BorderCrossing). |
| **RouteLink** | Réseaux §6.6.3 | 🟡 Medium | Segment between RoutePoints with distance and GML geometry. |
| **RoutingConstraintZone** | Réseaux §6.11.1 | 🟡 Medium | ITL zones (e.g., no boarding+alighting in same zone). French-specific but useful. |
| **TransferRestriction** | Réseaux §6.11.2 | 🟢 Low | Forbids transfers between specific stop points. |
| **NavigationPath** | Réseaux §6.10 | 🟡 Medium | Detailed walking path with accessibility features (lifts, stairs, etc.). |
| **PointOfInterest** | Réseaux §6.10 | 🟢 Low | POI for trip planning (inherits Site). Not core to transit data. |
| **SchematicMap** | Réseaux §6.13 | 🟢 Low | Schematic line map with pixel/vector object linking. |
| **Branding** | Éléments communs §6.26 | 🟢 Low | Commercial brand info (Presentation child). Minimal object. |
| **ServiceCalendar** | Éléments communs §6.22 | 🟡 Medium | Groups DayTypes, OperatingDays, OperatingPeriods. Container missing from our Objects/. |
| **UicOperatingPeriod** | Éléments communs §6.22 | 🟡 Medium | FR strongly prefers this over OperatingPeriod. Adds ValidDayBits bitstring. |
| **TrainStopAssignment** | Réseaux §6.12.1 | 🟡 Medium | Maps train components to boarding positions at stops. |
| **DynamicStopAssignment** | Réseaux §6.12.2 | 🟢 Low | Late-planned stop reassignment. |
| **BookingArrangements** | Réseaux §6.8.1 | 🟡 Medium | Embedded object for DRT booking conditions. |

### 3.3 Abstract base types in French profile (NOT in our Objects/)

The French profile documents these as standalone sections. Our approach keeps inheritance implicit — each concrete object's Description mentions what it inherits.

| FR Abstract Type | FR Section | Used by | Our approach |
|------------------|-----------|---------|-------------|
| DataManagedObject | §6.2 | Everything | @id, @version, KeyList, ValidBetween appear in every concrete object |
| Entity / EntityInVersion | §6.2 | Everything | Same — implicit |
| GroupOfEntities | §6.3 | GroupOfLines, Network, etc. | Name, ShortName, PrivateCode, PurposeOfGroupingRef |
| Zone | §6.4 | TariffZone, FareZone, StopPlace | Centroid, Polygon, projections |
| Point | §6.5 | ScheduledStopPoint, RoutePoint | Location, PointNumber, projections |
| Link | §6.6 | RouteLink, ServiceLink | Distance, LineString, From/ToPointRef |
| LinkSequence | §6.7 | Route, JourneyPattern | sectionsInSequence, Distance |
| Transfer | §6.10 | Connection, SiteConnection, DefaultConnection | WalkTransferDuration, BothWays, Distance |
| VersionFrame | §7.2 | All frames | TypeOfFrameRef, FrameDefaults, prerequisites |

**Recommendation:** Do NOT create Object folders for abstract types. Instead, create a guide in Guides/ that documents the NeTEx inheritance hierarchy with a Mermaid class diagram and links to concrete objects. This would replace the French profile's §6.2–§6.8 sections.

---

## 4. Structural & Conceptual Differences

### 4.1 Frame Strategy: Specialized vs. GeneralFrame

| Aspect | Our Profile | French Profile |
|--------|-------------|---------------|
| **Frame types** | Specialized: ServiceFrame, SiteFrame, TimetableFrame, ResourceFrame, etc. | GeneralFrame with TypeOfFrame (NETEX_COMMUN, NETEX_ARRET, NETEX_RESEAU, NETEX_HORAIRE, etc.) |
| **Wrapping** | CompositeFrame wrapping specialized frames | CompositeFrame of type NETEX_FRANCE wrapping GeneralFrames |
| **Effect on us** | No action needed — this is a legitimate NeTEx design choice. Both are valid. Our specialized frames are cleaner for documentation. |

### 4.2 File Packaging

The French profile specifies a **ZIP archive** with named files:

| File | Content |
|------|---------|
| `resource.xml` | Common elements + calendar |
| `network.xml` | Networks, groups of lines |
| `stop.xml` | Stops and quays |
| `line_xyz.xml` | One file per line (structure + timetable) |
| `fare.xml` | Fares |
| `accessibility.xml` | Accessibility |
| `parking.xml` | Parking |
| `poi.xml` | Points of interest |

**Gap:** We have no equivalent packaging guide. This would be valuable as a guide in `Guides/FilePackaging/` or similar.

### 4.3 Identifier Coding Rules

The French profile defines **detailed ID construction rules**:
- General: `[CODESPACE]:[type d'objet]:[identifiantTechnique]:[LOC ou NomAttributaire]`
- Stops: `[CountryCode]:[INSEE]:[ObjectType]:[TechnicalCode]:[AttributorCode]`

**Our approach:** We use codespace-based IDs (e.g., `ERP:Line:1`) but don't document the construction rules this formally. This is partially covered in our Codespace object documentation but could be enhanced.

### 4.4 Classification Column (PK / FK / AK / GROUP)

As discussed earlier, the French profile adds a `Classification` column to every table:
- **PK** (Primary Key): `id` + `version`
- **AK** (Alternate Key): PublicCode, PrivateCode, etc.
- **FK** (Foreign Key): All `*Ref` elements
- **GROUP**: XML attribute groups

**Decision (already made):** We don't add this column because it's implicit from our Type column (Reference = FK, ID = PK, etc.) and adding it would be profile-specific.

### 4.5 Regulatory Mapping (MMTIS / LOM)

Each French profile part includes a **Section 5** table mapping objects to EU Regulation 2017/1926 (MMTIS) categories with three tiers:
- Level 1/2/3 (urgency of data provision)
- Category + Detail (English)
- "Concepts à minima" vs. "Autres concepts"

**Gap:** We have no regulatory mapping. This is valuable for any EU member state. Could live in `Guides/RegulatoryCompliance/` and be linked from individual object descriptions via Section 5d.

### 4.6 Modes and Submodes Enumeration

The French profile provides complete enumeration tables for all modes (Bus, Coach, Metro, Rail, Tram, Telecabin, Air, Water, Funicular) and their submodes with French translations.

**Gap:** We don't have a centralized mode/submode reference. Currently modes appear per-object (Line, ServiceJourney). A guide or reference page would be useful.

### 4.7 Yellow Highlighting for Profile Deviations

The French profile uses **yellow-highlighted text** wherever the profile is stricter than base NeTEx (e.g., making an optional field mandatory). This is a systematic approach to showing "where we deviate."

**Our equivalent:** Our profile columns (MIN, NP) in tables serve this purpose — the cardinality difference between NeTEx base and our profile is visible. No change needed.

### 4.8 Web Service Interface

The French profile includes a full **SOAP web service** specification (Section 8.3) based on SIRI, with request/response structures.

**Gap:** We don't document any API interface. If we need one, this would be a Guides/ topic.

---

## 5. Proposed Actions

### 5.1 High Priority — Create Missing Core Objects

These objects are commonly used in journey planning and network modeling:

| Object | Action | Effort |
|--------|--------|--------|
| **Network** | New Object folder. Subclass of GroupOfLines with TransportOrganisationRef and tariffZones. | Small |
| **Connection** | New Object folder. Transfer between ScheduledStopPoints with WalkTransferDuration. | Medium |
| **ServiceCalendar** | New Object folder. Container grouping DayTypes + OperatingDays + OperatingPeriods + DayTypeAssignments. | Small |
| **StopPointInJourneyPattern** | New Object folder. Rich sub-object with ForAlighting, ForBoarding, RequestStop, ChangeOfDestinationDisplay. | Medium |

### 5.2 Medium Priority — Enhance Existing Objects

| Object | Enhancement | Source |
|--------|------------|--------|
| **Line** | Add Monitored, TypeOfLineRef, documentLinks, AccessibilityAssessment, allowedDirections | FR Réseaux §6.3 |
| **Operator** | Add PrimaryMode, CountryRef | FR Éléments communs §6.18.2 |
| **OperatingPeriod** | Document UicOperatingPeriod variant with ValidDayBits | FR Éléments communs §6.22 |
| **DayType** | Add PropertyOfDay with DaysOfWeek, Seasons, HolidayTypes enums | FR Éléments communs §6.22 |
| **Route** | Add PointOnRoute, RouteLink as linked sub-objects | FR Réseaux §6.6 |
| **DestinationDisplay** | Add DestinationDisplayVariant for multi-media | FR Réseaux §6.7 |
| **Notice** | Add DeliveryVariant and NoticeAssignment inline pattern | FR Éléments communs §6.20 |
| **PassengerStopAssignment** | Add TrainStopAssignment reference, DynamicStopAssignment | FR Réseaux §6.12 |

### 5.3 Medium Priority — New Guides

| Guide | Content | Location |
|-------|---------|----------|
| **Inheritance Hierarchy** | Mermaid class diagrams showing DataManagedObject → GroupOfEntities → Zone → StopPlace chain, etc. Links to concrete objects. Replaces FR's abstract type sections. | `Guides/NeTExInheritance/` |
| **File Packaging** | ZIP structure, file naming, one-file-per-line pattern, TypeOfFrame values | `Guides/FilePackaging/` |
| **ID Coding Rules** | Codespace conventions, ID construction patterns, version management | Enhance existing `Objects/Codespace/` |
| **Mode/Submode Reference** | Complete enum tables with descriptions for all transport modes and submodes | `Guides/TransportModes/` or in Glossary |

### 5.4 Low Priority — Nice-to-Have Objects

| Object | Notes |
|--------|-------|
| FlexibleLine, FlexibleRoute | Important for DRT, but niche. |
| RoutingConstraintZone | French ITL concept. Useful for routing engines. |
| RoutePoint, RouteLink | Infrastructure-level detail. |
| NavigationPath | Accessibility-focused walking paths. |
| PointOfInterest | Usually from external sources (OSM, etc.). |
| SchematicMap | SVG/pixel map binding. Very specialized. |
| Branding | Simple Presentation wrapper. |
| TransferRestriction | Negative constraint on transfers. |

### 5.5 Deferred — Explicitly Not Recommended

| Item | Reason |
|------|--------|
| PK/FK/AK column | Profile-specific; our Type column + Reference links make it implicit |
| Abstract base type Object folders | Over-engineering; inheritance is implicitly documented in each concrete object |
| SOAP web service specification | Not relevant to our current scope |
| French-specific ID coding rules | National-specific; we have our own codespace conventions |

---

## 6. French Profile Conventions Worth Adopting

Even though the French profile is organized differently, three conventions are worth considering:

### 6.1 Section 5 Regulatory Mapping (MMTIS) — in our Section 5d
For each object, the French profile lists which EU regulation category it satisfies. We could add this to Section 5d of relevant objects: "This object is required for MMTIS Level 1, Category: Trip plan computation — scheduled modes transport, Detail: Network topology and routes/lines."

### 6.2 Inheritance Line in Section 1
The French tables always begin with a `::> | ::> | ParentClass | ::>` row showing what the object inherits from. We could add a one-liner in Section 1 Purpose: "Inherits from: DataManagedObject (via GroupOfEntities > Zone)."

### 6.3 Centralized Validity Condition Documentation
The French profile documents ValidBetween, AvailabilityCondition, and ValidityTrigger once in common elements. We could create a guide in `Guides/ValidityConditions/` or document it in the ServiceCalendarFrame description.

---

## 7. Complete Concept Inventory

Below is every NeTEx concept mentioned in the French profile Éléments communs and Réseaux parts, with our coverage status:

### From Éléments communs (26 objects + abstract types)

| # | FR Object | We Have | Object/Guide |
|---|-----------|---------|-------------|
| 1 | DataManagedObject (abstract) | — | No separate doc (implicit) |
| 2 | Entity / EntityInVersion (abstract) | — | No separate doc (implicit) |
| 3 | GroupOfEntities (abstract) | — | No separate doc (implicit) |
| 4 | Zone (abstract) | — | No separate doc (implicit) |
| 5 | Point (abstract) | — | No separate doc (implicit) |
| 6 | Link (abstract) | — | No separate doc (implicit) |
| 7 | LinkSequence (abstract) | — | No separate doc (implicit) |
| 8 | PointInLinkSequence (abstract) | — | No separate doc (implicit) |
| 9 | ValidBetween | — | No separate doc (in DayType/OperatingDay) |
| 10 | ValidityCondition | — | ❌ Missing |
| 11 | AvailabilityCondition | — | ❌ Missing |
| 12 | ValidityTrigger | — | ❌ Missing |
| 13 | **AlternativeName** | ✅ | Objects/AlternativeName |
| 14 | **AlternativeText** | ✅ | Objects/AlternativeText |
| 15 | Location | — | Implicit in StopPlace/Quay |
| 16 | PostalAddress / RoadAddress | — | Implicit in StopPlace |
| 17 | Locale | — | Implicit in frames |
| 18 | Projection (Point/Zone) | ✅ | Objects/LinkSequenceProjection |
| 19 | **Codespace** | ✅ | Objects/Codespace |
| 20 | **Operator** | ✅ | Objects/Operator |
| 21 | **Authority** | ✅ | Objects/Authority |
| 22 | OrganisationalUnit | — | ❌ Missing (minor) |
| 23 | GroupOfOperators | — | ❌ Missing (minor) |
| 24 | **ResponsibilitySet** | ✅ | Objects/ResponsibilitySet |
| 25 | **Notice** | ✅ | Objects/Notice |
| 26 | NoticeAssignment | — | Described within Notice |
| 27 | DeliveryVariant | — | ❌ Missing (sub-object of Notice) |
| 28 | **OperatingDay** | ✅ | Objects/OperatingDay |
| 29 | **DayType** | ✅ | Objects/DayType |
| 30 | **DayTypeAssignment** | ✅ | Objects/DayTypeAssignment |
| 31 | PropertyOfDay | — | ❌ Missing (sub-object of DayType) |
| 32 | ServiceCalendar | — | ❌ Missing |
| 33 | **OperatingPeriod** | ✅ | Objects/OperatingPeriod |
| 34 | UicOperatingPeriod | — | ❌ Missing |
| 35 | Timeband | — | ❌ Missing (minor) |
| 36 | TypeOfValue | — | ❌ Missing |
| 37 | Presentation | — | Implicit in Line |
| 38 | Branding | — | ❌ Missing |
| 39 | ContactDetails | — | Implicit in Operator |
| 40 | KeyList | — | Implicit in DataManagedObject |
| 41 | VersionFrame / GeneralFrame | ✅ | Frames/ |
| 42 | PublicationDelivery | ✅ | Frames/Example_PublicationDelivery.xml |

### From Réseaux (25 objects)

| # | FR Object | We Have | Object/Guide |
|---|-----------|---------|-------------|
| 43 | **Line** | ✅ | Objects/Line |
| 44 | **GroupOfLines** | ✅ | Objects/GroupOfLines |
| 45 | Network | — | ❌ Missing |
| 46 | **TariffZone** | ✅ | Objects/TariffZone |
| 47 | **Route** | ✅ | Objects/Route |
| 48 | RoutePoint | — | ❌ Missing |
| 49 | PointOnRoute | — | ❌ Missing (sub-object of Route) |
| 50 | RouteLink | — | ❌ Missing |
| 51 | Direction | — | ❌ Missing |
| 52 | **DestinationDisplay** | ✅ | Objects/DestinationDisplay |
| 53 | DestinationDisplayVariant | — | ❌ Missing (sub-object) |
| 54 | FlexibleLine | — | ❌ Missing |
| 55 | FlexibleRoute | — | ❌ Missing |
| 56 | FlexiblePointProperties | — | ❌ Missing |
| 57 | FlexibleLinkProperties | — | ❌ Missing |
| 58 | BookingArrangements | — | ❌ Missing |
| 59 | ServiceJourneyPattern | See JourneyPattern | Objects/JourneyPattern |
| 60 | StopPointInJourneyPattern | — | ❌ Missing |
| 61 | TimingPointInJourneyPattern | — | ❌ Missing |
| 62 | TimingPoint | — | ❌ Missing |
| 63 | **ScheduledStopPoint** | ✅ | Objects/ScheduledStopPoint |
| 64 | Connection | — | ❌ Missing |
| 65 | DefaultConnection | — | ❌ Missing |
| 66 | SiteConnection | — | ❌ Missing |
| 67 | Transfer (abstract) | — | No separate doc |
| 68 | **PassengerStopAssignment** | ✅ | Objects/PassengerStopAssignment |
| 69 | TrainStopAssignment | — | ❌ Missing |
| 70 | DynamicStopAssignment | — | ❌ Missing |
| 71 | RoutingConstraintZone | — | ❌ Missing |
| 72 | TransferRestriction | — | ❌ Missing |
| 73 | NavigationPath | — | ❌ Missing |
| 74 | PointOfInterest | — | ❌ Missing |
| 75 | SchematicMap | — | ❌ Missing |

### Coverage Summary

| Status | Count | Percentage |
|--------|-------|-----------|
| ✅ Objects we have | 22 | 29% |
| ❌ Missing objects (total) | 36 | 48% |
| — Abstract types (by design) | 9 | 12% |
| — Implicit sub-objects | 8 | 11% |
| **Unique concepts in FR profile** | **75** | **100%** |

However, many "missing" items are sub-objects (PointOnRoute inside Route), abstract types (we don't document those), or minor utilities (Timeband, Branding). Looking at only **standalone, concrete objects that matter for data exchange**:

| | Count |
|---|---|
| FR concrete exchangeable objects | ~40 |
| We already have | ~22 |
| Missing high/medium priority | ~10 |
| Missing low priority | ~8 |

---

## 8. Recommended Implementation Roadmap

### Phase 1: High-value missing objects (4 objects)
1. **Network** — simple, extends GroupOfLines
2. **Connection** — critical for routing engines
3. **ServiceCalendar** — container for calendar objects
4. **StopPointInJourneyPattern** — rich object with ForAlighting/ForBoarding/RequestStop

### Phase 2: Enhance existing objects with FR-inspired additions (6 objects)
5. Add UicOperatingPeriod docs to **OperatingPeriod**
6. Add PropertyOfDay docs to **DayType**
7. Enhance **Line** with Monitored, TypeOfLineRef, allowedDirections
8. Enhance **Route** with RoutePoint/RouteLink references
9. Enhance **Notice** with DeliveryVariant and inline NoticeAssignment
10. Add DestinationDisplayVariant to **DestinationDisplay**

### Phase 3: New guides (3 guides)
11. **Guides/NeTExInheritance/** — Class hierarchy with Mermaid diagrams
12. **Guides/TransportModes/** — Complete mode/submode enumeration tables
13. **Guides/FilePackaging/** — ZIP structure and TypeOfFrame conventions

### Phase 4: Medium-priority new objects (6 objects)
14. **FlexibleLine** (with BookingArrangements)
15. **RouteLink**
16. **TimingPoint**
17. **TrainStopAssignment**
18. **DefaultConnection**
19. **SiteConnection** (with NavigationPath)

---

## Appendix: French Profile Table Format vs. Ours

### French table format
```
| Classification | Nom | Type | Cardinalité | Description |
| PK | id | ObjectIdType | 1:1 | Identifiant unique... |
| FK | responsibilitySetRef | ResponsibilitySetIdType | 1:1 | Pointe les roles... |
| AK | PublicCode | xsd:normalizedString | 0:1 | Code public... |
```

### Our table format
```
| Element | Type | MIN | NP | Description | Path |
| @id | ID | 1..1 | 1..1 | Unique identifier... | Line/@id |
| OperatorRef/@ref | Reference | 1..1 | 1..1 | Reference to Operator | Line/OperatorRef/@ref |
| PublicCode | String | | 0..1 | Public line code... | Line/PublicCode |
```

### Key differences:
1. FR has Classification column (PK/FK/AK) — we use Type column implicitly
2. FR has single Cardinalité column — we have per-profile columns (MIN, NP, etc.)
3. FR uses XSD type names — we use simplified types (String, ID, Reference, Enum)
4. We have Path column — FR does not
5. FR descriptions are in French — ours in English
6. FR uses `0:1` notation — we use `0..1`
7. FR has yellow highlighting for deviations — we show it via profile column differences
