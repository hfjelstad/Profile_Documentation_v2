# DayType

**Definition:**
A **DayType** in NeTEx represents a classification of days on which a specific set of services operates. It is used to group calendar days that share the same operational characteristics.

**Purpose:**
The main purpose of DayType is to define operational patterns for public transport services. Instead of assigning individual dates to each ServiceJourney, DayType allows grouping of dates into logical sets (e.g., weekdays, weekends, holidays).

**Relationships:**
- **ServiceJourney**: Each ServiceJourney references one or more DayTypes to indicate on which days it runs.
- **DayTypeAssignment**: Links DayType to specific calendar dates or periods.
- **OperatingPeriod**: Defines a continuous range of dates during which a DayType is valid.

**Cardinality:**
- A DayType can be referenced by multiple ServiceJourneys.
- A ServiceJourney must reference at least one DayType.
- A DayType can have zero or more DayTypeAssignments.

**Usage with DayTypeAssignment and OperatingPeriod:**
- **DayTypeAssignment** specifies which dates or periods a DayType applies to. It can include or exclude specific dates.
- **OperatingPeriod** defines a start and end date for a DayType, typically used for seasonal or timetable validity.

This combination allows flexible calendar definitions, such as: "Service runs on weekdays from 01-03-2026 to 30-06-2026, excluding public holidays."
