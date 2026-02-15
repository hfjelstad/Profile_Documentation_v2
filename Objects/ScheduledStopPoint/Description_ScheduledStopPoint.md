# ScheduledStopPoint

Purpose
- ScheduledStopPoint represents a logical (planned) stopping point used by service journeys and journey patterns. It is the anchor for passenger stop assignments to physical quays.

Scope and assumptions
- ScheduledStopPoint lives in the ServiceFrame and is referenced by StopPointInJourneyPattern via ScheduledStopPointRef.
- The link to a physical stopping place (Quay) is modelled through PassengerStopAssignment.

Identification and namespace
- All identifiers MUST be scoped to the ERP codespace (e.g., ERP:ScheduledStopPoint:1001).
- Examples and IDs in this profile use the ERP namespace consistently.

Key relationships
- ScheduledStopPointRef: Referenced from StopPointInJourneyPattern.
- PassengerStopAssignment: Maps a ScheduledStopPoint to a Quay (and thus to a StopPlace).
- Quay/StopPlace: Physical infrastructure elements defined in SiteFrame.

Business rules
- The combination of id and version uniquely identifies a ScheduledStopPoint.
- When used for timetables, each referenced ScheduledStopPoint MUST have a valid PassengerStopAssignment to an existing Quay within the same delivery or an external referenced frame.
- TimingPointStatus SHOULD be set when applicable to support punctuality checks (e.g., timingPoint).

Validation checklist
- [ ] File content is written in English.
- [ ] All IDs are ERP-scoped (prefix ERP:...).
- [ ] If used in journey patterns, each ScheduledStopPoint has a corresponding PassengerStopAssignment.

See also
- Objects/ScheduledStopPoint/Table_ScheduledStopPoint.md for the property specification table.
- Objects/ScheduledStopPoint/Example_ScheduledStopPoint.xml for a minimal NeTEx example with ERP namespace.
