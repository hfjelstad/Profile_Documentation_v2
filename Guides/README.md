# Guide Structure Recommendations

To maintain a clear and scalable documentation structure for future guides, the following approach is recommended:

## **Folder Structure**
```
Guides/
  ├── NeTEx/
  │     ├── README.md
  │     ├── [GuideTopic1].md
  │     ├── [GuideTopic2].md
  │
  ├── GTFS/
  │     ├── README.md
  │     ├── [GuideTopic1].md
  │
  ├── OtherStandards/
  │     ├── README.md
  │     ├── [GuideTopic].md
  │
  └── README.md
```

### **Explanation:**
- **Guides/**: Root folder for all guides.
- **NeTEx/**: Contains all NeTEx-related guides.
- **GTFS/**: Contains all GTFS-related guides.
- **OtherStandards/**: For other formats or standards.

Each subfolder should have its own **README.md** that provides:
- An overview of the guides in that folder.
- Links to each guide file.

## **Splitting Information**
- Create **one guide per topic** for clarity and easier navigation.
- If a topic becomes too large, split it into multiple smaller guides and link them from the folder's README.md.

## **Main README.md (Guides/)**
- Provides a high-level overview of all available guide categories.
- Links to each subfolder (e.g., NeTEx, GTFS).

---

### **Example of NeTEx README.md**
```
# NeTEx Guides

This section contains guides related to NeTEx modeling and best practices.

- [Interchange and StopUse](Interchange_StopUse.md)
- [DatedServiceJourney Examples](DatedServiceJourney.md)
```

This structure ensures scalability and easy navigation as the number of guides grows.