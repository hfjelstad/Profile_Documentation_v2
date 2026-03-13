# NeTEx Example Objects – Overview and Validation Guidance

This document provides a concise overview of the example NeTEx XML objects included under the `Objects/` directory and explains how they relate to each other. It also outlines how to validate these examples against NeTEx 2.0 XSD.

Note: The examples are illustrative. Integrations must always be validated against the target profile and organizational constraints in addition to schema validation.

## Validation (NeTEx 2.0)
- All NeTEx examples in this repository are intended to comply with NeTEx version 2.0 XSD.
- Recommended workflow:
  1) Edit/update XML locally as needed.
  2) Validate the raw XML against the NeTEx 2.0 XSD.
  3) Resolve any schema or referential integrity issues before publishing.

## Object Summaries and Typical Relationships
Below is a short description of each example file and typical cross-references it participates in. Paths are relative to the repository root.

### 1) GroupOfLines
- Path: `Objects/GroupOfLines/Example_GroupOfLines.xml`
- Purpose: Groups two or more `Line` entities for reporting, publication, or operational grouping.
- Typical references: `Line` members by reference.

### 2) Interchange
- Path: `Objects/Interchange/Example_Interchange.xml`
- Purpose: Models a guaranteed or planned transfer between two `ServiceJourney` instances.
- Typical references: FromJourney/ToJourney (`ServiceJourney`), timing constraints, buffer times.

### 3) JourneyPattern
- Path: `Objects/JourneyPattern/Example_JourneyPattern.xml`
- Purpose: Defines the ordered sequence of `ScheduledStopPoint` occurrences for a service.
- Typical references: `Route` (sequence of `RoutePoint`s), `ScheduledStopPoint` (by reference), `Line` and `Operator` indirectly through enclosing structures.

### 4) Line
- Path: `Objects/Line/Example_Line.xml`
- Purpose: A public-facing line or service brand for passenger information.
- Typical references: `Operator`, `Route`/`JourneyPattern` (indirect), branding, presentation attributes.

### 5) Operator
- Path: `Objects/Operator/Example_Operator.xml`
- Purpose: Identifies the transport organization operating services.
- Typical references: Linked from `Line`, `ServiceJourney`, or `ResponsibilitySet` roles.

### 6) PassengerStopAssignment
- Path: `Objects/PassengerStopAssignment/Example_PassengerStopAssignment.xml`
- Purpose: Binds a passenger-boarding/alighting activity to a specific `Quay` within a `StopPlace` for a `ScheduledStopPoint`.
- Typical references: `ScheduledStopPoint`, `StopPlace`, `Quay`.

### 7) ResponsibilitySet
- Path: `Objects/ResponsibilitySet/Example_ResponsibilitySet.xml`
- Purpose: Assigns responsibilities (data ownership, maintenance) to parties over certain data scopes.
- Typical references: Parties (e.g., `Operator` or authority), scopes (lines, areas, datasets).

### 8) ResponsibilitySet (Contract-oriented)
- Path: `Objects/ResponsibilitySet/Example_ResponsibilitySet_Contract.xml`
- Purpose: Variant focused on contractual responsibilities, typically tied to concessions or service contracts.
- Typical references: Contract identifiers, authorities, `Operator`s, validity periods.

### 9) Route
- Path: `Objects/Route/Example_Route.xml`
- Purpose: Describes the physical path a service takes via an ordered set of points.
- Typical references: `Line`, `RoutePoint`s, alignment with `JourneyPattern` stop sequence.

### 10) ScheduledStopPoint
- Path: `Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml`
- Purpose: Logical stop occurrences used in timetables and journey patterns.
- Typical references: `StopPlace`/`Quay` via assignments, used by `JourneyPattern` and `ServiceJourney`.

### 11) ServiceJourney
- Path: `Objects/ServiceJourney/Example_ServiceJourney.xml`
- Purpose: A dated operational journey with times over a `JourneyPattern`.
- Typical references: `JourneyPattern`, time demand types, `Operator`, vehicle/`VehicleType`, `Interchange`.

### 12) Quay
- Path: `Objects/Quay/Example_Quay.xml`
- Purpose: A specific platform/stand within a `StopPlace` for boarding/alighting.
- Typical references: Linked from `PassengerStopAssignment`, contained by a `StopPlace`.

### 13) StopPlace
- Path: `Objects/StopPlace/Example_StopPlace.xml`
- Purpose: A passenger facility such as a station, stop, or terminal.
- Typical references: Contains one or more `Quay`s; linked by `PassengerStopAssignment`.

### 14) TrainBlock
- Path: `Objects/TrainBlock/Example_TrainBlock.xml`
- Purpose: Defines operational coupling of services (block working), typically for rail.
- Typical references: Sequences of `ServiceJourney`s operated as a linked block.

### 15) Vehicle
- Path: `Objects/Vehicle/Example_Vehicle.xml`
- Purpose: Represents a single physical vehicle with identifiers and attributes.
- Typical references: `VehicleType`, assigned to `ServiceJourney` or blocks; operational IDs.

### 16) VehicleType
- Path: `Objects/VehicleType/Example_VehicleType.xml`
- Purpose: Describes vehicle capabilities and classification (capacity, accessibility, features).
- Typical references: Referenced from `Vehicle` and sometimes planning elements.

## Typical Cross-Object Flow
- `StopPlace` contains `Quay`(s) → `PassengerStopAssignment` links a `ScheduledStopPoint` to a `Quay`.
- `Route` provides topology; `JourneyPattern` provides the stop sequence that aligns with the route.
- `ServiceJourney` runs over a `JourneyPattern` with dated times, operated by an `Operator`, and may be subject to `Interchange` constraints.
- `Vehicle` instances conform to a `VehicleType`; services may be grouped by `Line` and further by `GroupOfLines`.
- `ResponsibilitySet` clarifies who owns/maintains data for specific scopes or contracts.

## Versioning and Profile Notes
- Schema target: NeTEx 2.0. If organizational profiles impose stricter rules (e.g., ID schemes, mandatory attributes), ensure examples are adapted accordingly before validation and publication.

## Change Log
- 2026-03-11: Initial overview and validation guidance added.
