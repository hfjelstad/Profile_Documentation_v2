# Line

Purpose
- The Line object represents a marketed public transport line within the profile. It groups service journeys and routes that are publicly communicated as one line.

Scope and assumptions
- A Line is identified and versioned within the ERP codespace. All identifiers MUST be ERP-scoped (e.g., ERP:Line:1001) and stable across updates.
- A Line may cover one or more routes and multiple service journeys. Operational details (timetables, day types) are specified elsewhere.

Identification and namespace
- All NeTEx examples and IDs in this profile use the ERP codespace/namespace.
- Example IDs: ERP:Line:1001, ERP:CompositeFrame:Line:1, ERP:ServiceFrame:1, ERP:Operator:ENTUR.

Key relationships
- OperatorRef: References the responsible operator organisation.
- Routes: A Line may relate to multiple Routes. Route definitions live in ServiceFrame/Route objects.
- Branding/Presentation: Optional presentation elements for colour and branding.

Business rules
- The combination of id and version uniquely identifies a Line.
- Name or PublicCode MUST be present so that the line can be understood by end users.
- TransportMode MUST be provided. TransportSubmode SHOULD be provided when relevant (e.g., expressBus).
- All referenced objects (e.g., Operator) MUST exist within the delivered data set or a known external frame.

Validation checklist
- [ ] File content is written in English.
- [ ] All IDs are ERP-scoped (prefix ERP:...).
- [ ] Required elements provided: id, version, Name or PublicCode, TransportMode, OperatorRef.
- [ ] Example complies with NeTEx structure used by this profile.

See also
- Objects/Line/Table_Line.md for the property specification table.
- Objects/Line/Example_Line.xml for a minimal NeTEx example with ERP namespace.
