# `<FrameName>` — Description Template

## Overview

This template defines the structure for all Frame description files in the NeTEx profile.
Frame descriptions are simpler than Object descriptions because Frames are containers that group
related Objects rather than carrying rich domain data themselves.

All description files must follow this 5-section format in the exact order specified below.

---

## Mandatory Section Order

**Sections 1–4 are required. Section 5 is optional.**
All sections must appear in this exact sequence.

---

## 1. Purpose

**Required.** A short (2–3 sentence) explanation of the frame's role, scope, and what kind of data it contains.
Should clarify where the frame sits in the NeTEx delivery structure (e.g., child of CompositeFrame).

**Example:**
> A **ServiceFrame** contains the network and route definitions for a public transport delivery. It groups Lines, Routes, JourneyPatterns, ScheduledStopPoints, and DestinationDisplays — the structural elements that describe where and how services run.

---

## 2. Structure Overview

**Required.** A visual, icon-based representation of the frame's top-level structure.
Must follow the ordering and hierarchy shown in `Table_<FrameName>.md`.

### Icon Legend
- `📄` = Simple element or attribute (primitive data)
- `📁` = Container element (collection)
- `🔗` = Reference to another object (always include @ref suffix)

### Cardinality Notation

Use standard cardinality notation to express element requirements:

| Notation | Meaning |
| -------- | ------- |
| `(1..1)` | Mandatory, exactly one |
| `(1..n)` | Mandatory, one or more |
| `(0..1)` | Optional, at most one |
| `(0..n)` | Optional, zero or more |

- Every element in the Structure Overview should include its cardinality.
- Do **not** use words like "mandatory", "optional", or "required" — use cardinality notation instead.

### Structure Example

```text
📄 @id (1..1)
📄 @version (1..1)
📁 organisations (0..1)
   ├── 📄 Authority (0..n)
   └── 📄 Operator (0..n)
📁 vehicleTypes (0..1)
   └── 📄 VehicleType (0..n)
📁 vehicles (0..1)
   └── 📄 Vehicle (0..n)
```

### Guidelines
- Keep structure concise — show the frame's collections and their immediate children
- Every element must show its cardinality using the notation above
- Mirror the exact order from the XML examples
- Use proper indentation and box-drawing lines (`├──`, `└──`)

---

## 3. Contained Elements

**Required.** A bulleted list of the key collections and elements carried by this frame.
Each item should name the container element and briefly describe what it holds, with links to
the relevant Object Table files where they exist.

**Example:**
- **lines** – Collection of [Line](../../Objects/Line/Table_Line.md) definitions
- **routes** – Collection of [Route](../../Objects/Route/Table_Route.md) definitions
- **journeyPatterns** – Collection of [JourneyPattern](../../Objects/JourneyPattern/Table_JourneyPattern.md) definitions
- **scheduledStopPoints** – Collection of [ScheduledStopPoint](../../Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md) definitions
- **destinationDisplays** – Collection of [DestinationDisplay](../../Objects/DestinationDisplay/Table_DestinationDisplay.md) definitions

---

## 4. Frame Relationships

**Required.** Describe how this frame relates to other frames in a typical NeTEx delivery.
Include which frames it depends on and which frames depend on it.

**Example:**
> ServiceFrame depends on **ResourceFrame** for Operator and Authority definitions.
> **TimetableFrame** depends on ServiceFrame for JourneyPatterns and Lines.
> All frames are typically wrapped in a **CompositeFrame** within a PublicationDelivery.

---

## 5. Usage Notes (optional)

**Optional.** Any additional guidance on how to use the frame correctly.
Include only when there are non-obvious constraints, ordering requirements, or common mistakes.
Use `> [!NOTE]` or `> [!WARNING]` callouts for important points.

**Example:**
```markdown
> [!NOTE]
> The ServiceFrame must always appear after ResourceFrame in the CompositeFrame when Operators are referenced by Lines.
```

---

## Section Rules & Constraints

1. **Sections 1–4 are mandatory.** All must be present and in order.
2. **Section 5 is optional.** Omit if not relevant.
3. **No additional top-level sections.** Keep frame descriptions concise.
4. **Structure Overview must use icon notation** (📄, 📁, 🔗) and match the XML example order.
5. **Structure Overview must use cardinality notation** on every element: `(1..1)`, `(1..n)`, `(0..1)`, `(0..n)`.
6. **Use relative markdown links** to reference Object Table files: `[ObjectName](../../Objects/ObjectName/Table_ObjectName.md)`
7. **Link to the frame's Table file** at the end of the description if one exists.

---

## Quality Checklist

Before finalizing a frame description file, verify:

- [ ] **Purpose** is 2–3 sentences and clearly states the frame's role
- [ ] **Structure Overview** uses icons consistently and matches the Table file order
- [ ] **Structure Overview** uses cardinality notation on every element — no "mandatory"/"optional" words
- [ ] **Contained Elements** lists all key collections from the XML example
- [ ] **Contained Elements** links to existing Object Table files where available
- [ ] **Frame Relationships** describes dependencies upstream and downstream
- [ ] **Usage Notes** (if present) provides actionable, non-obvious guidance
- [ ] **No sections beyond the 5 defined here**
- [ ] **All relative links** are functional
