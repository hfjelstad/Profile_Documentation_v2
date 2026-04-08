## Structure Overview

```text
VehicleType
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (1..1)
 ├─ Description (0..1)
 ├─ PropulsionType (0..1)
 ├─ PassengerCapacity (0..1)
 │  ├─ SeatingCapacity (0..1)
 │  ├─ StandingCapacity (0..1)
 │  └─ WheelchairPlaceCapacity (0..1)
 ├─ Length (0..1)
 ├─ Width (0..1)
 └─ Height (0..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the VehicleType | VehicleType/@id |
| @version | String | 1..1 | Version label | VehicleType/@version |
| Name | String | 0..1 | Name of the vehicle type | VehicleType/Name |
| Description | String | 0..1 | Description of the vehicle type | VehicleType/Description |
| PropulsionType | Enum | 0..1 | Fuel or propulsion type (combustion, electric, electricAssist, hybrid, human, other) | VehicleType/PropulsionType |
| SeatingCapacity | Integer | 0..1 | Number of seated passenger positions | VehicleType/PassengerCapacity/SeatingCapacity |
| StandingCapacity | Integer | 0..1 | Number of standing passenger positions | VehicleType/PassengerCapacity/StandingCapacity |
| WheelchairPlaceCapacity | Integer | 0..1 | Number of wheelchair positions | VehicleType/PassengerCapacity/WheelchairPlaceCapacity |
| Length | Decimal | 0..1 | Total vehicle length in meters | VehicleType/Length |
| Width | Decimal | 0..1 | Total vehicle width in meters | VehicleType/Width |
| Height | Decimal | 0..1 | Total vehicle height in meters | VehicleType/Height |
