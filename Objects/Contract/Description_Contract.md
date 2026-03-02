# Contract – description

Purpose
A Contract models an administrative/legal agreement at organisation/service level, not a customer fare agreement. It corresponds to the NeTEx class Contract and is used to capture the governing agreement between parties such as a Transport Authority and an Operator.

Scope and placement
- Not a FareContract: A FareContract is a customer agreement defined in Part 3 – Sales and lives in a SalesTransactionFrame. See also: Objects/FareContract/Description_FareContract.md
- Exchange placement: Until specified otherwise in the profile, Contract is proposed to be exchanged in a ResourceFrame that carries organisational and shared resource objects.
- Versioning: Contract is a versioned object and must carry @id and @version.

Minimum viable subset (profile MVP)
The profile initially supports the following Contract elements and relations:
- id (required)
- version (required)
- Name (optional but recommended)
- Description (optional)
- ValidBetween (optional)
- Involved organisations (Authority/Operator) via OrganisationRef. Use separate lists for contractees (clients) and contractors (suppliers) when available; otherwise a simple involved organisations list may be used by the profile.
- Optional references for responsibilities: ResponsibilitySetRef and/or ResponsibilityRoleAssignmentRef (optional, for governance and data stewardship where relevant)
- Optional scope references (subject to further study): LineRef, GroupOfLinesRef, or other scope-defining references that indicate which services the contract covers.

Conformance notes
- Uniqueness: The tuple [Contract id + version] must be unique within a single document.
- Codespace: All identifiers should use an assigned codespace. For examples in this profile, the ERP codespace is used (e.g., ERP:Contract:CON-001).

See also
- FareContract (customer agreement in SalesTransactionFrame)
