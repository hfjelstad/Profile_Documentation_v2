# 🚌 Transport Modes — Reference Guide

## 1. 🎯 Introduction

NeTEx defines a two-level classification for transport: a **TransportMode** (primary mode) and a **TransportSubmode** (detailed variant). This system supports all European public transport types, from urban buses to cable cars to ferry services.

This guide provides the complete enumeration of modes and submodes as defined in the NeTEx XSD, with guidance on correct usage.

---

## 2. 📋 Mode/Submode Reference

### Bus

| Submode | Description |
|---------|-------------|
| `localBus` | Standard urban/suburban bus |
| `regionalBus` | Inter-city bus within a region |
| `expressBus` | Long-distance express service |
| `nightBus` | Service operating only during night hours |
| `postBus` | Combination postal/passenger service |
| `specialNeedsBus` | Accessible transport for special needs |
| `mobilityBus` | On-demand mobility service |
| `mobilityBusForRegisteredDisabled` | Registered disabled service |
| `sightseeingBus` | Tourist sightseeing service |
| `shuttleBus` | Short-distance shuttle |
| `highFrequencyBus` | High-frequency urban corridor service |
| `dedicatedLaneBus` | Bus using dedicated lanes (BRT-like) |
| `schoolBus` | Service for school transport |
| `schoolAndPublicServiceBus` | Combined school and public service |
| `railReplacementBus` | Temporary bus replacing rail service |
| `demandAndResponseBus` | On-demand, flexible route bus |
| `airportLinkBus` | Dedicated airport connection |

### Rail

| Submode | Description |
|---------|-------------|
| `local` | Local/suburban rail |
| `highSpeedRail` | High-speed long-distance trains |
| `suburbanRailway` | Suburban/commuter rail |
| `regionalRail` | Regional inter-city rail |
| `interregionalRail` | Long-distance rail between regions |
| `longDistance` | Long-distance national rail |
| `international` | International cross-border rail |
| `sleeperRailService` | Overnight sleeper trains |
| `nightRail` | Night rail services |
| `carTransportRailService` | Rail services carrying cars |
| `touristRailway` | Heritage/tourist railway |
| `airportLinkRail` | Dedicated airport rail connection |
| `railShuttle` | Short-distance rail shuttle |
| `replacementRailService` | Temporary replacement service |
| `specialTrainService` | Special event/charter train |
| `crossCountryRail` | Cross-country express |

### Water

| Submode | Description |
|---------|-------------|
| `internationalCarFerry` | International car-carrying ferry |
| `nationalCarFerry` | National car-carrying ferry |
| `regionalCarFerry` | Regional car-carrying ferry |
| `localCarFerry` | Local/fjord car ferry |
| `internationalPassengerFerry` | International passenger-only ferry |
| `nationalPassengerFerry` | National passenger-only ferry |
| `regionalPassengerFerry` | Regional passenger-only ferry |
| `localPassengerFerry` | Local/harbour passenger ferry |
| `postBoat` | Combination postal/passenger boat |
| `trainFerry` | Ferry carrying trains |
| `roadFerryLink` | Road-connected ferry link |
| `highSpeedPassengerService` | High-speed catamaran/hydrofoil |
| `highSpeedVehicleService` | High-speed car ferry |
| `sightseeingService` | Tourist/sightseeing boat |
| `riverBus` | Scheduled river bus |
| `shuttleFerryService` | Short-distance shuttle ferry |

### Tram

| Submode | Description |
|---------|-------------|
| `cityTram` | Urban tramway |
| `localTram` | Local/suburban tram |

### Metro

| Submode | Description |
|---------|-------------|
| `metro` | Standard metro/underground |
| `tube` | Deep-level tube (UK-style) |
| `urbanRailway` | Urban light metro |

### Air

| Submode | Description |
|---------|-------------|
| `domesticFlight` | Domestic scheduled flight |
| `helicopterService` | Scheduled helicopter service |
| `internationalFlight` | International scheduled flight |

### Coach

| Submode | Description |
|---------|-------------|
| `internationalCoach` | International coach service |
| `nationalCoach` | National long-distance coach |
| `shuttleCoach` | Short-distance coach shuttle |
| `regionalCoach` | Regional coach service |
| `specialCoach` | Special event coach |
| `schoolCoach` | School transport coach |
| `sightseeingCoach` | Tourist coach |
| `touristCoach` | Long-distance tourist coach |
| `commuterCoach` | Daily commuter coach |

### Telecabin (Cable Transport)

| Submode | Description |
|---------|-------------|
| `telecabin` | Aerial gondola/cable car |
| `cableCar` | Cable car on tracks |
| `lift` | Inclined elevator/lift |
| `chairLift` | Open chair lift |
| `dragLift` | Drag/button lift |
| `telecabinLink` | Connection telecabin |

### Funicular

| Submode | Description |
|---------|-------------|
| `funicular` | Standard funicular railway |
| `streetCableCar` | Street-running cable car (San Francisco-style) |
| `allFunicularServices` | All funicular service types |

---

## 3. 🔗 Where Modes Are Used

Transport modes appear on several objects:

| Object | Element | Purpose |
|--------|---------|---------|
| [Line](../../Objects/Line/Table_Line.md) | `TransportMode` + `TransportSubmode` | Classifies the line's primary service type |
| [StopPlace](../../Objects/StopPlace/Table_StopPlace.md) | `TransportMode` | Defines which mode(s) serve the stop |
| [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) | `TransportMode` | Overrides the line mode for a specific journey |
| [Operator](../../Objects/Operator/Table_Operator.md) | `PrimaryMode` | The operator's primary service mode |
| [Connection](../../Objects/Connection/Table_Connection.md) | `From/TransportMode`, `To/TransportMode` | Mode filter on connection endpoints |

---

## 4. 💡 Usage Rules

> [!WARNING]
> **Only one submode element per TransportSubmode container.** The submode type must match the parent TransportMode. For example, if TransportMode is `bus`, only `BusSubmode` should appear inside TransportSubmode.

**Correct:**
```xml
<TransportMode>bus</TransportMode>
<TransportSubmode>
  <BusSubmode>regionalBus</BusSubmode>
</TransportSubmode>
```

**Incorrect:**
```xml
<TransportMode>bus</TransportMode>
<TransportSubmode>
  <RailSubmode>local</RailSubmode>  <!-- WRONG: rail submode on a bus line -->
</TransportSubmode>
```

> [!TIP]
> If no submode is relevant, omit TransportSubmode entirely — it is always optional. Don't use a "generic" submode just to fill the element.

---

## 5. 🗺️ Mode Mapping to GTFS

For interoperability with GTFS:

| NeTEx TransportMode | GTFS route_type |
|---------------------|-----------------|
| `tram` | 0 |
| `metro` | 1 |
| `rail` | 2 |
| `bus` | 3 |
| `water` | 4 |
| `telecabin` | 6 |
| `funicular` | 7 |
| `coach` | 200 (extended) |
| `air` | 1100 (extended) |

> [!NOTE]
> GTFS extended route types provide more granular mapping. The Nordic profile recommends using submode values for accurate GTFS conversion.
