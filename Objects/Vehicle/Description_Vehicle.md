# Vehicle

## Description
The **Vehicle** element in NeTEx represents a specific physical vehicle used to operate public transport services. It is typically associated with a **VehicleType** that defines its general characteristics (e.g., bus, tram, train). The Vehicle element allows operators to manage and reference individual vehicles, including their registration numbers and operator associations.

### Purpose and Usage
- Identify individual vehicles in operational data.
- Link vehicles to their type for capacity and feature information.
- Associate vehicles with operators for fleet management.

Vehicles are usually referenced in **DatedServiceJourney** or **Block** assignments to indicate which physical vehicle is used for a specific service.

---

## Key Characteristics
- **Granularity**: Represents a single physical vehicle.
- **Context**: Defined within a **ResourceFrame** in NeTEx.

