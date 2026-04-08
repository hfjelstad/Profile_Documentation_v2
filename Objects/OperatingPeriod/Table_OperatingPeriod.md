## Structure Overview

```text
OperatingPeriod
 ├─ @id (1..1)
 ├─ @version (1..1)
 ├─ FromDate (1..1)
 └─ ToDate (1..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the operating period | OperatingPeriod/@id |
| @version | String | 1..1 | Version label | OperatingPeriod/@version |
| FromDate | xsd:dateTime | 1..1 | Start of the period (inclusive) | OperatingPeriod/FromDate |
| ToDate | xsd:dateTime | 1..1 | End of the period (inclusive) | OperatingPeriod/ToDate |
