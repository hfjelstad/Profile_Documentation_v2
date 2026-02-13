# Beskrivelse: ServiceJourney

Denne siden beskriver objektet ServiceJourney (planlagt reise) slik det brukes i profilen. Dokumentet følger samme struktur og innholdsnivå som for DatedServiceJourney-beskrivelsen, men er tilpasset planlagte (ikke-daterte) turer.

Formålet er å gi en kortfattet, operativt nyttig forklaring av hva ServiceJourney er, hvordan det henger sammen med øvrige objekter, og hvilke felter som er sentrale. Detaljerte feltbeskrivelser finnes i tabellen for ServiceJourney.

Relaterte dokumenter:
- Tabell for ServiceJourney: Objects/ServiceJourney/Table_ServiceJourney.md
- Dato-instans av tur: Objects/DatedServiceJourney/Description_DatedServiceJourney.md

## Hva er ServiceJourney?
ServiceJourney representerer en planlagt tur i ruteplanen. Den beskriver hvilken linje/trasé og mønster (JourneyPattern) som kjøres, hvilke stoppsekvenser som gjelder gjennom referanse til mønsteret, og metaopplysninger som operatør, koder og eventuelle lenker til blokker/omløp. Selve passeringstidene for ServiceJourney er normalt avledet fra mønster og tidtabellregler; den daterte varianten (DatedServiceJourney) uttrykker samme tur på en konkret driftsdato.

## Nøkkelrelasjoner
- Line/Route: ServiceJourney er knyttet til en linje/trasé via relevante referanser.
- JourneyPattern: Angir stoppsekvensen og struktur for kjøremønsteret som turen bruker.
- Operator: Hvilken operatør som utfører turen.
- Block/VehicleJourneyGroup (der det brukes): Kobling til omløp/blokk for å sikre sammenheng mellom påfølgende turer.
- DayType/OperatingDays: Angir hvilke dager turen normalt kjøres (logikk for faktisk kjøring per dato ligger i daterte instanser og/eller produksjonsregler).

## Sentrale felter
Se tabellen Objects/ServiceJourney/Table_ServiceJourney.md for komplette felt og kardinalitet. Typiske nøkler og identifikatorer omfatter:
- id, version
- privateCode/publicCode (interne/viste koder)
- journeyPatternRef (referanse til valgt mønster)
- lineRef/routeRef (tilhørende linje/trasé)
- operatorRef
- dayTypeRefs/operatingProfile (hvilke dager turen gjelder)
- blockRef (omløp), gir kjedingen av turer der dette er i bruk

## Forretningsregler (oversikt)
- En ServiceJourney skal peke til ett gyldig JourneyPattern. Mønsterets stoppsekvens er autoritativ for turen.
- En ServiceJourney bør tilhøre én linje/trasé; inkonsistente referanser (f.eks. mønster fra annen linje) er ikke tillatt.
- Dersom block/omløp benyttes, skal turer i samme blokk være tidsmessig kompatible uten overlapp for samme kjøretøy.
- DayType/OperatingProfile styrer planlagt kjøring; avvik per dato håndteres på DatedServiceJourney-nivå.

## Sammenligning med DatedServiceJourney
- ServiceJourney = mal/plan for turen uten konkret dato.
- DatedServiceJourney = konkret instans av en tur på en gitt dato, med eventuelle avvik (erstatning, forsterkning, m.m.).
- Felt knyttet til ServiceAlteration og dato-spesifikke endringer tilhører DatedServiceJourney, ikke ServiceJourney.

## Datakvalitet og validering (anbefaling)
- Valider at journeyPatternRef, lineRef og operatorRef faktisk finnes og er konsistente.
- Sikre at DayType/OperatingProfile dekker forventet ruteplan og ikke skaper kollisjoner med andre regler.
- Bruk privateCode/publicCode konsekvent for sporbarhet og presentasjon.

## Eksempel
Eksempler for ServiceJourney kan legges til på tilsvarende måte som for DatedServiceJourney-eksemplene. Inntil de foreligger, benytt tabellen som referanse for feltnavn og strukturer.

## Endringslogg
- 2026-02-13: Første versjon av beskrivelsen, tilpasset fra DatedServiceJourney-malen.
