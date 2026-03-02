# Contract – table

| Element | Type | Cardinality | Notes |
|---|---|---:|---|
| id | Identifier | 1 | Unique identifier within the ERP codespace (e.g., ERP:Contract:CON-001). |
| version | Version | 1 | Version of the Contract entity. The pair [id + version] must be unique within a document. |
| Name | xsd:normalizedString | 0..1 | Human-readable name of the contract. Recommended. |
| Description | xsd:normalizedString | 0..1 | Short description of the agreement and its purpose. |
| ValidBetween | ValidityConditionsStructure | 0..1 | Overall validity window for the agreement. If omitted, validity may be implied by the enclosing frame or dataset. |
| contractees | OrganisationRef (list) | 0..* | Client-side organisations that receive the service (e.g., Authority). Use OrganisationRef. |
| contractors | OrganisationRef (list) | 0..* | Supplier-side organisations that deliver the service (e.g., Operator). Use OrganisationRef. |
| ResponsibilitySetRef | ResponsibilitySetRef | 0..1 | Optional governance/data stewardship reference for the Contract. |
| ResponsibilityRoleAssignmentRef | ResponsibilityRoleAssignmentRef | 0..* | Optional references to role assignments relevant to the Contract. |
| LineRef | LineRef (list) | 0..* | Optional scope reference to Lines covered by the contract. Subject to further study in the profile. |
| GroupOfLinesRef | GroupOfLinesRef (list) | 0..* | Optional scope reference to groups of lines. Subject to further study in the profile. |
