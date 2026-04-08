## Structure Overview

```text
ResponsibilitySet
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 └─ roles (0..1)
    └─ ResponsibilityRoleAssignment (0..n)
       ├─ @id (1..1)
       ├─ @version (1..1)
       ├─ ResponsibleOrganisationRef/@ref (0..1)
       ├─ TypeOfResponsibilityRoleRef/@ref (0..1)
       └─ AssociatedContract (0..1)
          └─ ContractRef/@ref (0..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the ResponsibilitySet | ResponsibilitySet/@id |
| @version | String | 1..1 | Version label | ResponsibilitySet/@version |
| Name | String | 0..1 | Human-readable name of the responsibility set | ResponsibilitySet/Name |
| ResponsibilityRoleAssignment/@id | ID | 1..1 | Unique identifier for the role assignment | ResponsibilitySet/roles/ResponsibilityRoleAssignment/@id |
| ResponsibilityRoleAssignment/@version | String | 1..1 | Version label | ResponsibilitySet/roles/ResponsibilityRoleAssignment/@version |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | 0..1 | Reference to the responsible organisation | ResponsibilitySet/roles/ResponsibilityRoleAssignment/ResponsibleOrganisationRef/@ref |
| TypeOfResponsibilityRoleRef/@ref | Reference | 0..1 | Reference to the role type qualifier | ResponsibilitySet/roles/ResponsibilityRoleAssignment/TypeOfResponsibilityRoleRef/@ref |
| [Contract](../Contract/Table_Contract.md)@ref | Reference | 0..1 | Reference to the governing contract | ResponsibilitySet/roles/ResponsibilityRoleAssignment/AssociatedContract/ContractRef/@ref |
