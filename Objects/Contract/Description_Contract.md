# Contract – description

Purpose: Defines the legal or commercial agreement that governs responsibilities, rights, and obligations between parties (e.g., an Authority and an Operator) for providing, operating, selling, or publishing public transport services or data. Contract is part of NeTEx v2.0 (Part 3) and is referenced across frames to indicate governance and accountability.

Typical elements:
- ContractType: Form of contract (e.g., written, oral, formal). Enumeration in the XSD.
- LegalStatus: Optional description of legal status or registration details.
- ContractGoverningLaw: Jurisdiction or legal code (e.g., country code) governing the contract.
- contractees: The party or parties benefiting from the contract (each Contractee has an OrganisationRef).
- contractors: The party or parties performing under the contract (each Contractor has an OrganisationRef).
- Name/Description: Optional descriptive labeling.
- ValidBetween / validityConditions: Optional validity windows.

Keys:
- Identification: @id and @version are mandatory for the Contract object and follow the profile’s codespace conventions (use ERP:Contract:{LocalId}).
- References: ContractRef is a reference structure with attributes ref, versionRef, and nameOfRefClass, and is used by other elements to point to a Contract. In this profile, ContractRef is used by ResponsibilitySetAssignment and ResponsibilityRoleAssignment to express which Contract applies to a given scope or role.
- Placement: In NeTEx v2.0, Contract instances are defined under SalesTransactionFrame (Part 3). In this profile’s examples, documentation for Contract is grouped under Objects, and cross-referenced from relevant frames.
