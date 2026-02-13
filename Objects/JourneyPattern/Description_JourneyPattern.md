# JourneyPattern

Kort oppsummering
- JourneyPattern beskriver den faktiske stoppsekvensen som en linje kjører for en retning på en rute, dvs. hvilke planlagte holdeplasspunkter som inngår og i hvilken rekkefølge.
- ServiceJourney peker til ett (og bare ett) JourneyPattern for å indikere hvilken sekvens av stopp den følger.

Mål og bruksområde
- Gi produsenter og konsumenter et entydig grunnlag for å forstå hvilken trasé en tjenestereise følger, uavhengig av kalender og passeringstider.
- Brukes når samme rute har flere varianter (avstikkere, kort-/langløp, retning). Hver variant beskrives som et eget JourneyPattern.

Relasjoner til andre objekter
- Route: JourneyPattern må referere til én Route (RouteRef) som det er en variant av.
- ServiceJourney: Hver ServiceJourney refererer til nøyaktig ett JourneyPattern.
- StopPointInJourneyPattern: En ordnet liste (1..n) som utgjør selve sekvensen. Hvert element peker til ett ScheduledStopPoint.
- JourneyPatternSection (valgfritt): Kan brukes for å gjenbruke delstrekninger (lenkesekvenser) på tvers av mønstre.

Kjernefelt (minstekrav i profilen)
- id (Netex ID)
- version (ofte "1" for første versjon)
- name (menneskelesbart navn, f.eks. "Linje 10 Retning Ut" eller kort variantnavn)
- RouteRef (lenker til ruten som mønsteret tilhører)
- DirectionType (inbound | outbound | clockwise | anticlockwise | unknown). Brukes når det er relevant for linjen.
- pointsInSequence/StopPointInJourneyPattern (1..n) med:
  - order (1..n, uten hull i sekvensen)
  - ScheduledStopPointRef (ref til planlagt stoppunkt)

Regler og anbefalinger
- Sekvensen må være sammenhengende: order starter på 1 og øker med 1 for hvert nytt punkt.
- Alle ScheduledStopPointRef i patternet skal tilhøre samme Route som RouteRef peker på.
- Angi DirectionType konsekvent for hele linjen der det gir mening (f.eks. outbound for fra sentrum, inbound for mot sentrum).
- Bruk name som gjør varianten lett å skille fra andre mønstre på samme rute (f.eks. "A-løp via Torget" vs. "B-løp via Sykehuset").

Eksempel (forkortet)
```xml
<!-- Minimal, illustrativt eksempel. Kommentarer er på engelsk for gjenbruk i tooling. -->
<JourneyPattern id="ERP:JourneyPattern:JP_10_out" version="1" name="Line 10 Outbound">
  <RouteRef ref="ERP:Route:10"/>
  <DirectionType>outbound</DirectionType>
  <pointsInSequence>
    <StopPointInJourneyPattern id="ERP:SPiJP:JP_10_out:1" version="1" order="1">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:10:001"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPiJP:JP_10_out:2" version="1" order="2">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:10:002"/>
    </StopPointInJourneyPattern>
    <StopPointInJourneyPattern id="ERP:SPiJP:JP_10_out:3" version="1" order="3">
      <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:10:003"/>
    </StopPointInJourneyPattern>
  </pointsInSequence>
</JourneyPattern>
```

Vanlige valideringer
- Det finnes minst ett StopPointInJourneyPattern.
- order-verdier er unike og uten hull (1..n).
- Alle ScheduledStopPointRef finnes og er konsistente med tilhørende Route.

Avgrensninger og notater
- JourneyPattern beskriver kun rekkefølgen av stopp, ikke passeringstider. Passeringstider hører til ServiceJourney (via passingTimes).
- Når mange mønstre deler lange like delstrekninger, vurder bruk av JourneyPatternSection for å unngå duplisering.

Endringslogg
- v1 (2026-02-13): Første komplette beskrivelse med eksempel og valideringsregler.
