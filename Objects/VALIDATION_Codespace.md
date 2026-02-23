# Codespace Validation Checklist

Use this checklist to verify codespace usage in NeTEx deliveries.

- All IDs SHALL be scoped to the producer’s own codespace (documentation examples use ERP: as a placeholder).
- ParticipantRef in PublicationDelivery MUST equal the producer’s codespace (e.g., OPR).
- id + version uniquely identifies each object within the chosen codespace.
- References (Ref/@ref) MUST resolve within the same PublicationDelivery or an explicitly referenced external frame that is available to the recipient.
- Do not mix multiple codespaces in the same delivery unless explicitly required and documented via an external frame.
