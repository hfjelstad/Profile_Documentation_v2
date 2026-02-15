# Quay

Overview
- A Quay represents a specific boarding or alighting position within a StopPlace. It is the precise place where passengers meet the vehicle (for example, a platform, stand, or bay).

Scope and intent
- Quays are used to provide passenger-facing names/codes and a geospatial position that can be used for wayfinding, passenger information and vehicle docking.

Key elements (profile subset)
- id (required): ERP-scoped identifier using the pattern "ERP:Quay:<localId>".
- version (required): Version of this Quay, typically "1" for first publication.
- Name (required): Passenger-facing name of the quay.
- PublicCode (optional): Short public-facing code printed on signage (e.g., "A", "B2").
- StopPlaceRef (required): Reference to the parent StopPlace.
- Centroid (required): Geographic position of the quay (WGS84 latitude/longitude).
- Description (optional): Additional free text description of the quay.

Profile rules
- All examples and identifiers must use the ERP codespace (e.g., ERP:Quay:1001) and be valid NeTEx identifiers.
- A Quay must belong to exactly one StopPlace through StopPlaceRef.
- Provide a Centroid with both Latitude and Longitude.
- Use English language for all documentation and example text.

Example location
- See Objects/Quay/Example_Quay.xml for a minimal, ERP-compliant NeTEx example.

Notes
- Additional properties (accessibility, equipment, level, etc.) may be added as needed by the profile, but are not mandatory in the minimal subset shown here.
