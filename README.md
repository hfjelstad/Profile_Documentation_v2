# 📚 Profile_Documentation_v2
Profile documentation for a NeTEx profile, with curated examples, descriptions, and tables designed for consistent modeling and exchange. The repository includes patterns/templates and an index for easy navigation.

## 🎯 Purpose
- Provide consistent, reusable NeTEx examples per object/frame.
- Ensure each example has a descriptive write-up and a structural table.
- Maintain a central, link-verified index for discoverability.

## 🗂️ Repository structure
- Root (excerpt):
  - [Guides/](Guides/)
  - [Frames/](Frames/)
  - [Objects/](Objects/)
  - [LLM/](LLM/) → see [LLM/README.md](LLM/README.md) and the example index [LLM/TableOfExamples.md](LLM/TableOfExamples.md)
  - [XSD 2.0/](XSD%202.0/) (NeTEx 2.0 schemas)
- Per Frame:
  - [Frames/](Frames/)<FrameName>/{Description_*.md, Table_*.md, Example_*.xml}
- Per Object:
  - [Objects/](Objects/)<ObjectName>/{Description_*.md, Table_*.md, Example_*.xml}

## 🧱 Conventions
- File naming:
  - Examples: Example_*.xml
  - Descriptions: Description_*.md
  - Tables: Table_*.md
- Use ERP as the codespace for XML ids in examples (e.g., ERP:DayType:WKD).
- Keep overview lists alphabetically ordered and verify links.

## 🔄 Workflow (add/update examples)
1) Under Objects/ (or Frames/), add at least one XML example named “Example_*.xml” using the ERP codespace, plus matching Description_*.md and Table_*.md following the master template.  
2) Update [LLM/TableOfExamples.md](LLM/TableOfExamples.md) with a new row:
   - Use the full relative path to the example.
   - Add links to the corresponding Description and Table documents.
   - Keep entries alphabetically sorted (by object, and when applicable by example name).  
3) Verify that all links resolve correctly in EnStandardBranch before opening a pull request.

## 🧭 Example structure (NeTEx)
- Container layout (minimal pattern):
  - PublicationDelivery (xmlns="http://www.netex.org.uk/netex", version="1.0")
  - dataObjects → CompositeFrame → frames → [Frames/Objects]
- Conventions:
  - Use lowerCamelCase for collection elements (e.g., dataObjects, dayTypes).
  - Use xs:dateTime with timezone (e.g., 2026-02-25T14:22:00Z).
  - Consistent id and version strategy; use *Ref elements for relationships.
  - Keep examples minimal yet valid against NeTEx 2.0 XSD.

## 🧪 Validation and schemas
- Validate all XML examples against the NeTEx 2.0 schemas under [XSD 2.0/](XSD%202.0/).

## 🔗 Navigation index (LLM/TableOfExamples.md)
- Centralized index of examples with links to their Description and Table documents.
- New entries must include full relative paths and maintain alphabetical ordering.
- All links must resolve correctly in EnStandardBranch prior to PR submission.

## 🧩 Appendix: minimal skeletons
- Description_*.md
  - <Title> – description
  - Purpose: …
  - Typical elements: …
  - Keys: …
- Table_*.md
  - Columns: Element | Type (NeTEx) | Cardinality | Notes
- Example_*.xml
  - PublicationDelivery → dataObjects → CompositeFrame → frames → …