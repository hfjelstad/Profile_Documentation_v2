# Codespace and Namespace Guidelines

This section defines how producers must scope identifiers and references in NeTEx deliveries.

- Codespace choice: Use a stable, unique codespace owned by the data producer (e.g., an organizational code such as OPR). Align the chosen codespace with PublicationDelivery/ParticipantRef for every delivery.
- Requirement: All IDs SHALL be scoped to the producer’s own codespace. Documentation examples use ERP: as a placeholder to illustrate the pattern. Parallel examples show OPR: to emphasize that ERP is not a requirement.
- Consistency: Use the same codespace consistently across all frames and objects in a delivery, unless there is an explicit intent to reference external frames.
- Resolving references: Any Ref/@ref used MUST resolve within the same PublicationDelivery or an explicitly referenced external frame available to the recipient at import time.
- Identity: id + version uniquely identifies an object within the chosen codespace.
- Mixing codespaces: Do not mix multiple codespaces in the same delivery unless this is explicitly required and documented through an external frame or a known shared namespace.

Validation notes
- Where documentation or validation checklists previously referred to an "ERP prefix", interpret this as the producer’s codespace prefix requirement.
- ParticipantRef MUST equal the producer’s codespace for the delivery (e.g., OPR). All object identifiers and references must use the same prefix.
