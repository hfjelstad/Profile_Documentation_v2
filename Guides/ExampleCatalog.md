# Example Catalog (NeTEx Profile)

Purpose
- Provide a single, searchable catalog of all NeTEx examples in the profile (both complete examples and isolated fragments).
- Help implementers discover which examples demonstrate which profile sections and validation rules.

Conventions
- File naming:
  - Example_<Object>_(Minimal|Full).xml for valid examples that illustrate minimal vs. extended cardinalities.
  - Example_<Object>_Invalid_<RuleKey>.xml for intentionally invalid examples that correspond to a specific validation rule.
- Codespace: All XML examples use the ERP codespace in identifiers.

How to use this catalog
- Each entry lists metadata: Title, File path, Object(s), Frame(s), Profile sections demonstrated, Relevant validation rules, Cardinality variant, Conformance level, Known pitfalls, Related documents.
- “Planned” entries indicate examples referenced by documentation or requested but not yet committed; they are placeholders until the XML is added.

---

Catalog

| Title | File path | Object(s) | Frame(s) | Profile sections demonstrated | Relevant validation rules | Cardinality variant | Conformance level | Known pitfalls | Related documents |
|---|---|---|---|---|---|---|---|---|---|
| Line – Example (planned) | Objects/Line/Example_Line.xml | Line | N/A (fragment) | Line object description and table | See Validation Guide (Line) | TBD (Minimal/Full) | Profile-compliant | Ensure Name or PublicCode is present | Objects/Line/Table_Line.md |
| ScheduledStopPoint – Example (planned) | Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml | ScheduledStopPoint | N/A (fragment) | ScheduledStopPoint description and table | See Validation Guide (ScheduledStopPoint) | TBD (Minimal/Full) | Profile-compliant | Provide PassengerStopAssignment where applicable | Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md |
| ServiceJourney – Example (planned) | Objects/ServiceJourney/Example_ServiceJourney.xml | ServiceJourney | N/A (fragment) | ServiceJourney description | See Validation Guide (ServiceJourney) | TBD (Minimal/Full) | Profile-compliant | Ensure JourneyPatternRef is resolved | Objects/ServiceJourney/Description_ServiceJourney.md |
| VehicleType – Example (if available) | Objects/VehicleType/Example_VehicleType.xml | VehicleType | N/A (fragment) | VehicleType description/table | See Validation Guide (VehicleType) | TBD (Minimal/Full) | Profile-compliant | Verify vehicle mode/type consistency | Objects/VehicleType/Table_VehicleType.md |

Notes
- “N/A (fragment)” indicates the example is expected to be a focused fragment rather than a complete multi-frame dataset. When a full dataset is provided, update the Frame(s) column accordingly (e.g., ResourceFrame, ServiceFrame).

Planned invalid examples (placeholders)
- Objects/Line/Example_Line_Invalid_MissingNameOrPublicCode.xml — Demonstrates failure when Line lacks Name and PublicCode.
- Objects/ScheduledStopPoint/Example_ScheduledStopPoint_Invalid_NoPassengerStopAssignment.xml — Demonstrates failure when a ScheduledStopPoint misses a required PassengerStopAssignment.
- Objects/ServiceJourney/Example_ServiceJourney_Invalid_MissingJourneyPatternRef.xml — Demonstrates failure when ServiceJourney lacks JourneyPatternRef or it cannot be resolved.

Maintenance
- Update this catalog whenever a new example XML is added or when rules/sections evolve. Keep titles concise and prefer a single, canonical example per rule unless variants are necessary.
