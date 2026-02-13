# Route

Kort oppsummering
- Route beskriver den overordnede kjørettraséen for en linje. JourneyPattern er varianter/undermønstre av en Route (med konkret stoppsekvens pr. variant).
- ServiceJourney følger ett JourneyPattern, og JourneyPattern refererer tilbake til én Route.

Mål og bruksområde
- Gi et entydig anker for traséen som ulike varianter (JourneyPattern) bygger på.
- Skille mellom logisk trasé (Route) og operativ stoppsekvens (JourneyPattern) og avganger (ServiceJourney/DatedServiceJourney).

Relasjoner til andre objekter
- Line: Route hører til en Line (LineRef).
- JourneyPattern: Én Route kan ha 1..n JourneyPattern-varianter.
- ScheduledStopPoint: Stedene som brukes i JourneyPattern er planlagte stoppunkter innenfor samme ServiceFrame som Route.

Kjernefelt (minstekrav i profilen)
- id (NeTEx ID)
- version (ofte "1" for første versjon)
- name (menneskelesbart navn, f.eks. "Line 10 Main Route")
- LineRef (anbefalt når tilgjengelig)

Regler og anbefalinger
- Bruk konsistente navn og koder på tvers av Line, Route og JourneyPattern.
- Dersom Route modelleres med punktsekvens (pointsOnRoute), anbefales samme stoppunivers som brukes av JourneyPattern (ScheduledStopPoint) i samme ServiceFrame.
- Hold ID-er og codespace konsistent med resten av profilen (ERP i disse eksemplene).

Eksempel
Se komplett XML-eksempel i Example_Route.xml.

Avgrensninger og notater
- Route inneholder ikke passeringstider; tider modelleres gjennom ServiceJourney (passingTimes) og daterte forekomster i DatedServiceJourney.
- Route er logisk trasé; variasjoner og alternative løp håndteres med egne JourneyPattern knyttet til Route.

Endringslogg
- v1 (2026-02-13): Første beskrivelse med relasjoner og anbefalinger.