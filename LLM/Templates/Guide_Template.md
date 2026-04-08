# Guide Template

## Overview

This template defines the recommended structure for all Guide files under `Guides/<GuideName>/`.
Guides are **conceptual documents** aimed at human readers — they explain *why* and *how*, not just *what*. Unlike Object/Frame documentation (which is structural and specification-oriented), Guides teach concepts, explain patterns, and provide worked examples.

Each guide lives in its own folder and may include supporting files (XML examples, images, diagrams).

---

## Guide Folder Structure

```
Guides/
└── <GuideName>/
    ├── <GuideName>.md              ← Main guide document (required)
    ├── Example_<Topic>.xml         ← Validated XML example (recommended)
    └── images/                     ← Diagrams, models, screenshots (optional)
        ├── <diagram_name>.png
        └── ...
```

---

## Recommended Section Structure

Guides are more flexible than Object/Frame documentation, but should follow this general flow. Sections can be renamed to fit the topic, but the **progression from context → concept → practice → reference** should be maintained.

### 1. Introduction (required)

**What:** 2–4 sentences explaining the guide's topic and why it matters.
**Tone:** Accessible to newcomers. Assume the reader knows what NeTEx is but not the specific topic.

Include a "what you'll learn" summary using an emoji list:

```markdown
In this guide you will learn:
- 🎯 What separation of concerns means in a NeTEx context
- 🧩 The three coupling strategies and when to use each
- 🗂️ How NeTEx frames map to domains
- 📝 Practical XML examples for each approach
```

### 2. Core Concepts (required)

**What:** The conceptual foundation. Explain the *why* before the *how*.
Use a mix of:
- **Prose** for explanation
- **Tables** for comparisons and trade-offs
- **ASCII/Unicode diagrams** for relationships and flows
- **Images** for complex visual models (reference from `images/` folder)

**Tips:**
- Use `> [!TIP]` callouts for practical advice
- Use `> [!NOTE]` for important caveats
- Use `> [!WARNING]` for common mistakes or pitfalls
- Use tables to compare approaches with pros/cons columns
- Use collapsible `<details>` sections for advanced topics that might overwhelm newcomers
- Use **Mermaid diagrams** for relationships, flows, and tree structures (apply the blue palette — see LLM/README.md section 7c)
- **Do not use** emoji-based callouts (`> 💡 **Tip:**`, `> ⚠️ **Note:**`) — use flexible-alerts syntax instead

### 3. How It Works in NeTEx (required)

**What:** Map the concepts to concrete NeTEx objects, frames, and references. This is where the guide becomes NeTEx-specific.

Include:
- **Domain/Object mapping table** — which NeTEx objects belong to which concern
- **Frame mapping** — which frames carry which data
- **Reference patterns** — how objects link across domains

Use code blocks with inline comments for XML snippets:
```xml
<!-- Traveler concern: what the passenger sees -->
<ServiceJourney id="ERP:ServiceJourney:SJ_001" version="1">
  <VehicleTypeRef ref="ERP:VehicleType:IC_Train"/>   <!-- lightweight hint only -->
</ServiceJourney>
```

### 4. Practical Examples (required)

**What:** Complete, runnable XML examples with narrative explanation.
Each example should:
- Be a **validated** NeTEx XML file (or reference one in the same folder)
- Include **inline comments** explaining key decisions
- Show a **realistic scenario** (not abstract Object A → Object B)

If the guide folder contains a full `Example_<Topic>.xml`, reference it:
```markdown
📄 **Full example:** [Example_SeparationOfConcerns.xml](Example_SeparationOfConcerns.xml)
```

For inline snippets, keep them focused — show only the relevant fragment, not the full PublicationDelivery wrapper.

### 5. Best Practices (recommended)

**What:** Actionable recommendations. Use a `> [!TIP]` callout with bullet points.

Format options:
- `> [!TIP]` with bulleted best-practice rules
- ✅ / ❌ do/don't lists
- Decision flowcharts (Mermaid)

### 6. Related Resources (required)

**What:** Links to related guides, frame/object documentation, and external references.

```markdown
## 🔗 Related Resources

### Guides
- [FramesOverview](../FramesOverview/FramesOverview.md) – How frames organize data

### Frames & Objects
- [TimetableFrame](../../Frames/TimetableFrame/Table_TimetableFrame.md) – Journey scheduling
- [ServiceJourney](../../Objects/ServiceJourney/Table_ServiceJourney.md) – Journey definitions

### External
- [NeTEx CEN Standard](https://www.netex-cen.eu/) – Official specification
```

---

## Formatting Guidelines

### Tone & Audience
- Write for **human readers** first (practitioners, system architects, developers)
- Assume familiarity with NeTEx basics but not the specific topic
- Use **active voice** and **second person** ("you") where appropriate
- Keep paragraphs short (3–5 sentences max)

### Visual Elements

| Element | When to Use | How |
|---------|-------------|-----|
| Emoji headers | Section headings | `## 🎯 Introduction` |
| Tables | Comparisons, mappings, trade-offs | Markdown tables |
| ASCII diagrams | Simple relationships, flows | Monospace code blocks |
| Images | Complex visual models | `![Alt text](images/name.png)` |
| Code blocks | XML examples, snippets | Fenced with `xml` language tag |
| Blockquotes | Tips, warnings, key insights | `> [!TIP]`, `> [!WARNING]`, `> [!NOTE]` |
| Collapsible sections | Advanced/optional content | `<details><summary>` |
| Mermaid diagrams | Relationships, flows, trees | ` ```mermaid ` with blue palette |
| Docsify tabs | Multi-profile examples | `<!-- tabs:start -->` blocks |

### Cross-References
- Use **relative markdown links** to existing files in the repository
- Link to **Table** files for structural reference, **Description** files for conceptual context
- Always verify links resolve correctly

### Length
- **Target:** 400–1200 words for the main content (excluding XML examples)
- Guides may be longer than Object/Frame descriptions — depth is expected
- If a guide exceeds ~2000 words, consider splitting into sub-guides

---

## Quality Checklist

Before finalizing a guide, verify:

- [ ] **Introduction** clearly states the topic and what the reader will learn
- [ ] **Core Concepts** explain the *why*, not just the *what*
- [ ] **NeTEx mapping** connects concepts to concrete objects and frames
- [ ] **Examples** are validated XML (or reference validated files)
- [ ] **Best Practices** are actionable and specific
- [ ] **Related Resources** link to relevant guides, frames, and objects
- [ ] **All relative links** resolve to existing files
- [ ] **Images** are stored in `images/` subfolder (not inline base64)
- [ ] **Tone** is accessible — a newcomer can follow the guide
- [ ] **No duplication** — references Object/Frame docs instead of repeating their content
