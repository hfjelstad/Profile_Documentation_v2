
# NeTEx Profile Documentation
A practical reference, learning resource, and example library for working with NeTEx.

This repository is designed as a human-friendly entry point to NeTEx: a place to learn the structure of the standard, explore real examples, and understand how frames and objects relate to each other in practice.

Its goals are:
- 📘 **Introduce** the concepts and structure of NeTEx
- 🧭 **Guide** readers through frames, objects, and modeling patterns
- 🗂️ **Provide** a high-quality example library
- 🛠️ **Define** conventions for profiling and documentation
- 🔎 **Serve** as a reference for navigation and discovery

---

## 🎯 What This Repository Contains

### 1. **High‑quality NeTEx examples**
Each example is:
- Minimal, but complete enough to be meaningful
- Structured consistently using the ERP codespace
- Designed to illustrate a single concept or object clearly
- Built using a unified pattern:

```
PublicationDelivery → dataObjects → CompositeFrame → frames → …
```

### 2. **Human‑oriented documentation**
For every frame or object, you will find:
- A description file explaining purpose, usage, and relationships
- A structured table outlining elements, cardinality, and type information
- One or more XML examples showing how to model the entity

### 3. **A centralized navigation index**
Located at:
```
LLM/TableOfExamples.md
```
This file provides an alphabetically ordered list of all examples, together with links to documentation and tables.

---

## 🗂️ Repository Structure

```
Root
│
├── Guides/                 → Introductory material and conceptual explanations
├── Frames/                 → Documentation and examples grouped by Frame
│     └── <FrameName>/
│          ├── Description_*.md
│          ├── Table_*.md
│          └── Example_*.xml
│
├── Objects/                → Documentation and examples for individual NeTEx objects
│     └── <ObjectName>/
│          ├── Description_*.md
│          ├── Table_*.md
│          └── Example_*.xml
│
├── LLM/
│     ├── README.md
│     └── TableOfExamples.md → Central index of all examples
```

---

## 🧱 Conventions

### **File naming**
| Type | Naming | 
|------|--------|
| XML examples | `Example_*.xml` |
| Descriptions | `Description_*.md` |
| Tables | `Table_*.md` |

### **Codespace**
All XML identifiers use the `ERP` codespace:
```
ERP:<ObjectType>:<Identifier>
```
Example:
```
ERP:DayType:WKD
```

### **XML structure principles**
- Consistent element naming (`lowerCamelCase` for collections)
- `*Ref` elements used for relationships
- Minimal but valid examples
- Time values use timezone-aware `xs:dateTime`
  → `2026-02-25T14:22:00Z`

---

## 🔄 How to Add or Update an Example

### 1. Add three files in the correct directory
- `Example_<Name>.xml`
- `Description_<Name>.md`
- `Table_<Name>.md`

Use the master templates found in the Guides/ folder whenever applicable.

### 2. Update the navigation index
In:
```
LLM/TableOfExamples.md
```
Add a new row with:
- Relative path to the XML example
- Links to description and table
- Alphabetical ordering
- Verified working links

### 3. Verify links in the target branch
All links must resolve correctly before opening a pull request.

---

## 🧩 Template Structures

### **Description_*.md**
Should include:
- Purpose
- Typical elements
- Key relationships
- Notes related to examples

### **Table_*.md**
Standard columns:
| Element | Type | Cardinality | Notes |

### **Example_*.xml**
A minimal but correct XML example, using ERP codespace and consistent structure.

---

## 📚 How to Use This Repository for Learning
1. Begin in `Guides/` to understand the overall context
2. Explore `Frames/` for structural patterns
3. Dive into `Objects/` for detailed reference material
4. Use the index in `LLM/TableOfExamples.md` for quick lookup
5. Compare XML examples with table documentation
6. Read description files to understand modeling intent

---

## ✨ Goal of This Repository
This project exists to make NeTEx easier to understand and apply by providing:
- Clear documentation
- Consistent modeling patterns
- A rich library of examples
- A unified reference structure

It is designed to help both newcomers and experienced practitioners work with NeTEx in a predictable, well-documented, and transparent way.
