## Structure Overview

```text
Connection
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ Description (0..1)
 ├─ Distance (0..1)
 ├─ BothWays (0..1)
 ├─ TransferDuration (0..1)
 │  ├─ DefaultDuration (1..1)
 │  ├─ FrequentTravellerDuration (0..1)
 │  ├─ OccasionalTravellerDuration (0..1)
 │  └─ MobilityRestrictedTravellerDuration (0..1)
 ├─ From (1..1)
 │  ├─ ScheduledStopPointRef/@ref (1..1)
 │  └─ TransportMode (0..1)
 └─ To (1..1)
    ├─ ScheduledStopPointRef/@ref (1..1)
    └─ TransportMode (0..1)
```

---

## Table

| Element | Type | FR | Description | Path |
|---------|------|-----|-------------|------|
| **@id** | ID | 1..1 | Unique identifier for the connection | @id |
| **@version** | xsd:string | 1..1 | Version of this connection instance | @version |
| Name | xsd:string | 1..1 | Human-readable name for the connection | Name |
| Description | xsd:string | 0..1 | Textual description of the connection | Description |
| Distance | xsd:decimal | 0..1 | Walking distance in metres between the two stops | Distance |
| BothWays | xsd:boolean | 0..1 | Whether the connection applies in both directions (default: true) | BothWays |
| TransferDuration | | 1..1 | Container for walking duration data | TransferDuration |
| DefaultDuration | xsd:duration | 1..1 | Standard walking time for the transfer (e.g., PT4M) | TransferDuration/DefaultDuration |
| FrequentTravellerDuration | xsd:duration | 0..1 | Walking time for frequent travellers (shorter) | TransferDuration/FrequentTravellerDuration |
| OccasionalTravellerDuration | xsd:duration | 0..1 | Walking time for occasional travellers (longer) | TransferDuration/OccasionalTravellerDuration |
| MobilityRestrictedTravellerDuration | xsd:duration | 0..1 | Walking time for mobility-restricted travellers | TransferDuration/MobilityRestrictedTravellerDuration |
| **From** | ConnectionEnd | 1..1 | Origin endpoint of the connection | From |
| ScheduledStopPointRef | Reference | 1..1 | Reference to the origin ScheduledStopPoint | From/ScheduledStopPointRef/@ref |
| TransportMode | TransportModeEnum | 0..1 | Transport mode filter at origin | From/TransportMode |
| **To** | ConnectionEnd | 1..1 | Destination endpoint of the connection | To |
| ScheduledStopPointRef | Reference | 1..1 | Reference to the destination ScheduledStopPoint | To/ScheduledStopPointRef/@ref |
| TransportMode | TransportModeEnum | 0..1 | Transport mode filter at destination | To/TransportMode |

### Notes

- **Bold** elements are mandatory.
- From and To are ConnectionEnd structures, each requiring a ScheduledStopPointRef.
- TransferDuration follows the NeTEx TransferDuration structure (inherited from Transfer).
- For journey-level transfers, use [Interchange](../Interchange/Table_Interchange.md) instead.
