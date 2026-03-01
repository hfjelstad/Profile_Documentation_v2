# Line – Requirements Table

This table enumerates the required and optional elements for a NeTEx Line in this profile. It reflects constraints from the current XSD variant used in this repository.

| Element | XPath | Cardinality | Type | Rules / Notes |
|---|---|---|---|---|
| Line | /PublicationDelivery/dataObjects/CompositeFrame/frames/ServiceFrame/lines/Line | 1..n | Line | Must be in the NeTEx namespace (http://www.netex.org.uk/netex). |
| @id | @id | 1..1 | xs:ID | Use codespace ERP, e.g. ERP:Line:<LOCAL_ID>. |
| @version | @version | 1..1 | xs:string | Use profile’s versioning convention (e.g. "1"). |
| Name | Name | 1..1 | xs:string | Human-readable line name. |
| OperatorRef | OperatorRef | 1..1 | Reference | Must resolve to an Operator defined in ResourceFrame/organisations. |
| Presentation | Presentation | 0..1 | Complex | Presentation is a direct child of Line. Do not add @id or @version on Presentation. |
| Colour | Presentation/Colour | 0..1 | string (HEX) | Use six uppercase hex digits without a leading #, e.g. 005EB8. |
| TextColour | Presentation/TextColour | 0..1 | string (HEX) | Use six uppercase hex digits without a leading #, e.g. FFFFFF. |
| TransportMode | — | — | — | Not applicable: TransportMode is not present directly under Line in the current XSD variant. Model line classification elsewhere (see notes). |
| TypeOfLineRef | — | — | — | Not applicable under Line in this XSD variant. If required by profile, document usage under an allowed context (e.g. via OperationalContextRef or other profile construct). |

Additional notes
- LowerCamelCase is used for collection elements: dataObjects, frames, lines, organisations.
- Line classification: Since TransportMode and TypeOfLineRef are not accepted directly under Line in the current schema, classification should be handled via an alternative modelling pattern permitted by the schema/profile (e.g. OperationalContextRef) or documented as a profile rule. Keep such usage out of Line if the XSD variant does not permit it.
