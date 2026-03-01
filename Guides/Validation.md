# NeTEx 2.0 Validation Guide

This guide explains how to validate example XML files in this repository against the NeTEx 2.0 schemas contained under "XSD 2.0/xsd".

Requirements
- A validator capable of XML Schema 1.0 (e.g., xmllint) or Saxon/Ant-based validation.
- Local clone of this repository.

Schema entry points
- PublicationDelivery (timetable focus): XSD 2.0/xsd/NeTEx_publication_timetable.xsd
- Generic publication: XSD 2.0/xsd/NeTEx_publication.xsd

Relevant object schemas for DatedServiceJourney context (part 2, journey times)
- XSD 2.0/xsd/netex_part_2/part2_journeyTimes/netex_datedVehicleJourney_support.xsd
- XSD 2.0/xsd/netex_part_2/part2_journeyTimes/netex_datedVehicleJourney_version.xsd

Run validation (xmllint example)
- cd to the repository root
- xmllint --noout \
  --schema "XSD 2.0/xsd/NeTEx_publication_timetable.xsd" \
  "Objects/DatedServiceJourney/Example_DatedServiceJourney.xml"

Notes
- Examples must be complete PublicationDelivery documents or be wrapped by a minimal PublicationDelivery envelope for XSD resolution.
- If an example is a fragment, create a temporary envelope (do not commit) like:

  <?xml version="1.0" encoding="UTF-8"?>
  <PublicationDelivery xmlns="http://www.netex.org.uk/netex"
                       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                       xsi:schemaLocation="http://www.netex.org.uk/netex XSD 2.0/xsd/NeTEx_publication_timetable.xsd">
    <PublicationTimestamp>2026-01-01T00:00:00Z</PublicationTimestamp>
    <ParticipantRef>ERP</ParticipantRef>
    <DataObjects>
      <!-- Insert the fragment within an appropriate frame (e.g., ServiceCalendarFrame/TimetableFrame)
           ensuring that identifiers and references are consistent. -->
    </DataObjects>
  </PublicationDelivery>

Troubleshooting
- Ensure relative paths in xsi:schemaLocation point to the local XSD 2.0/xsd directory.
- If the instance uses Part 2 constructs (e.g., DatedVehicleJourney), validate via the publication_timetable entry point since it imports required Part 2 modules.
