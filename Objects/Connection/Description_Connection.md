# Connection

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#connection)*

## 1. Purpose

A **Connection** represents a physical transfer opportunity between two ScheduledStopPoints, defining the walking time a passenger needs to move from one service to another. Unlike Interchange (which links specific ServiceJourneys), a Connection describes a spatial, schedule-independent transfer possibility — it says "you can walk from stop A to stop B in 4 minutes." Journey planners use Connections to calculate viable transfer options.

## 2. Structure Overview

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

## 3. Key Elements

- **From / To**: Mandatory endpoints of the connection, each referencing a ScheduledStopPoint and optionally filtered by TransportMode.
- **TransferDuration**: Contains the walking times; DefaultDuration is mandatory when this element is present. Multiple duration variants support accessibility-aware routing.
- **BothWays**: Whether the connection is bidirectional (default: true). When false, only the From→To direction is valid.
- **Distance**: Physical walking distance in metres between the two stops.
- **TransportMode**: On each endpoint, optionally restricts the connection to specific modes (e.g., transfer only from bus to rail).

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – Both endpoints of the connection

## 5. Usage Notes

### 5a. Consistency Rules

- Both ScheduledStopPointRef entries must resolve to existing ScheduledStopPoints in the dataset.
- Connections are placed in the ServiceFrame (or GeneralFrame with TypeOfFrame NETEX_COMMUN in the French profile).
- For transfers between specific journeys (guaranteed connections), use [Interchange](../Interchange/Table_Interchange.md) instead.

### 5b. Validation Requirements

- **From and To are mandatory** — each must contain a ScheduledStopPointRef.
- **DefaultDuration is mandatory when TransferDuration is present** — use ISO 8601 duration format (e.g., `PT4M` for 4 minutes).
- Expect: FrequentTravellerDuration ≤ DefaultDuration ≤ OccasionalTravellerDuration.

### 5c. Common Pitfalls

> [!WARNING]
> - **Connection vs. Interchange**: Connection is a spatial/physical transfer possibility between stops. Interchange (ServiceJourneyInterchange) is a timed transfer between specific journeys. Don't use Connection where you need journey-level coordination.
> - **Connection vs. SiteConnection**: Connection links ScheduledStopPoints (planning-level). SiteConnection links StopPlaces or Quays (infrastructure-level). Use Connection for journey planning; SiteConnection for wayfinding.
> - **Missing DefaultDuration**: A Connection without TransferDuration is technically valid but useless for journey planners — always include the walking time.

## 6. Additional Information

See [Table_Connection.md](Table_Connection.md) for detailed attribute specifications.

For default transfer times that apply broadly (by mode or area), see DefaultConnection. For connections between physical sites with navigation details, see SiteConnection.
