# DayType

## Definition
**DayType** represents a classification of days within a Service Calendar in NeTEx. It is used to group days that share the same operational characteristics, such as weekdays, weekends, or holidays.

## Purpose
The purpose of **DayType** is to define sets of days on which specific services operate. It allows operators to manage and apply operational patterns consistently across multiple services.

## Structure
A DayType element typically includes the following attributes and sub-elements:

- **id** (mandatory): Unique identifier for the DayType.
- **Name** (mandatory): Human-readable name for the DayType (e.g., "Weekdays").
- **Description** (optional): Additional description of the DayType.
- **Properties** (optional): May include operational characteristics or tags.

## Usage
- **DayType** is referenced by **ServiceCalendar** to define which days a service is active.
- It is linked to **DayTypeAssignment**, which assigns the DayType to specific dates or periods.

## Rules and Constraints
- **id**: Must be unique within the dataset.
- **Name**: Mandatory.
- A DayType can be associated with multiple DayTypeAssignments.

