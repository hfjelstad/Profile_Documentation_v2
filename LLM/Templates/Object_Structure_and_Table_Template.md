## 1. Structure Overview (placed at the top of `Table_<ObjectName>.md`)
The Structure Overview must:
- start with the object name as the root node (e.g., `ServiceJourney`),
- follow the exact element order from the XML examples,
- show nesting using a monospace tree diagram,
- use box‑drawing symbols for clarity and consistency,
- list attributes inline using `ElementName/@attribute`,
- show cardinality on every element using standard notation: `(1..1)`, `(1..n)`, `(0..1)`, `(0..n)`,
- match the Structure Overview in the corresponding `Description_<ObjectName>.md` (same elements, same order, same cardinality),
- contain no descriptions or comments—structure only.

### Structure Overview Template
```text
<ObjectName>
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ <ElementA> (1..1)
 ├─ <ElementB> (0..1)
 ├─ <ContainerA> (0..1)
 │   └─ <ChildElement> (0..n)
 └─ <ReferenceElement/@ref> (1..1)
 ```

## 2. `Table_<ObjectName>.md` (mandatory)

The flat table provides a normalized, machine‑readable representation of the object's structure.  
It must always be placed below the Structure Overview.

### Required Columns
The table must always contain the following base columns, in this order:

Element | Type | XSD | Description | Path

The **XSD** column is always the first cardinality column, showing the schema-level
minOccurs/maxOccurs values (e.g., `1..1` for required elements, `0..1` for optional).
This column is derived from the NeTEx XSD definition and represents what the schema
structurally allows.

In addition, the table must include one column for each ProfileCode for which an
`Example_<ObjectName>_<ProfileCode>.xml` file exists in the object folder.

These profile columns must be placed after the XSD column and before Description,
using the ProfileCode as the column header.

Each ProfileCode column must describe the cardinality for that profile as defined by the
corresponding XML example. If a profile example uses the MANDATORY/OPTIONAL frame convention,
elements in the MANDATORY frame map to `1..1`, elements only in the OPTIONAL frame map to
`0..1`, and absent elements are left empty. If a profile example exists but a particular
XML element is not present in that example, the column must still be included and the value
for that row left empty


### Rules
- **Element** must contain only the element name or attribute (e.g. `ArrivalTime`, `StopPointInJourneyPatternRef/@ref`).  
  No nesting or path notation is allowed here.
  
- **Cross‑references** must be written using relative links.  
  The link wraps the referenced object name, and `@ref` must appear *after* the link.  
  Example:  
  `[JourneyPattern](../JourneyPattern/Table_JourneyPattern.md/)@ref`

- **Type** must reflect the datatype or reference type used in the XML examples and NeTEx model.

- **Description** must briefly describe the purpose or meaning of the element, based on the XML and its role in the model.

- **Path** must contain the full hierarchical structure using slash notation  
  (e.g. `passingTimes/TimetabledPassingTime/ArrivalTime`).

### Additional Requirements
- All columns must be present for every row.
- Attributes must appear with an `@` prefix.
- The structure, order, and presence of elements must match the XML examples.
- The table and Structure Overview must always remain synchronized.
- All documentation must be written in English.

### Profile Column Rules
- The **XSD** column is always present as the first cardinality column.
- If no `Example_<ObjectName>_<ProfileCode>.xml` files exist (only `Example_<ObjectName>.xml`),
  the table should have: `Element | Type | XSD | Description | Path`.
- If one or more profile-specific XML examples exist, insert the profile columns between
  `XSD` and `Description`: `Element | Type | XSD | ERP | NP | Description | Path`.
- Only include profile columns for profiles that have corresponding XML example files.

### Structural Variants
When an object has distinct structural variants (e.g., StopPlace with Monomodal vs. Multimodal),
show each variant as a separate tree in the Structure Overview with a label after the root node
name (e.g., `StopPlace (Monomodal)`, `StopPlace (Multimodal Parent)`).
The flat table should contain a single unified set of rows covering all variants.