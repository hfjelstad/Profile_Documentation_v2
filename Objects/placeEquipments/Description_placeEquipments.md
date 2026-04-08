# placeEquipments

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#placeequipments)*

## 1. Purpose

The **placeEquipments** element is a container within a StopPlace or Quay that holds equipment items describing the physical amenities and facilities available at the stop. It aggregates equipment objects such as WaitingRoomEquipment, ShelterEquipment, SanitaryEquipment, and TicketingEquipment into a single collection.

## 2. Structure Overview

```text
placeEquipments
 ├─ 📁 WaitingRoomEquipment (0..n)
 │  ├─ 📄 @id (1..1)
 │  └─ 📄 @version (1..1)
 ├─ 📁 ShelterEquipment (0..n)
 │  ├─ 📄 @id (1..1)
 │  └─ 📄 @version (1..1)
 ├─ 📁 SanitaryEquipment (0..n)
 │  ├─ 📄 @id (1..1)
 │  └─ 📄 @version (1..1)
 └─ 📁 TicketingEquipment (0..n)
    ├─ 📄 @id (1..1)
    └─ 📄 @version (1..1)
```

## 3. Key Elements

- **WaitingRoomEquipment** – Enclosed waiting facilities with properties such as Seats, StepFree, and Heated.
- **ShelterEquipment** – Open or semi-enclosed shelters with Seats, StepFree, and Enclosed indicators.
- **SanitaryEquipment** – Toilet and hygiene facilities with accessibility details.
- **TicketingEquipment** – Ticket machines and validators with payment method and transaction type details.

## 4. References

- [StopPlace](../StopPlace/Table_StopPlace.md) – Parent element that contains placeEquipments at the stop level
- [Quay](../Quay/Table_Quay.md) – Parent element that contains placeEquipments at the platform level
- [WaitingRoomEquipment](../WaitingRoomEquipment/Description_WaitingRoomEquipment.md) – Waiting room facility details
- [ShelterEquipment](../ShelterEquipment/Description_ShelterEquipment.md) – Shelter facility details
- [SanitaryEquipment](../SanitaryEquipment/Description_SanitaryEquipment.md) – Sanitary facility details
- [TicketingEquipment](../TicketingEquipment/Description_TicketingEquipment.md) – Ticketing machine details

## 5. Usage Notes

### 5a. Consistency Rules

- placeEquipments is always a child of StopPlace or Quay — it is not a standalone object.
- Equipment at the StopPlace level applies to the entire stop; equipment at the Quay level applies to that specific platform.
- Each equipment item within placeEquipments must have its own unique @id and @version.

### 5b. Validation Requirements

- Every equipment child must have a valid @id following codespace conventions.
- Equipment types should match the supported types in the profile (WaitingRoomEquipment, ShelterEquipment, SanitaryEquipment, TicketingEquipment).

### 5c. Common Pitfalls

> [!WARNING]
> - **Equipment at wrong level** — Placing platform-specific equipment (e.g., a shelter for Quay 1) on the StopPlace level makes it ambiguous which platform it belongs to.
> - **Missing placeEquipments wrapper** — Equipment items must be nested inside the placeEquipments container, not placed directly as children of StopPlace or Quay.

## 6. Additional Information

See [Table_placeEquipments.md](Table_placeEquipments.md) for detailed attribute specifications.

Example XML: [Example_placeEquipments.xml](Example_placeEquipments.xml)
