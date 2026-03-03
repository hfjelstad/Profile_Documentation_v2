# ResponsibilitySet

## Purpose
ResponsibilitySet defines the set of roles and organisations responsible for managing data, operations, or contractual obligations within a defined scope in a NeTEx dataset. It is used to express who is accountable for specific responsibilities and how these responsibilities apply within a frame or other scope.

## Typical elements
- ResponsibilityRoleAssignment: associates a role with a responsible organisation (e.g., an Authority or an Operator).
- ResponsibilitySetAssignment (reference): binds a ResponsibilitySet to a concrete scope (e.g., a Frame) and may constrain it by contract.
- ContractRef usage: used to indicate that the responsibility applies under a specific contract.
- Links to Authority/Operator: ResponsibilityRoleAssignment typically points to an Authority or an Operator as the responsible organisation.

## Keys
- id
- version
- ResponsibilitySetRef (used from ResponsibilitySetAssignment)
- OrganisationRef (used from ResponsibilityRoleAssignment)
- ContractRef (used from ResponsibilitySetAssignment)

## Placement
ResourceFrame

## See also
- ../Authority/Description_Authority.md
- ../Operator/Description_Operator.md
- ../Contract/Description_Contract.md
- ../../Frames/ResourceFrame/Description_ResourceFrame.md