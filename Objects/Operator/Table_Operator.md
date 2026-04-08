## Structure Overview

```text
Operator
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ CompanyNumber (0..1)
 ├─ Name (1..1)
 ├─ ShortName (0..1)
 ├─ LegalName (0..1)
 ├─ ContactDetails (0..1)
 │  ├─ Phone (0..1)
 │  └─ Url (0..1)
 ├─ OrganisationType (0..1)
 ├─ CustomerServiceContactDetails (0..1)
 │  ├─ Email (0..1)
 │  ├─ Phone (0..1)
 │  └─ Url (0..1)
 ├─ AuthorityRef/@ref (0..1)
 └─ ResponsibilitySetRef/@ref (0..1)
```

## Table

| Element | Type | XSD | ERP | NP | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the Operator | Operator/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version label | Operator/@version |
| Name | String | 0..1 |  | 1..1 | Name of the Operator organisation | Operator/Name |
| CompanyNumber | String | 0..1 |  | 0..1 | Official company registration number | Operator/CompanyNumber |
| ShortName | String | 0..1 |  |  | Abbreviated name | Operator/ShortName |
| LegalName | String | 0..1 |  | 0..1 | Official legal name of the operator | Operator/LegalName |
| ContactDetails | Element | 0..1 |  | 0..1 | Contact information (phone, email, website) | Operator/ContactDetails |
| Phone | String | 0..1 |  | 0..1 | Contact telephone number | Operator/ContactDetails/Phone |
| Url | String | 0..1 |  | 0..1 | Website URL | Operator/ContactDetails/Url |
| CustomerServiceContactDetails | Element | 0..1 |  | 0..1 | Public-facing customer service contact details | Operator/CustomerServiceContactDetails |
| Email | String | 0..1 |  | 0..1 | Customer service email | Operator/CustomerServiceContactDetails/Email |
| Phone | String | 0..1 |  | 0..1 | Customer service phone | Operator/CustomerServiceContactDetails/Phone |
| Url | String | 0..1 |  | 0..1 | Customer service URL | Operator/CustomerServiceContactDetails/Url |
| OrganisationType | String | 0..1 |  | 0..1 | Type of organisation (e.g., company, cooperative) | Operator/OrganisationType |
| [Authority](../Authority/Table_Authority.md)@ref | Reference | 0..1 |  |  | Reference to the contracting Authority | Operator/AuthorityRef/@ref |
| [ResponsibilitySet](../ResponsibilitySet/Table_ResponsibilitySet.md)@ref | Reference | 0..1 |  |  | Reference to a ResponsibilitySet defining roles | Operator/ResponsibilitySetRef/@ref |
