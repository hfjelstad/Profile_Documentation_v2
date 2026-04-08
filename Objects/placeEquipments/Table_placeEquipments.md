## Structure Overview

```text
placeEquipments
 ├─ ShelterEquipment (0..n)
 │  ├─ @id (1..1)
 │  └─ @version (1..1)
 ├─ WaitingRoomEquipment (0..n)
 │  ├─ @id (1..1)
 │  └─ @version (1..1)
 ├─ SanitaryEquipment (0..n)
 │  ├─ @id (1..1)
 │  └─ @version (1..1)
 └─ TicketingEquipment (0..n)
    ├─ @id (1..1)
    └─ @version (1..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| [WaitingRoomEquipment](../WaitingRoomEquipment/Table_WaitingRoomEquipment.md) | Element | 0..n | Enclosed waiting room facility | placeEquipments/WaitingRoomEquipment |
| [ShelterEquipment](../ShelterEquipment/Table_ShelterEquipment.md) | Element | 0..n | Open or semi-enclosed shelter | placeEquipments/ShelterEquipment |
| [SanitaryEquipment](../SanitaryEquipment/Table_SanitaryEquipment.md) | Element | 0..n | Toilet and hygiene facility | placeEquipments/SanitaryEquipment |
| [TicketingEquipment](../TicketingEquipment/Table_TicketingEquipment.md) | Element | 0..n | Ticket machine or validator | placeEquipments/TicketingEquipment |
