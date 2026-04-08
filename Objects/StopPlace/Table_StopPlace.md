## Structure Overview

```text
StopPlace (Monomodal)
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ ValidBetween (0..1)
 ├─ keyList (0..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 ├─ PrivateCode (0..1)
 ├─ Centroid (0..1)
 ├─ AccessibilityAssessment (0..1)
 │  ├─ MobilityImpairedAccess (1..1)
 │  └─ limitations (0..1)
 │     └─ AccessibilityLimitation (1..n)
 │        ├─ WheelchairAccess (0..1)
 │        └─ StepFreeAccess (0..1)
 ├─ TopographicPlaceRef/@ref (0..1)
 ├─ ParentSiteRef/@ref (0..1)
 ├─ TransportMode (1..1)
 ├─ OtherTransportModes (0..1)
 ├─ tariffZones (0..n)
 ├─ StopPlaceType (0..1)
 ├─ Weighting (0..1)
 ├─ placeEquipments (0..1)
 ├─ adjacentSites (0..1)
 │  └─ SiteRef/@ref (1..n)
 └─ quays (1..n)
```

## Table

| Element | Type | XSD | ERP | NP | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier (e.g., ERP:StopPlace:1001) | StopPlace/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version number | StopPlace/@version |
| @created | DateTime | 0..1 |  |  | Creation date | StopPlace/@created |
| @changed | DateTime | 0..1 |  |  | Last modification date | StopPlace/@changed |
| @modification | String | 0..1 |  |  | Modification type (e.g., delete for decommissioning) | StopPlace/@modification |
| ValidBetween | Period | 0..1 |  | 0..1 | Validity period (FromDate, ToDate) | StopPlace/ValidBetween |
| KeyValue | KeyValue | 0..n |  | 0..n | Alternative keys (e.g., external IDs) | StopPlace/keyList/KeyValue |
| Name | String | 0..1 | 1..1 | 1..1 | Name of the stop place | StopPlace/Name |
| AlternativeName | String | 0..1 |  |  | Alternative names or aliases | StopPlace/alternativeNames/AlternativeName |
| Description | String | 0..1 |  |  | Free-text description of the stop place | StopPlace/Description |
| PrivateCode | String | 0..1 |  |  | Internal identifier code | StopPlace/PrivateCode |
| Centroid | Location | 0..1 | 0..1 | 0..1 | Geographic point representation | StopPlace/Centroid/Location |
| AccessibilityAssessment | Element | 0..1 |  | 0..1 | Accessibility evaluation of the stop place | StopPlace/AccessibilityAssessment |
| MobilityImpairedAccess | Enum | 0..1 |  | 1..1 | Overall mobility access status (true, false, unknown) | StopPlace/AccessibilityAssessment/MobilityImpairedAccess |
| limitations | Container | 0..1 |  | 0..1 | Collection of specific accessibility limitations | StopPlace/AccessibilityAssessment/limitations |
| AccessibilityLimitation | Element | 0..n |  | 1..n | Specific accessibility limitation assessment | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation |
| WheelchairAccess | Enum | 0..1 |  | 0..1 | Wheelchair accessibility (true, false, unknown) | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation/WheelchairAccess |
| StepFreeAccess | Enum | 0..1 |  | 0..1 | Step-free access availability (true, false, unknown) | StopPlace/AccessibilityAssessment/limitations/AccessibilityLimitation/StepFreeAccess |
| [TopographicPlace](../TopographicPlace/Table_TopographicPlace.md)@ref | Reference | 0..1 |  | 0..1 | Reference to city or region | StopPlace/TopographicPlaceRef/@ref |
| ParentSiteRef/@ref | Reference | 0..1 | 0..1 |  | Reference to multimodal parent StopPlace | StopPlace/ParentSiteRef/@ref |
| TransportMode | Enum | 0..1 | 1..1 | 1..1 | Primary mode (bus, rail, metro, tram, water, etc.) | StopPlace/TransportMode |
| BusSubmode / RailSubmode / ... | Enum | 0..1 |  |  | Optional submode category | StopPlace/BusSubmode |
| OtherTransportModes | String | 0..1 |  |  | Additional transport modes served | StopPlace/OtherTransportModes |
| TariffZoneRef/@ref | Reference | 0..n | 0..n |  | References to tariff zones | StopPlace/tariffZones/TariffZoneRef/@ref |
| StopPlaceType | Enum | 0..1 | 0..1 | 0..1 | Functional type (onstreetBus, railStation, metroStation, busStation, etc.) | StopPlace/StopPlaceType |
| Weighting | Enum | 0..1 |  | 0..1 | Interchange weighting (e.g., interchangeAllowed) | StopPlace/Weighting |
| placeEquipments | Container | 0..1 |  |  | Equipment installed at the stop place | StopPlace/placeEquipments |
| adjacentSites | Container | 0..1 |  |  | References to adjacent stop places | StopPlace/adjacentSites |
| SiteRef/@ref | Reference | 0..n |  |  | Reference to an adjacent StopPlace | StopPlace/adjacentSites/SiteRef/@ref |
| [Quay](../Quay/Table_Quay.md) | Quay | 0..n | 1..n | 1..n | Boarding/alighting positions (not on multimodal parent) | StopPlace/quays/Quay |
