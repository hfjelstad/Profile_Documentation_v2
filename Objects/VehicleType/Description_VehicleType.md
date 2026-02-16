# VehicleType

**Definition:**
A VehicleType represents a typified vehicle configuration (model or series), not an individual physical vehicle. It aggregates reusable properties such as capacity, dimensions, technical characteristics, and accessibility features that can be referenced across multiple journeys and vehicles in the fleet.

## Key Characteristics
- **Identification:** `id`, `version`, `Name`, `ShortName`, `Description`
- **Capacity:** Total passenger capacity and optional breakdown by class
- **Dimensions and Weight:** `length`, `width`, `height`, `weight`
- **Technical Attributes:** `selfPropelled`, `fuelType`, `euroClass`
- **Accessibility and Boarding:** `LowFloor`, `Lift`, `Ramp`, `Hoist`, `StepHeight`, `BoardingHeight` (LengthType), `GapToPlatform` (LengthType)

## Design Principles
- **Generic Nature:** VehicleType is designed to be generic and reusable. It must not include individual identifiers (e.g., registration number, VIN) or line-specific details.
- **Separation of Concerns:** VehicleType should be defined in a `ResourceFrame` and referenced from `ServiceJourney` or `VehicleJourney` via `VehicleTypeRef` (0..1). This ensures that vehicle characteristics are separated from route and timetable data.
- **Contextual Data:** Platform-specific or stop-specific attributes (e.g., actual gap measurements) belong to StopPlace/Quay objects, not VehicleType.

## Usage
- Define VehicleType once and reuse it across multiple journeys.
- Keep it free from operator branding, line-specific attributes, or infrastructure details.

