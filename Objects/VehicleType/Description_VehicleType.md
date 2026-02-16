# VehicleType

## Overview
VehicleType describes a typified vehicle configuration (not a single physical vehicle). It is used to express capacities, dimensions, and accessibility features that can be reused across departures and vehicles in the fleet. 

## Purpose and Scope
Used as reference data and referenced from ServiceJourney via VehicleTypeRef (0:1). This keeps vehicle properties separate from route data (Separation of Concerns).

## Core Data (from XSD – selection)
- **Identifier and version**: id, version.
- **Name/ShortName/Description**.
- **Classification/association to model (VehicleModel)** – optional.
- **Properties**: selfPropelled, fuelType, euroClass.
- **Capacity**: total capacity and distribution per (fare) class.
- **Dimensions/weight**: length, width, height, weight.
- **Accessibility/boarding**: lowFloor, hasLiftOrRamp, hasHoist, stepHeight/BoardingHeight (LengthType), GapToPlatform (LengthType).

## Separation of Concerns
VehicleType should only describe properties of the type (e.g., dimensions, capacity, boarding). Service and line properties (mode, submode, branding, operator-specific details) belong in Timetable-/Line-objects and reference fields there.

**Recommended placement**: define VehicleType in a ResourceFrame and reference it from ServiceJourney/VehicleJourney with VehicleTypeRef in TimetableFrame (profile recommendation to keep data modular and reusable).

## When is a VehicleType not “generic”?
If it contains characteristics for an individual vehicle (individual ID, temporary adaptations, advertising/branding for a line), it is no longer generic. Such aspects should be modeled as vehicle/operational data, not in VehicleType. The XSD elements in VehicleType are inherently type-descriptive and do not encourage individual-level data.

Classification against VehicleModel can still be generic as long as it describes a model/series, not an individual.

## Usage from ServiceJourney
VehicleTypeRef is optional (0..1) and used when type information is relevant for communication (capacity/accessibility) or operational calculations.

## Profile Rules (proposed)
- Use stable ERP IDs: ERP:VehicleType:<key>.
- Keep VehicleType at “fleet/model level.” Do not include individual-specific data.
- Accessibility measures (BoardingHeight/GapToPlatform) should indicate nominal values for the type, not station/platform-specific deviations.

## Minimal XML Example (illustrative)
```xml
<ResourceFrame id="ERP:ResourceFrame:1" version="1">
  <vehicleTypes>
    <VehicleType id="ERP:VehicleType:bus_12m_lf" version="1">
      <Name>12 m bus (low-floor)</Name>
      <Description>Lavgulv, manuell rampe</Description>
      <LowFloor>true</LowFloor>
      <BoardingHeight>0.30</BoardingHeight>
      <GapToPlatform>0.07</GapToPlatform>
    </VehicleType>
  </vehicleTypes>
</ResourceFrame>
```

And reference from ServiceJourney:
```xml
<ServiceJourney id="ERP:ServiceJourney:1" version="1">
  <JourneyPatternRef ref="ERP:JourneyPattern:1"/>
  <VehicleTypeRef ref="ERP:VehicleType:bus_12m_lf"/>
  ...
</ServiceJourney>
```

Note: element names for properties (e.g., LowFloor/BoardingHeight/GapToPlatform) should be validated against the current XSD (LengthType for heights/distances).

---

**Missing in current profile repo**
There is no dedicated VehicleType description in Profile_Documentation_v2; only references via ServiceJourney table. Create a new description page and link it from relevant “Objects” pages (ServiceJourney, VehicleJourney).

**Sources**: NeTEx XSD, Norwegian profile conventions.