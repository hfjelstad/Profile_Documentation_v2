## Structure Overview

```text
StopPointInJourneyPattern
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ @order (1..1)
 ├─ ScheduledStopPointRef/@ref (1..1)
 ├─ ForAlighting (0..1)
 ├─ ForBoarding (0..1)
 ├─ DestinationDisplayRef/@ref (0..1)
 ├─ ChangeOfDestinationDisplay (0..1)
 ├─ RequestStop (0..1)
 ├─ RequestMethod (0..1)
 ├─ StopUse (0..1)
 ├─ noticeAssignments (0..1)
 │  └─ NoticeAssignment (0..n)
 └─ BookingArrangements (0..1)
```

---

## Table

| Element | Type | XSD | FR | SLO | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| **@id** | ID | 1..1 | 1..1 | 1..1 | Unique identifier | @id |
| **@version** | xsd:string | 1..1 | 1..1 | 1..1 | Version label | @version |
| **@order** | xsd:integer | 1..1 | 1..1 | 1..1 | Sequential position in the JourneyPattern (1, 2, 3…) | @order |
| **[ScheduledStopPoint](../ScheduledStopPoint/Table_ScheduledStopPoint.md)@ref** | Reference | 0..1 | 1..1 | 1..1 | Reference to the logical stop point | ScheduledStopPointRef/@ref |
| ForAlighting | xsd:boolean | 0..1 | 0..1 | 0..1 | Whether passengers may alight (default: true) | ForAlighting |
| ForBoarding | xsd:boolean | 0..1 | 0..1 | 0..1 | Whether passengers may board (default: true) | ForBoarding |
| [DestinationDisplay](../DestinationDisplay/Table_DestinationDisplay.md)@ref | Reference | 0..1 | 0..1 |  | Headsign/display shown from this stop onwards | DestinationDisplayRef/@ref |
| ChangeOfDestinationDisplay | xsd:boolean | 0..1 | 0..1 |  | Whether the destination display changes at this stop | ChangeOfDestinationDisplay |
| RequestStop | xsd:boolean | 0..1 | 0..1 |  | Whether this is a request stop (on-demand only) | RequestStop |
| RequestMethod | RequestMethodEnum | 0..1 | 0..1 | How to request the stop: `handSignal`, `phoneCall`, `sms`, `stopButton`, `none` | RequestMethod |
| StopUse | StopUseEnum | 0..1 | | How the stop is used: `access`, `passthrough`, `interchangeOnly` | StopUse |
| noticeAssignments | | 0..1 | 0..1 | Container for stop-specific notice assignments | noticeAssignments |

### NoticeAssignment (within noticeAssignments)

| Element | Type | XSD | FR | Description | Path |
|---------|------|-----|-----|-------------|------|
| **@id** | ID | 1..1 | 1..1 | Unique identifier for the assignment | noticeAssignments/NoticeAssignment/@id |
| **@version** | xsd:string | 1..1 | 1..1 | Version label | noticeAssignments/NoticeAssignment/@version |
| **@order** | xsd:integer | 1..1 | 1..1 | Evaluation order | noticeAssignments/NoticeAssignment/@order |
| **[Notice](../Notice/Table_Notice.md)@ref** | Reference | 0..1 | 1..1 | Reference to the Notice text | noticeAssignments/NoticeAssignment/NoticeRef/@ref |

### BookingArrangements

| Element | Type | XSD | FR | Description | Path |
|---------|------|-----|-----|-------------|------|
| BookingAccess | BookingAccessEnum | 0..1 | 0..1 | Who can book: `public`, `authorisedPublic`, `staff` | BookingArrangements/BookingAccess |
| BookWhen | PurchaseWhenEnum | 0..1 | 0..1 | When to book: `advanceOnly`, `dayOfTravelOnly`, `untilPreviousDay`, `advanceAndDayOfTravel` | BookingArrangements/BookWhen |
| LatestBookingTime | xsd:time | 0..1 | 0..1 | Latest time a booking can be made (e.g., 16:00:00) | BookingArrangements/LatestBookingTime |
| MinimumBookingPeriod | xsd:duration | 0..1 | 0..1 | Minimum advance booking period (e.g., PT2H) | BookingArrangements/MinimumBookingPeriod |
| BookingUrl | xsd:anyURI | 0..1 | | URL for online booking | BookingArrangements/BookingUrl |
| BookingNote | xsd:string | 0..1 | 0..1 | Human-readable booking instructions | BookingArrangements/BookingNote |
| BookingMethod | BookingMethodEnum | 0..n | 0..n | How to book: `callDriver`, `callOffice`, `online`, `phoneAtStop`, `text` | BookingArrangements/BookingMethods/BookingMethod |

### Notes

- **Bold** elements are mandatory.
- StopPointInJourneyPattern is always nested within a JourneyPattern's pointsInSequence — it does not appear as a standalone top-level object.
- For the basic usage inline within JourneyPattern, see [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md).
- BookingArrangements is primarily used for flexible/demand-responsive transport.
