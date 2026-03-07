# Documentation Templates for the NeTEx Profile (LLM)

Scope
- This guide defines the templates and conventions for documentation and examples used in this profile (ERP - European Recommended Profile). It covers: folder structure, file naming, required documentation sections, description formatting, table formatting, and XML example formatting.

Folder structure
- Root (excerpt): Guides/, Frames/, Objects/, LLM/
- Per Frame: Frames/<FrameName>/{Description_<FrameName>.md, Table_<FrameName>.md, Example_<FrameName>.xml}
- Per Object: Objects/<ObjectName>/{Description_<ObjectName>.md, Table_<ObjectName>.md, Example_<ObjectName>.xml}
- Keep overview entries and links updated in navigation lists where applicable.

File naming conventions
- Examples: Example_<ObjectOrFrame>.xml
- Descriptions: Description_<ObjectOrFrame>.md
- Tables: Table_<ObjectOrFrame>.md
- Use the ERP codespace for XML ids in examples (e.g., ERP:DayType:WKD).
- Maintain alphabetical ordering in overview lists and verify that links resolve correctly.

Required documentation sections (Description_*.md)
- Title: "<Name> – description"
- Purpose: one-paragraph summary of intent and scope.
- Typical elements: bullet list of key child containers/elements.
- Keys: identifiers, versioning, and reference elements (e.g., *XxxRef*).
- Optionally: pointers to examples and XSD sections.

Description formatting
- Keep language concise and normative.
- Use bullet lists for Typical elements and Keys.
- Use relative links to related guides or frames when helpful.

Table formatting (Table_*.md)
- Purpose: a quick structural overview.
- Recommended columns:
  - Element
  - Type (NeTEx class/type)
  - Cardinality
  - Notes (constraints, references, profile rules)
- Ensure the table reflects the current profile and example file.

XML example formatting
- Container structure:
  - PublicationDelivery (xmlns="http://www.netex.org.uk/netex", version="1.0")
  - dataObjects → CompositeFrame → frames → [Frames/Objects]
- Conventions:
  - Use lowerCamelCase for list/collection elements (e.g., dataObjects, dayTypes, operatingPeriods).
  - Timestamps as xs:dateTime with timezone (e.g., 2026-02-25T14:22:00Z).
  - Consistent id strategy and version values (e.g., ERP:<Type>:<LocalId>). Use *Ref elements to link related objects.
- Keep examples minimal yet valid against NeTEx 2.0 XSD.

Workflow notes
- When adding a new item under Objects/ or Frames/, always provide the trio: Description_*.md, Table_*.md, and Example_*.xml using the patterns above.
- Update lists or indexes that reference the new files and verify that all links resolve.

Validation
- Validate all XML examples against the NeTEx 2.0 schemas included under XSD 2.0/.

Appendix: Minimal skeletons
- Description_<Name>.md
  - <Name> – description
  - Purpose: ...
  - Typical elements: ...
  - Keys: ...
- Table_<Name>.md
  - Columns: Element | Type | XSD Cardinality | ERP Cardinality | Description
  - Attributes should have @ as prefix, like @id and @version
- Example_<Name>.xml
  - PublicationDelivery → dataObjects → CompositeFrame → frames → <Name>
