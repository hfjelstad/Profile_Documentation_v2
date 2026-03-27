# Connection

## Structure Overview

```text
📄 Connection
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 Name (0..1)
  ├─ 📄 Description (0..1)
  ├─ 📄 Distance (0..1)
  ├─ 📄 BothWays (0..1)
  ├─ 📁 TransferDuration (0..1)
  │  ├─ 📄 DefaultDuration (1..1)
  │  ├─ 📄 FrequentTravellerDuration (0..1)
  │  ├─ 📄 OccasionalTravellerDuration (0..1)
  │  └─ 📄 MobilityRestrictedTravellerDuration (0..1)
  ├─ 📁 From (1..1)
  │  ├─ 🔗 ScheduledStopPointRef/@ref (1..1)
  │  └─ 📄 TransportMode (0..1)
  └─ 📁 To (1..1)
     ├─ 🔗 ScheduledStopPointRef/@ref (1..1)
     └─ 📄 TransportMode (0..1)
```

---

## Connection

| Element | Type | Description | Path |
|---------|------|-------------|------|
| **@id** | ID | Unique identifier for the connection | @id |
| **@version** | xsd:string | Version of this connection instance | @version |
| Name | xsd:string | Human-readable name for the connection | Name |
| Description | xsd:string | Textual description of the connection | Description |
| Distance | xsd:decimal | Walking distance in metres between the two stops | Distance |
| BothWays | xsd:boolean | Whether the connection applies in both directions (default: true) | BothWays |
| TransferDuration | | Container for walking duration data | TransferDuration |
| DefaultDuration | xsd:duration | Standard walking time for the transfer (e.g., PT4M) | TransferDuration/DefaultDuration |
| FrequentTravellerDuration | xsd:duration | Walking time for frequent travellers (shorter) | TransferDuration/FrequentTravellerDuration |
| OccasionalTravellerDuration | xsd:duration | Walking time for occasional travellers (longer) | TransferDuration/OccasionalTravellerDuration |
| MobilityRestrictedTravellerDuration | xsd:duration | Walking time for mobility-restricted travellers | TransferDuration/MobilityRestrictedTravellerDuration |
| **From** | ConnectionEnd | Origin endpoint of the connection | From |
| ScheduledStopPointRef | Reference | Reference to the origin ScheduledStopPoint | From/ScheduledStopPointRef/@ref |
| TransportMode | TransportModeEnum | Transport mode filter at origin | From/TransportMode |
| **To** | ConnectionEnd | Destination endpoint of the connection | To |
| ScheduledStopPointRef | Reference | Reference to the destination ScheduledStopPoint | To/ScheduledStopPointRef/@ref |
| TransportMode | TransportModeEnum | Transport mode filter at destination | To/TransportMode |

### Notes

- **Bold** elements are mandatory.
- From and To are ConnectionEnd structures, each requiring a ScheduledStopPointRef.
- TransferDuration follows the NeTEx TransferDuration structure (inherited from Transfer).
- For journey-level transfers, use [Interchange](../Interchange/Table_Interchange.md) instead.
