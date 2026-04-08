## Structure Overview

```text
Contract
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ Name (0..1)
 ├─ ContractType (0..1)
 ├─ LegalStatus (0..1)
 ├─ ContractGoverningLaw (0..1)
 ├─ contractees (0..1)
 │  └─ OrganisationRef/@ref (0..n)
 └─ contractors (0..1)
    └─ OrganisationRef/@ref (0..n)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the Contract | Contract/@id |
| @version | String | 1..1 | Version label | Contract/@version |
| Name | String | 0..1 | Human-readable name of the contract | Contract/Name |
| ContractType | Enum | 0..1 | Form of contract (written, oral, formal) | Contract/ContractType |
| LegalStatus | String | 0..1 | Legal standing of the contract | Contract/LegalStatus |
| ContractGoverningLaw | String | 0..1 | Jurisdiction or legal code governing the contract | Contract/ContractGoverningLaw |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | 0..1 | Client-side organisation (contractee) | Contract/contractees/OrganisationRef/@ref |
| [Operator](../Operator/Table_Operator.md)@ref | Reference | 0..1 | Supplier-side organisation (contractor) | Contract/contractors/OrganisationRef/@ref |
