# StopPointInJourneyPattern

> *→ [Glossary definition](../../Guides/Glossary/Glossary.md#stoppointinjourneypattern)*

## 1. Purpose

A **StopPointInJourneyPattern** defines how a single stop is used within a JourneyPattern — whether passengers can board or alight, what destination display is shown, whether it is a request stop, and what booking arrangements apply. It is the richest sub-object within JourneyPattern and controls the per-stop passenger experience.

While the basic elements (@order, ScheduledStopPointRef, ForAlighting, ForBoarding) are already documented in [JourneyPattern](../JourneyPattern/Description_JourneyPattern.md), this page covers the full set of attributes available on StopPointInJourneyPattern, including elements used in flexible transport and passenger information.

## 2. Structure Overview

```text
📄 StopPointInJourneyPattern
  ├─ 📄 @id (1..1)
  ├─ 📄 @version (1..1)
  ├─ 📄 @order (1..1)
  ├─ 🔗 ScheduledStopPointRef/@ref (1..1)
  ├─ 📄 ForAlighting (0..1)
  ├─ 📄 ForBoarding (0..1)
  ├─ 🔗 DestinationDisplayRef/@ref (0..1)
  ├─ 📄 ChangeOfDestinationDisplay (0..1)
  ├─ 📄 RequestStop (0..1)
  ├─ 📄 RequestMethod (0..1)
  ├─ 📄 StopUse (0..1)
  ├─ 📁 noticeAssignments (0..1)
  │  └─ 📄 NoticeAssignment (0..n)
  │     ├─ 📄 @id (1..1)
  │     ├─ 📄 @version (1..1)
  │     ├─ 📄 @order (1..1)
  │     └─ 🔗 NoticeRef/@ref (1..1)
  └─ 📁 BookingArrangements (0..1)
     ├─ 📄 BookingAccess (0..1)
     ├─ 📄 BookWhen (0..1)
     ├─ 📄 LatestBookingTime (0..1)
     ├─ 📄 MinimumBookingPeriod (0..1)
     ├─ 📄 BookingUrl (0..1)
     ├─ 📄 BookingNote (0..1)
     └─ 📁 BookingMethods (0..1)
        └─ 📄 BookingMethod (0..n)
```

## 3. Key Elements

- **@order**: Sequential position in the JourneyPattern (1, 2, 3…). Must be unique and sequential within the pattern.
- **ScheduledStopPointRef**: Mandatory reference to the logical stop point being served.
- **ForAlighting / ForBoarding**: Boolean flags controlling whether passengers may get off/on at this stop. First stop is typically ForAlighting=false, last stop ForBoarding=false.
- **DestinationDisplayRef**: Reference to the DestinationDisplay shown on the vehicle from this stop onwards (e.g., the headsign changes).
- **ChangeOfDestinationDisplay**: Boolean indicating whether the destination display changes at this stop.
- **RequestStop**: Whether the vehicle only stops on passenger request (flag-down or button).
- **RequestMethod**: How to request the stop — `handSignal`, `phoneCall`, `sms`, `stopButton`, `none`, etc.
- **StopUse**: How the stop is used — `access` (passengers get on/off), `passthrough` (timing point only), `interchangeOnly`.
- **noticeAssignments**: Stop-specific notices (e.g., "This stop is served only on school days").
- **BookingArrangements**: For flexible/demand-responsive transport — how to book this stop, booking deadlines, booking methods.

## 4. References

- [ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md) – The logical stop being referenced
- [DestinationDisplay](../DestinationDisplay/Table_DestinationDisplay.md) – The display shown from this stop onwards
- [Notice](../Notice/Table_Notice.md) – Notices attached to this stop via NoticeAssignment
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – The parent pattern containing this stop point

## 5. Usage Notes

### 5a. Consistency Rules

- StopPointInJourneyPattern always exists within a JourneyPattern's pointsInSequence — it is never a standalone top-level object.
- @order values must be sequential integers starting from 1, with no duplicates or gaps within the same JourneyPattern.
- DestinationDisplayRef should only change at stops where the headsign actually changes — set ChangeOfDestinationDisplay=true at those stops.

### 5b. Validation Requirements

- **@id, @version, @order are mandatory** on every instance.
- **ScheduledStopPointRef is mandatory** — must resolve to an existing ScheduledStopPoint.
- ForAlighting defaults to `true` if omitted; ForBoarding defaults to `true` if omitted.
- When BookingArrangements is present, at least BookWhen or LatestBookingTime should be included to be actionable.

### 5c. Common Pitfalls

> [!WARNING]
> - **Forgetting ForAlighting=false on first stop**: The first stop has no preceding travel, so alighting makes no sense. Set ForAlighting=false explicitly.
> - **Forgetting ForBoarding=false on last stop**: The last stop has no onward travel. Set ForBoarding=false.
> - **BookingArrangements without BookingMethod**: Including booking rules without specifying *how* to book (phone, online, etc.) makes the data incomplete for consumer applications.
> - **ChangeOfDestinationDisplay without DestinationDisplayRef**: Setting ChangeOfDestinationDisplay=true but omitting the DestinationDisplayRef means the display changes to… nothing.

## 6. Additional Information

See [Table_StopPointInJourneyPattern.md](Table_StopPointInJourneyPattern.md) for detailed attribute specifications.

For the parent structure, see [JourneyPattern](../JourneyPattern/Description_JourneyPattern.md). For flexible transport, see also [FlexibleServiceProperties](../FlexibleServiceProperties/Description_FlexibleServiceProperties.md).
