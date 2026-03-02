| Element | Type | Cardinality | Notes |
|---|---|---|---|
| FareContract/@id | Identifier | 1 | Use ERP codespace (e.g., ERP:FareContract:FC_1). Unique within dataset. |
| FareContract/@version | Version | 1 | Version of the contract object. |
| TypeOfFareContractRef | TypeOfFareContractRefStructure | 1 | Classifies the contract (e.g., standard, subscription). |
| CustomerAccountRef | CustomerAccountRefStructure | 0..1 | Links the contract to a customer account for identification and after-sales. |
| entries | Container | 1 | Container for one or more FareContractEntry elements. |
| FareContractEntry/@id | Identifier | 1 | Unique id for the contract entry; use ERP codespace (e.g., ERP:FareContractEntry:FCE_1). |
| FareContractEntry/@version | Version | 1 | Version of the entry object. |
| CustomerPurchasePackageRef | CustomerPurchasePackageRefStructure | 1 | References the purchased package granting rights to travel. |
| TravelSpecificationRef | TravelSpecificationRefStructure | 0..1 | Optionally constrains or describes the intended travel scope. |