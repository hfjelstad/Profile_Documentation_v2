# DatedServiceJourney – Lifecycle (Conceptual)

This note explains how a planned journey becomes a dated, operational instance and how reinforcement/replacement works in practice.

## Overview
- **ServiceJourney**: Planned/template journey (pattern, stop sequence via JourneyPattern).
- **OperatingDay**: A concrete **calendar date**.
- **DatedServiceJourney**: The *realisation* of a ServiceJourney on a specific **OperatingDay**.
- **Reinforcement/Replacement**: Indicated with `ServiceAlteration` and a `replacedJourneys` list containing one or more `DatedVehicleJourneyRef`.

## Flow
```
[Plan]
  ServiceJourney ---------------------> (instantiated on a date) ---------------------> DatedServiceJourney
                                              |                                                     |
                                              | optional operational linkage                        | optional
                                              v                                                     v
                                          Block / TrainBlock                    replacedJourneys -> DatedVehicleJourneyRef (0..*)
```

## Typical Scenarios
1. **Planned operation**: A regular trip occurs on its intended day: `ServiceAlteration=planned` (or omitted).
2. **Extra capacity**: An additional trip is added: `ServiceAlteration=extraJourney` and `replacedJourneys` containing one or more `DatedVehicleJourneyRef` pointing to base dated journeys.
3. **Replacement**: An existing dated journey is replaced: `ServiceAlteration=replaced` with `replacedJourneys` listing the dated journey(s) being replaced.

> **Identifier stability**: The `ref` inside `DatedVehicleJourneyRef` may continue to point to identifiers in the form `ERP:DatedServiceJourney:*` to preserve backward compatibility.

## Validation Hints
- Ensure `ServiceJourneyRef` and `OperatingDayRef` are present and resolvable in the same `TimetableFrame`.
- Choose `ServiceAlteration` consistently with the operational intent; default is `planned`.
- Use `replacedJourneys` + `DatedVehicleJourneyRef` to make reinforcement/replacement explicit; resolve each `ref` to a valid dated journey identifier.
