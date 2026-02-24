# Validation Guide (NeTEx Profile)

Purpose
- Provide a consolidated guide for validating NeTEx data against the profile.
- Clarify what to validate (syntax, structure, references, and profile rules) and where to find rule definitions and examples.

Scope and audience
- Intended for publishers, integrators and validator implementers working with the profile.
- Applies to both full datasets (multi-frame) and isolated example fragments.

1) XSD validation against the profile schema
- Always validate XML against the profile’s NeTEx XSDs (not only generic NeTEx): ensure your validator uses the profile-specific schema set.
- Use an XML Catalog (or equivalent) to resolve schema locations consistently; avoid remote HTTP lookups in CI.
- Codespace: All example identifiers use the ERP codespace. Validators may enforce codespace constraints if defined by the profile.
- Outcome: Documents must be well-formed and schema-valid before any profile rule checks are evaluated.

2) Reference resolution across Frames
- All references (e.g., LineRef, JourneyPatternRef, StopPointRef, VehicleTypeRef) must resolve to an existing element within the same dataset across frames.
- For multi-frame deliveries (PublicationDelivery): ensure proper scoping via frame namespaces and versioning; if a ref uses an identifier with a codespace, that identifier must be unique and resolvable.
- Recommended checks:
  - Unresolved references (dangling refs) are errors.
  - Ambiguous identifiers across frames are errors unless explicitly versioned and disambiguated.
  - External refs must follow the profile’s referencing conventions.

3) Object-wise profile rules
- The authoritative rule sets are defined per object in the profile’s documentation. Start here:
  - Line: Objects/Line/Table_Line.md
  - ScheduledStopPoint: Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md
  - ServiceJourney: Objects/ServiceJourney/Description_ServiceJourney.md
- Typical constraints (non-exhaustive, see the tables above):
  - Line must provide at least Name or PublicCode.
  - ScheduledStopPoint must have required PassengerStopAssignment when applicable in the profile scope.
  - ServiceJourney must reference a valid JourneyPattern (JourneyPatternRef) and the reference must resolve.
- Implementations should map each table rule to an executable validator rule with a stable RuleKey.

4) Cross-cutting controls
- JourneyPattern vs. ServiceJourney consistency: ServiceJourney must align with JourneyPattern structure (StopPoints, timing links, etc.).
- Frame integrity: elements declared in a frame must be internally consistent (e.g., ResourceFrame/ServiceFrame references).
- Temporal and versioning checks: if the profile requires validity periods or versions, ensure these are coherent across interdependent elements.

5) Error catalog and example links
- The following intentionally invalid examples illustrate common failures. They are referenced from the Example Catalog and will be populated with concrete XML illustrating the error cases:
  - Objects/Line/Example_Line_Invalid_MissingNameOrPublicCode.xml — Line without Name and PublicCode.
  - Objects/ScheduledStopPoint/Example_ScheduledStopPoint_Invalid_NoPassengerStopAssignment.xml — ScheduledStopPoint missing required PassengerStopAssignment.
  - Objects/ServiceJourney/Example_ServiceJourney_Invalid_MissingJourneyPatternRef.xml — ServiceJourney missing or with unresolved JourneyPatternRef.

Conformance levels and cardinalities
- When the documentation distinguishes Minimal vs. Full/Extended cardinalities, validators should expose configuration for conformance level and report violations accordingly.

Outputs and reporting
- Each rule should have a stable identifier (RuleKey), severity (Error/Warning), location (XPath or element id), and a clear message. Link to a concrete example when available.

Maintenance
- Keep this guide aligned with object tables and the “Data quality and validation” sections. Update references when rule documents or examples are added or moved.
