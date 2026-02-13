# Line

1. Definition & purpose
A Line is a grouping of Routes that is generally known to the public by a shared name or number. It represents the customer‑facing service identity used for communication and journey planning.

2. Context & relationships
- Belongs in ServiceFrame.
- Associated to its Network using RepresentedByGroupRef (either to Network or a GroupOfLines within a Network).
- Operated by one primary Operator (OperatorRef), with optional additional operators.
- Routes (Route) belonging to the Line define the directional paths served.

3. Attributes table
See Table_Line.md for a complete, machine‑readable overview of attributes, types and cardinalities.

4. Child elements table
See Table_Line.md for child elements, references and lists.

5. XSD reference(s)
- Complex type: Line_VersionStructure (NeTEx Part 1, ServiceFrame schema)
- Key data types: AllVehicleModesOfTransportEnumeration, TransportSubmodeStructure, OperatorRefStructure, GroupOfLinesRefStructure, TypeOfLineRef, ExternalObjectRef.

6. XML example(s)
See Example_Line.xml for a minimal compliant sample, including TransportMode/Submode, OperatorRef and RepresentedByGroupRef.

7. Cardinality & constraints (profile)
- Name: 1..1 (required)
- TransportMode: 1..1 (required)
- TransportSubmode: 1..1 (required; must match the chosen TransportMode)
- OperatorRef: 1..1 (required in profile; may be omitted only in exceptional cases)
- RepresentedByGroupRef: 1..1 (required)
- PublicCode: 0..1 (optional; public line number or code)
- PrivateCode: 0..1 (optional; non‑public identifier)
- Url: 0..1 (optional)
- BrandingRef: 0..1 (optional; to override/add line branding)
- TypeOfLineRef: 0..1 (optional; classification such as replacement line)
- ExternalLineRef: 0..1 (optional)
- Monitored: 0..1 (optional; true if real‑time normally available)
- routes (RouteRefs): 0..* (optional list of member routes)

8. Usage notes
- Prefer using Name for human‑readable presentation; PublicCode is the publicly advertised code/number.
- TransportSubmode must be consistent with TransportMode (e.g., localBus under bus).
- Use BrandingRef to apply a marketed name/URL distinct from the authority or operator brand.

9. Links to related objects
- Network, GroupOfLines, Route, Operator, Branding, Presentation, AccessibilityAssessment.

10. Profile‑specific rules
- The Nordic profile requires OperatorRef, TransportMode, TransportSubmode, Name and RepresentedByGroupRef.
- PublicCode is optional; some lines may not carry an explicit public code.
