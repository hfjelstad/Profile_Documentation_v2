# StopPlace – beskrivelse

Kort definisjon
- Et navngitt sted der passasjerer kan gå på/av kollektivtransport. Kan være en bygning/område (stasjon/terminal) eller et punkt i gatebildet.

Begreper og typer
- Monomodal StopPlace: én transporttype og én eller flere Quay-er (holdeplassposisjoner).
- Multimodal StopPlace (parent): samler minst to monomodale StopPlace. Har ingen egne Quay-er.
- GroupOfStopPlaces: grupperer flere StopPlace for felles referanse (f.eks. by/hub).

Kjerneattributter (utdrag)
- id, version, created, changed, modification
- Name, alternativeNames
- TransportMode (+ ev. Submode)
- StopPlaceType (påkrevd når StopPlace har Quay-er; ikke påkrevd for multimodal parent)
- tariffZones (TariffZoneRef)
- TopographicPlaceRef (by/sted)
- ParentSiteRef (peker til multimodal parent)
- keyList (KeyValue)
- Geometri: Centroid (punkt). For arealer kan AccessSpace ha polygoner.
- Tilgjengelighet/navigasjon: accessSpaces, pathLinks, pathJunctions, navigationPaths

Regler og relasjoner
- Quay tilhører nøyaktig én (mono) StopPlace. Monomodal StopPlace må ha minst én Quay. Multimodal parent har 0 Quay.
- ScheduledStopPoint knyttes til StopPlace/Quay via PassengerStopAssignment i ServiceFrame.

Plassering (anbefalinger, kort)
- Quay: på faktisk ombord/avstigningspunkt.
- StopPlace: som hovedregel midt mellom tilhørende Quay-er, eller sentralt i området (for terminal/stasjon).
- Multimodal: parent uten Quay; underordnede monomodale StopPlace for hver transporttype.

Se også
- [Table_StopPlace.md](./Table_StopPlace.md)
- [Example_StopPlace.xml](./Example_StopPlace.xml)
