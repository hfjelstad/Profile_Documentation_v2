# Frames Overview

This section provides an overview of NeTEx frames used to group related data structures (e.g., ServiceCalendarFrame, ServiceFrame, TimetableFrame). Each frame encapsulates logically connected objects and their references to support modular publication and reuse.

- ServiceCalendarFrame: captures service availability patterns through DayTypes, OperatingPeriods, and DayTypeAssignments.
- ServiceFrame: holds network-, line-, and journey-related data.
- TimetableFrame: holds time-related assignments and patterns.

For schema details and constraints, see the XSD 2.0 resources in this repository:
- XSD 2.0/README: ../../XSD%202.0/README.md

Notes
- All examples in this repository aim to be valid against NeTEx 2.0 schemas.
- Publication-level documents should validate against netex_publication.xsd for production use.
