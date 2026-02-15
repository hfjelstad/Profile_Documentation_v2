# Table – Quay

Feltoversikt for Quay-objekt i profilen. Dette er et utgangspunkt og kan utvides ved behov.

- id (påkrevd)
  - Format: ERP:Quay:<lokal-id>
  - Beskrivelse: Stabil, globalt unik identifikator.
- version (påkrevd)
  - Standard: 1 ved første versjon.
- Name (påkrevd)
  - Navn som vises for brukere.
- PublicCode (anbefalt)
  - Plattform-/spor-kode slik den vises for publikum (f.eks. «A», «1», «Spor 3»).
- ParentSiteRef (påkrevd)
  - Ref til overordnet StopPlace.
- Centroid/Location (anbefalt)
  - Geografisk posisjon (Latitude/Longitude).
- AccessibilityAssessment (valgfri)
  - Tilgjengelighetsattributter ved behov.
- Description (valgfri)
  - Utfyllende beskrivelse.

Relasjoner
- StopPlace —(har)→ Quay
