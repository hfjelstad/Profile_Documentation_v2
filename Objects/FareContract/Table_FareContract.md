## Structure Overview

```text
FareContract
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ TypeOfFareContractRef/@ref (1..1)
 ├─ CustomerAccountRef/@ref (0..1)
 └─ fareContractEntries (1..1)
    └─ FareContractEntry (1..n)
       ├─ @id (1..1)
       ├─ @version (1..1)
       ├─ CustomerPurchasePackageRef/@ref (1..1)
       └─ TravelSpecificationRef/@ref (0..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the FareContract | FareContract/@id |
| @version | String | 1..1 | Version label | FareContract/@version |
| TypeOfFareContractRef/@ref | Reference | 0..1 | Classifies the contract type (e.g., standard, subscription) | FareContract/TypeOfFareContractRef/@ref |
| CustomerAccountRef/@ref | Reference | 0..1 | Link to the customer account | FareContract/CustomerAccountRef/@ref |
| FareContractEntry/@id | ID | 1..1 | Unique identifier for the entry | FareContract/fareContractEntries/FareContractEntry/@id |
| FareContractEntry/@version | String | 1..1 | Version label for the entry | FareContract/fareContractEntries/FareContractEntry/@version |
| CustomerPurchasePackageRef/@ref | Reference | 0..1 | Reference to the purchased package | FareContract/fareContractEntries/FareContractEntry/CustomerPurchasePackageRef/@ref |
| TravelSpecificationRef/@ref | Reference | 0..1 | Optional travel scope constraint | FareContract/fareContractEntries/FareContractEntry/TravelSpecificationRef/@ref |
