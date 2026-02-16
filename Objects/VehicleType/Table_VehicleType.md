# VehicleType Table

| **Name**         | **Type**                  | **Cardinality** | **Description**                                      |
|-------------------|---------------------------|------------------|------------------------------------------------------|
| Name             | MultilingualString        | 1:1              | Name of the vehicle type                             |
| Description      | MultilingualString        | 0:1              | Description of the vehicle type                      |
| PrivateCode      | xsd:normalizedString      | 0:1              | Internal classification of the vehicle type          |
| TypeOfFuel       | TypeOfFuelEnumeration     | 0:1              | Fuel type (e.g., petrol, diesel, electric)          |
| EuroClass        | xsd:normalizedString      | 0:1              | Euro emission class                                  |
| capacities       | PassengerCapacity         | 0:*              | Capacity per tariff class                            |
| LowFloor         | xsd:boolean               | 0:1              | Indicates if the vehicle has low flooring            |
| HasLiftOrRamp    | xsd:boolean               | 0:1              | Indicates if the vehicle has a lift or ramp          |
| Length           | xsd:decimal               | 0:1              | Total length of the vehicle                          |
| facilities       | ServiceFacilitySetRef     | 0:*              | References to ServiceFacilitySet objects             |