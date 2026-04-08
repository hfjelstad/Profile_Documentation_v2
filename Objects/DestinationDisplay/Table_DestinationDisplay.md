# DestinationDisplay

## Structure Overview

```text
DestinationDisplay
  ├─ @id (1..1)
  ├─ @version (1..1)
  ├─ Name (0..1)
  ├─ FrontText (1..1)
  └─ SideText (0..1)
```

## Table

| Element | Type | XSD | ERP | NP | Description | Path |
|---------|------|-----|-----|-----|-------------|------|
| @id | ID | 1..1 | 1..1 | 1..1 | Unique identifier for the destination display | DestinationDisplay/@id |
| @version | String | 1..1 | 1..1 | 1..1 | Version number for change tracking | DestinationDisplay/@version |
| Name | String | 0..1 |  | 0..1 | Internal name for the destination display definition | DestinationDisplay/Name |
| FrontText | String | 0..1 | 1..1 | 1..1 | Text shown on the vehicle's destination display | DestinationDisplay/FrontText |
| SideText | String | 0..1 |  | 0..1 | Text shown on the side display of a vehicle | DestinationDisplay/SideText |
