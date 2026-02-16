# Get Started with NeTEx

## What is NeTEx and Why is it Used?
NeTEx (Network Timetable Exchange) is a CEN standard for exchanging public transport data in XML format. It is widely used to ensure interoperability between different systems and organizations, enabling consistent and structured data exchange for timetables, fares, and related information.

## Basic Structure
A NeTEx file is organized into **Frames**, which group related data. Common frame types include:
- **ResourceFrame**: Contains shared resources like codespaces, organizations, and responsibility sets.
- **ServiceFrame**: Defines routes, lines, and scheduled stop points.
- **TimetableFrame**: Holds dated service journeys and vehicle journeys.
- **FareFrame**: Contains fare structures, prices, and related rules.
- **SiteFrame**: Describes physical sites such as stations and stops.
- **VehicleScheduleFrame**: Includes vehicle blocks and duties.
- **ServiceCalendarFrame**: Defines operating days and calendars.

Each entity within a frame has a unique identifier, typically using a namespace (codespace) and a local ID, e.g., `ERP:Line:123`.

## How to Read and Validate a NeTEx File
- **Reading**: Use an XML viewer or specialized NeTEx tools to navigate the hierarchical structure.
- **Validation**: Validate against the NeTEx XSD schemas to ensure compliance. Tools like `xmllint` or dedicated NeTEx validators can be used.

## Useful Links
- [CEN NeTEx Standard](https://www.cen.eu/)
- [NeTEx GitHub Resources](https://github.com/NeTEx-CEN/NeTEx)
- [ENTUR NeTEx Guidelines](https://enturas.atlassian.net/wiki/spaces/PUBLIC/overview)
