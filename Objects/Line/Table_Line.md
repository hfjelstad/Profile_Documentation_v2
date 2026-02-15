# Line – Property specification table

This table defines the required and optional properties for a Line object in the profile. All identifiers MUST use the ERP codespace.

Columns
- Property: Logical name in the profile
- XPath: Location in the NeTEx document
- Card.: Cardinality
- Type/Values: Datatype and allowed values or constraints
- Example: Example value using ERP namespace

| Property | XPath | Card. | Type/Values | Example |
|---|---|---:|---|---|
| id | ServiceFrame/lines/Line/@id | 1..1 | ERP-scoped identifier | ERP:Line:1001 |
| version | ServiceFrame/lines/Line/@version | 1..1 | Positive integer or semantic version | 1 |
| Name | ServiceFrame/lines/Line/Name | 0..1 | String; SHOULD be present if PublicCode is missing | Line 21 |
| PublicCode | ServiceFrame/lines/Line/PublicCode | 0..1 | String; SHOULD be present if Name is missing | 21 |
| TransportMode | ServiceFrame/lines/Line/TransportMode | 1..1 | NeTEx TransportMode enumeration | bus |
| TransportSubmode | ServiceFrame/lines/Line/TransportSubmode | 0..1 | NeTEx BusSubmode/… enumeration; SHOULD when relevant | expressBus |
| OperatorRef | ServiceFrame/lines/Line/OperatorRef/@ref | 1..1 | Ref to Operator in ResourceFrame | ERP:Operator:ENTUR |
| Presentation/Colour | ServiceFrame/lines/Line/presentations/Presentation/Colour | 0..1 | RGB hex or named colour | #005EB8 |
| Presentation/TextColour | ServiceFrame/lines/Line/presentations/Presentation/TextColour | 0..1 | RGB hex or named colour | #FFFFFF |

Validation rules
- The combination of id and version uniquely identifies a Line within the dataset.
- Either Name or PublicCode MUST be present.
- All references (e.g., OperatorRef) MUST resolve within this delivery or a referenced frame.
- All IDs and references MUST be ERP-scoped (prefix ERP:...).

Related documents
- Objects/Line/Description_Line.md – narrative description and business rules.
- Objects/Line/Example_Line.xml – minimal NeTEx example using ERP codespace.
