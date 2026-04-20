<!-- LLM AGENT: Use LLM/README.md as startingpoint  --> 
# NeTEx Profile Documentation

![Urban transit at Jernbanetorget, Oslo](assets/images/Jernbanetorget.png)

A practical reference, learning resource, and example library for working with [NeTEx](https://github.com/NeTEx-CEN/NeTEx) — the European XML standard for exchanging public transport data (timetables, fares, stops, and more).

- 📘 **Learn** the concepts and structure of NeTEx
- 🧭 **Navigate** frames, objects, and modeling patterns
- 🗂️ **Explore** a validated example library built against the official XSD
- 🔎 **Reference** element ordering, cardinality, and profile-specific requirements

---

## 🚀 Start here

Whether you're new to NeTEx or looking to structure transport data for exchange, start with the [**Get Started guide**](Guides/GetStarted/GetStarted_Guide.md) — it introduces the core concepts, explains how frames and objects fit together, and walks you through a real NeTEx document step by step.

Already familiar with NeTEx? Jump straight to the [**Table of Contents**](LLM/Indexes/TableOfContent.md) to find the frame, object, or guide you need.

---

## 🎯 What's Inside

For every NeTEx frame and object you will find:

- **`Description`** — purpose, structure overview, key elements, and relationships
- **`Table`** — element-level specification with types, cardinality per profile, and XSD paths
- **`Example`** — one or more XML examples validated against the NeTEx 2.0 XSD

All examples follow the standard delivery pattern (`PublicationDelivery → dataObjects → Frame → …`), validate against the current XSD (see [Validation guide](Guides/Validation/Validation.md)), and can be provided in different profiles.

---

## 🏷️ Profiles

NeTEx is a large standard — a profile selects which elements to use, how they should be combined, and what level of detail is expected for a given context. Profiles make the standard practical by narrowing it down to a clear, implementable subset.

This documentation uses profiles to specify cardinality and requirements per element. Each object table shows which elements are mandatory, optional, or unused for each profile, and XML examples are provided per profile where relevant.

---

## 🗂️ Documentation Structure

```
📚 Guides
 └── <GuideName>
      └── <GuideName>.md

🏗️ Frames
 └── <FrameName>
      ├── Description_<FrameName>.md
      ├── Table_<FrameName>.md
      └── Example_<FrameName>.xml

📦 Objects
 └── <ObjectName>
      ├── Description_<ObjectName>.md
      ├── Table_<ObjectName>.md
      └── Example_<ObjectName>_<Profile>.xml
```

This structure is designed to be equally usable by humans browsing the documentation and by LLMs operating as chat agents or assisting with NeTEx data modelling. 🤖
