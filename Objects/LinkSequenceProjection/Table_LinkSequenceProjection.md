## Structure Overview

```text
LinkSequenceProjection
 ├─ @id (1..1)
 ├─ @version (1..1)
 └─ gml:LineString (1..1)
    ├─ @srsName (1..1)
    └─ gml:posList (1..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the projection | LinkSequenceProjection/@id |
| @version | String | 1..1 | Version label | LinkSequenceProjection/@version |
| gml:LineString | GML Element | 0..1 | Geographic path geometry | LinkSequenceProjection/gml:LineString |
| @srsName | xsd:anyURI | 1..1 | Spatial reference system (e.g., `EPSG:4326`) | LinkSequenceProjection/gml:LineString/@srsName |
| gml:posList | gml:doubleList | 1..1 | Ordered coordinate pairs defining the line shape | LinkSequenceProjection/gml:LineString/gml:posList |
