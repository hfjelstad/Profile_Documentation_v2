## Structure Overview

```text
Line
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ TransportMode (1..1)
 ├─ TransportSubmode (0..1)
 │  ├─ BusSubmode (0..1)
 │  ├─ RailSubmode (0..1)
 │  ├─ WaterSubmode (0..1)
 │  ├─ TramSubmode (0..1)
 │  ├─ MetroSubmode (0..1)
 │  ├─ AirSubmode (0..1)
 │  ├─ CoachSubmode (0..1)
 │  └─ TelecabinSubmode (0..1)
 ├─ PublicCode (0..1)
 ├─ PrivateCode (0..1)
 ├─ OperatorRef/@ref (1..1)
 ├─ RepresentedByGroupRef/@ref (0..1)
 └─ Presentation (0..1)
    ├─ Colour (0..1)
    └─ TextColour (0..1)
```

## Table

| Element | Type | XSD | ERP | NP | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the Line (e.g., ERP:Line:5) | Line/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | Line/@version |
| Name | String | 1..1 | 1..1 | 1..1 | Human-readable line name | Line/Name |
| TransportMode | Enum | 0..1 | 1..1 | 1..1 | Primary transport mode (bus, rail, water, tram, metro, air, coach, telecabin) | Line/TransportMode |
| TransportSubmode | Element | 0..1 |  | 0..1 | Transport submode container | Line/TransportSubmode |
| BusSubmode | Enum | 0..1 |  | 0..1 | Bus submode (localBus, regionalBus, expressBus, etc.) | Line/TransportSubmode/BusSubmode |
| RailSubmode | Enum | 0..1 |  |  | Rail submode (local, regionalRail, longDistance, etc.) | Line/TransportSubmode/RailSubmode |
| WaterSubmode | Enum | 0..1 |  |  | Water submode (localPassengerFerry, localCarFerry, etc.) | Line/TransportSubmode/WaterSubmode |
| TramSubmode | Enum | 0..1 |  |  | Tram submode (cityTram, localTram) | Line/TransportSubmode/TramSubmode |
| MetroSubmode | Enum | 0..1 |  |  | Metro submode | Line/TransportSubmode/MetroSubmode |
| AirSubmode | Enum | 0..1 |  |  | Air submode (domesticFlight, helicopterService) | Line/TransportSubmode/AirSubmode |
| CoachSubmode | Enum | 0..1 |  |  | Coach submode (internationalCoach, nationalCoach) | Line/TransportSubmode/CoachSubmode |
| TelecabinSubmode | Enum | 0..1 |  |  | Telecabin submode | Line/TransportSubmode/TelecabinSubmode |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | 0..1 | 1..1 | 1..1 | Reference to the Operator running this Line | Line/OperatorRef/@ref |
| PublicCode | String | 0..1 |  | 0..1 | Public-facing line number or code | Line/PublicCode |
| PrivateCode | String | 0..1 |  | 0..1 | Internal non-public code | Line/PrivateCode |
| RepresentedByGroupRef/@ref | Reference | 0..1 |  | 0..1 | Reference to the Network or GroupOfLines this line belongs to | Line/RepresentedByGroupRef/@ref |
| Colour | String | 0..1 | 0..1 | 0..1 | Line colour as 6-digit uppercase hex (e.g., 005EB8) | Line/Presentation/Colour |
| TextColour | String | 0..1 | 0..1 | 0..1 | Text colour as 6-digit uppercase hex (e.g., FFFFFF) | Line/Presentation/TextColour |
