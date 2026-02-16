# Interchange

**Description:**
The `Interchange` element in NeTEx represents a planned or guaranteed transfer between two journeys, typically between two `ServiceJourney` elements. It ensures that passengers can transfer from one service to another under defined conditions.

## Purpose
The main purpose of `Interchange` is to model connections between journeys, including whether the transfer is guaranteed, the minimum transfer time, and any waiting constraints.

## Key Relationships
- **FromJourneyRef**: Reference to the originating `ServiceJourney`.
- **ToJourneyRef**: Reference to the destination `ServiceJourney`.
- **Guaranteed**: Indicates if the transfer is guaranteed (true/false).

## Usage
`Interchange` is used in timetables and operational planning to ensure smooth passenger transfers and to define operational rules for waiting and coordination between services.