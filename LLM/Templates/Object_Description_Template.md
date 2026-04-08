# `<ObjectName>` — Description Template

## Overview

This template defines the mandatory structure for all Object description files in the NeTEx profile.  
All description files must follow this 6-section format in the exact order specified below.

---

## Mandatory Section Order

**Sections 1–4 are required. Sections 5–6 are optional.**  
All sections must appear in this exact sequence. Do not add sections beyond these 6, and do not reorder them.

---

## 1. Purpose

**Required.** A short (2–3 sentence) explanation of the object's intent, scope, and role in the NeTEx model.  
Must be readable by non-technical users and derived from real usage in the XML examples.

**Example:**
> A **ServiceJourney** represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a JourneyPattern, includes scheduled passing times, and specifies operational details such as operator and days of operation.

---

## 2. Structure Overview

**Required.** A visual, icon‑based representation of the object's structure.  
Must follow the ordering and hierarchy shown in `Table_<ObjectName>.md`.

### Icon Legend
- `📄` = Simple element or attribute (primitive data)
- `📁` = Container element (grouping)
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
- For reference elements (`🔗`), combine cardinality with the `@ref` suffix, e.g. `🔗 LineRef/@ref (1..1)`.

### Structure Example

```text
📄 @id (1..1)
📄 @version (1..1)
📄 Name (1..1)
📁 TransportSubmode (0..1)
   ├── 📄 BusSubmode (0..1)
   └── 📄 RailSubmode (0..1)
🔗 JourneyPatternRef/@ref (1..1)
📁 passingTimes (1..1)
   └── 📄 TimetabledPassingTime (1..n)
       ├── 🔗 StopPointInJourneyPatternRef/@ref (1..1)
       ├── 📄 ArrivalTime (0..1)
       └── 📄 DepartureTime (0..1)
```

### Guidelines
- Keep structure under 20 lines for brevity
- Every element must show its cardinality using the notation above
- Mirror the exact order from the XML examples
- Use proper indentation and box‑drawing lines (`├──`, `└──`)

---

## 3. Key Elements

**Required.** A bulleted summary (3–6 items) of the most important elements and their roles.  
Do **not** duplicate the entire table; focus on what makes this object unique.

**Example:**
- **@id, @version** – Unique identifier and version label
- **JourneyPatternRef** – Reference to the stop sequence (mandatory; defines which stops are served)
- **passingTimes** – Collection of TimetabledPassingTime with ArrivalTime and DepartureTime
- **dayTypes** – DayType references specifying on which days the journey operates
- **OperatorRef** – Reference to the Operator performing this journey

---

## 4. References

**Required.** A bulleted list of all externally referenced objects with brief explanations.  
Use markdown links to the referenced object's Table file.

**Example:**
- [JourneyPattern](../JourneyPattern/Table_JourneyPattern.md) – Provides the authoritative stop sequence
- [DayType](../DayType/Table_DayType.md) – Specifies operational days
- [Operator](../Operator/Table_Operator.md) – Identifies the service provider
- [DatedServiceJourney](../DatedServiceJourney/Description_DatedServiceJourney.md) – Per-date instances of this journey

---

## 5. Usage Notes (optional)

**Optional, but recommended for objects with complex business rules or constraints.**

This section provides modeling details, best practices, validation rules, or clarifications. Use clear subsections (5a, 5b, 5c, etc.) as needed. Do **not** make this section overly long; if more than 3–4 subsections are needed, consider the object's complexity and whether the full specification better belongs in the Table.

### When to Include Usage Notes (Recommended)

Include Usage Notes when:
- The object has **non-obvious cardinality or cross-reference constraints** (e.g., "must reference exactly one JourneyPattern")
- **Comparison with a similar object** would clarify usage (e.g., ServiceJourney vs. DatedServiceJourney)
- **Common validation errors or pitfalls** exist (e.g., "Do not confuse X with Y")
- The object supports **multiple profiles (MIN, ERP, NP) with different rules** or cardinalities
- **Profile-specific variations** affect how the object should be used
- **Lifecycle or evolution information** is important (e.g.deprecated field or migration path)

Omit Usage Notes when:
- The Table and Key Elements sufficiently explain the object
- No special business logic or constraints apply
- Cross-references and cardinalities are straightforward

### Optional Subsections (Use as Needed)

#### 5a. Consistency Rules / Cross-Reference Constraints (optional)

Explicitly state rules for maintaining data integrity.

**Example:**
> A ServiceJourney must reference exactly one JourneyPattern. The pattern's stop sequence is authoritative and must not conflict with other referenced elements.

#### 5b. Validation Requirements (optional)

List critical checks or cardinality rules that must be validated.

**Example:**
> - Exactly one ServiceJourneyRef and exactly one OperatingDayRef must be present.
> - If ServiceAlteration is omitted, treat it as "planned".
> - All TimetabledPassingTime entries must correspond to StopPointInJourneyPattern entries in the referenced JourneyPattern.

#### 5c. Common Pitfalls / Anti-Patterns (optional)

Describe common mistakes and how to avoid them. Use a `> [!WARNING]` callout with bullet points:

**Example:**
```markdown
> [!WARNING]
> - **Confusing DatedServiceJourney with ServiceJourney**: ServiceJourney is a reusable template; DatedServiceJourney is a concrete instance on a specific date.
> - **Assuming DatedServiceJourney defines stop times**: Stop times come from the ServiceJourney's passingTimes, which reference the JourneyPattern's stops.
```

When there is only a single pitfall, still wrap it in `> [!WARNING]` with a bullet point.

#### 5d. Profile-Specific Notes (optional)

If the object behaves differently across MIN, ERP, or NP profiles, document the variations.

**Example:**
> - **MIN Profile:** blockRef is optional.
> - **ERP Profile:** blockRef is recommended for vehicle continuity tracking.
> - **NP (Nordic) Profile:** blockRef is required when trips are part of block chains.

---

## 6. Additional Information (optional)

**Optional.** Any supplementary information relevant to the object.  
Typically: links to examples, related guides, or notes on relationships.

**Example:**
> For a complete list of all elements, attributes, cardinalities, and data types, see [Table — ServiceJourney](Table_ServiceJourney.md).  
> Example XML: [Example_ServiceJourney.xml](Example_ServiceJourney.xml), [Example_ServiceJourney_MIN.xml](Example_ServiceJourney_MIN.xml)

---

## Section Rules & Constraints

1. **Sections 1–4 are mandatory.** All must be present and in order.
2. **Sections 5–6 are optional.** Omit if not relevant; when present, maintain their numbering.
3. **Section 5 subsections (5a–5d) are optional.** Use only the subsections that are relevant to the object.
4. **Content must align with the Table.** The Structure Overview and Key Elements must correspond to the table structure.
5. **No additional top-level sections.** Do not add custom sections like "Business Rules," "Changelog," "Data Quality," or "Lifecycle" at the top level. Use Section 5 subsections instead.
6. **Use relative markdown links only.** All cross-references must be relative paths to existing files in the repository.

---

## Quality Checklist

Before finalizing a description file, verify all points:

- [ ] **Purpose** is 2–3 sentences, non-technical, and self-contained
- [ ] **Structure Overview** is under 20 lines and uses icons consistently
- [ ] **Structure Overview** uses cardinality notation (1..1, 0..1, 1..n, 0..n) on every element — no "mandatory"/"optional" words
- [ ] **Icon order** exactly matches the XML example and Table file order
- [ ] **Key Elements** lists 3–6 critical items only (not all 30+ fields from the table)
- [ ] **Key Elements** describe function/role, not just field names
- [ ] **Key Elements** do not duplicate content from the Table
- [ ] **References** includes links to all externally referenced objects
- [ ] **References** uses correct markdown link syntax: `[ObjectName](../ObjectName/Table_ObjectName.md)`
- [ ] **Usage Notes** (if present) uses subsections (5a, 5b, 5c, 5d) appropriately
- [ ] **Usage Notes 5a** (if used) clearly states consistency rules and cross-reference constraints
- [ ] **Usage Notes 5b** (if used) lists actionable, testable validation rules
- [ ] **Usage Notes 5c** (if used) describes actual pitfalls; does not duplicate the Table
- [ ] **Usage Notes 5d** (if used) explains profile-specific variations only when they affect usage
- [ ] **Usage Notes total** does not exceed 3–4 subsections; if more needed, reevaluate object complexity
- [ ] **No sections beyond the 6 defined here** (plus optional 5a–5d subsections)
- [ ] **All relative links** are functional (check with local file browser)
- [ ] **No changelog or version history** in the description file (metadata belongs elsewhere)

---

## Implementation Notes

### How to Approach Section 5 (Usage Notes)

Start with the 6-section template. After drafting sections 1–4:

1. **Ask:** Does this object have non-obvious constraints, profile variations, or common pitfalls?
2. **If YES:** Add Section 5 with only the relevant subsections (5a–5d).
3. **If NO:** Omit Section 5 entirely.

### When Each Subsection is Most Useful

- **5a (Consistency Rules):** Complex objects with many cross-references (e.g., ServiceJourney, StopPlace)
- **5b (Validation):** Objects with cardinality constraints or mandatory field combinations
- **5c (Common Pitfalls):** Objects with high confusion risk (e.g., DatedServiceJourney vs. ServiceJourney)
- **5d (Profile Variations):** Objects behaving differently across MIN, ERP, NP profiles

### Length Guidelines

- **Short description:** Sections 1–4 only (no Usage Notes, no Additional Information)
- **Standard description:** Sections 1–4 + 1–2 subsections in Section 5
- **Comprehensive description:** Sections 1–6 + all 4 Usage Notes subsections

**Total target length:** 300–600 words. If exceeding 800 words, the Table may be more appropriate than the description.
