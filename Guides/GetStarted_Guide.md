# Get Started with NeTEx

## Introduction to NeTEx
NeTEx (Network Timetable Exchange) is a CEN standard for exchanging public transport data. It is widely used to ensure interoperability between different systems and organizations. NeTEx provides a structured XML-based format for representing transport-related information such as timetables, fares, and operational data.

### Why use NeTEx?
- **Interoperability**: Enables seamless data exchange between different systems.
- **Standardization**: Ensures consistent data structures across the industry.
- **Flexibility**: Supports a wide range of public transport use cases.

## Basic Structure
A NeTEx document is organized into **Frames**, each representing a specific domain of data (e.g., ServiceFrame, FareFrame). Frames contain objects and references that define the transport network, schedules, and related information.

### Common Frames
- **ServiceFrame**: Contains routes, lines, and scheduled stop points.
- **FareFrame**: Defines fare structures and pricing information.
- **ResourceFrame**: Holds shared resources like operators and organizations.

## Validation
To ensure data quality, NeTEx files should be validated against the official XML schema. Validation tools and services are available to check compliance and detect errors.

## Useful Links
- [CEN NeTEx Standard](https://www.cen.eu/)
- [NeTEx GitHub Repository](https://github.com/NeTEx-CEN)
- [Entur Developer Portal](https://developer.entur.org/)

---

## Related Frames
Below are links to detailed descriptions of each frame:

- [Description_ServiceFrame.md](../Objects/ServiceFrame/Description_ServiceFrame.md)
- [Description_FareFrame.md](../Objects/FareFrame/Description_FareFrame.md)
- [Description_ResourceFrame.md](../Objects/ResourceFrame/Description_ResourceFrame.md)
- [Description_TimetableFrame.md](../Objects/TimetableFrame/Description_TimetableFrame.md)
- [Description_CompositeFrame.md](../Objects/CompositeFrame/Description_CompositeFrame.md)
- [Description_SiteFrame.md](../Objects/SiteFrame/Description_SiteFrame.md)
- [Description_OrganisationalFrame.md](../Objects/OrganisationalFrame/Description_OrganisationalFrame.md)
- [Description_ConnectionFrame.md](../Objects/ConnectionFrame/Description_ConnectionFrame.md)
- [Description_AccessibilityFrame.md](../Objects/AccessibilityFrame/Description_AccessibilityFrame.md)
