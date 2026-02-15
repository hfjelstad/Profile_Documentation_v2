# Quay

Kort beskrivelse
- Quay (plattform/holdeplasskant) representerer et konkret påstignings-/avstigningspunkt innenfor en StopPlace.
- Brukes for å beskrive fysiske detaljer som navn/kode, geometri og tilhørighet til en StopPlace.

Profilregler (utdrag)
- id skal følge mønsteret ERP:Quay:<lokal-id>
- version skal settes, normalt «1» ved første versjon
- Name er påkrevd
- PublicCode anbefales hvis plattform-/spor-bokstav/tall vises for reisende
- Hver Quay skal ha én ParentSiteRef til en StopPlace
- Koordinater anbefales via Centroid/Location

Relasjoner
- StopPlace —(har)→ Quay

Se også
- Example_Quay.xml for et minimalt NeTEx-eksempel for profilbruk
- Table_Quay.md for feltoverikt
