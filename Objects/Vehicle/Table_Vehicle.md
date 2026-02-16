# Vehicle Attribute Table

| **Attribute**        | **Description**                                      | **Type**   | **Usage**     |
|----------------------|------------------------------------------------------|-----------|--------------|
| **id**              | Unique identifier for the Vehicle element            | String    | Mandatory    |
| **version**         | Version of the element                               | String    | Mandatory    |
| **VehicleTypeRef**  | Reference to the associated VehicleType              | Reference | Mandatory    |
| **RegistrationNumber** | Vehicle's registration/license plate number       | String    | Optional     |
| **OperatorRef**     | Reference to the Operator responsible for the vehicle| Reference | Optional     |

---

**Notes:**
- `id` should follow NeTEx namespace conventions (e.g., `ERP:Vehicle:1234`).
- `VehicleTypeRef` links to a predefined VehicleType in the ResourceFrame.
- `OperatorRef` is useful for fleet ownership and operational responsibility.
