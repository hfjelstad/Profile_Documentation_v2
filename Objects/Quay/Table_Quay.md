# Quay – Property specification

This table defines the minimal profile subset for a Quay.

| Property      | Type    | Card. | Description                                                                                 | Example                 |
|---------------|---------|-------|---------------------------------------------------------------------------------------------|-------------------------|
| id            | string  | 1     | ERP-scoped NeTEx identifier. Use the pattern `ERP:Quay:<localId>`                           | ERP:Quay:1001          |
| version       | string  | 1     | Version of this Quay object                                                                  | 1                       |
| Name          | string  | 1     | Passenger-facing quay name                                                                   | Platform A              |
| PublicCode    | string  | 0..1  | Short public code printed on signage                                                         | A                       |
| StopPlaceRef  | ref     | 1     | Reference to parent StopPlace. If Quay is embedded inside StopPlace, this may be implicit.  | ERP:StopPlace:100       |
| Centroid.Lat  | decimal | 1     | WGS84 latitude                                                                               | 59.9127                 |
| Centroid.Lon  | decimal | 1     | WGS84 longitude                                                                              | 10.7461                 |
| Description   | string  | 0..1  | Optional free text description                                                               | Northbound boarding bay |

Notes
- All examples and identifiers must use the ERP codespace (e.g., ERP:Quay:1001) and follow NeTEx conventions.
- A Quay must belong to exactly one StopPlace (via StopPlaceRef when delivered standalone, or by being embedded under that StopPlace).
- Provide a Centroid with both Latitude and Longitude.
