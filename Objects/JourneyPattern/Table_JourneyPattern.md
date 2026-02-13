# Table — JourneyPattern

Formål
- Oppsummere kjernefelter, kardinalitet og konvensjoner slik at produsenter og konsumenter kan validere struktur konsekvent på tvers av objektene.

Relaterte filer
- Example: [Example_JourneyPattern.xml](Example_JourneyPattern.xml)
- Beskrivelse: [Description_JourneyPattern.md](Description_JourneyPattern.md)

Kjerneelementer (på JourneyPattern)
- id: Netex ID
  - Påkrevd: ja
  - Eksempel: ERP:JourneyPattern:JP_10_out
- version: String (typisk "1")
  - Påkrevd: ja
  - Eksempel: 1
- Name: Menneskelesbart navn
  - Påkrevd: anbefalt (profilkrav)
  - Eksempel: "Line 10 Outbound"
- RouteRef: Referanse til Route
  - Påkrevd: ja
  - Eksempel: ref=ERP:Route:10
- DirectionType: inbound | outbound | clockwise | anticlockwise | unknown
  - Påkrevd: når relevant
  - Eksempel: outbound
- pointsInSequence/StopPointInJourneyPattern (1..n)
  - order (1..n, uten hull) — Påkrevd
  - ScheduledStopPointRef — Påkrevd, ref til planlagt stoppunkt
  - Eksempler:
    - order=1, ScheduledStopPointRef=ERP:ScheduledStopPoint:10:001
    - order=2, ScheduledStopPointRef=ERP:ScheduledStopPoint:10:002

Valgfrie elementer
- JourneyPatternSectionRef (for gjenbruk av delstrekninger)
  - Påkrevd: nei

Konvensjoner for ID-er (ERP codespace)
- JourneyPattern: ERP:JourneyPattern:{RouteKode}_{Variant}
  - Eksempel: ERP:JourneyPattern:JP_10_out
- StopPointInJourneyPattern: ERP:SPiJP:{JourneyPatternId}:{order}
  - Eksempel: ERP:SPiJP:JP_10_out:3
- ScheduledStopPoint: ERP:ScheduledStopPoint:{RouteKode}:{Løpenr}
  - Eksempel: ERP:ScheduledStopPoint:10:003
- Route: ERP:Route:{RouteKode}
  - Eksempel: ERP:Route:10
- ServiceFrame (ramme for JourneyPattern): ERP:ServiceFrame:{Navn}
  - Eksempel: ERP:ServiceFrame:Line_10

Namespace og innpakking
- XML-eksempel følger Netex default namespace (http://www.netex.org.uk/netex) og pakkes i PublicationDelivery.
- ParticipantRef settes til ERP for å gjenspeile codespace.
- JourneyPattern hører naturlig hjemme i ServiceFrame (i motsetning til ServiceJourney som ofte vises i TimetableFrame i eksempler).

Valideringsregler (kort)
- Minst ett StopPointInJourneyPattern finnes.
- order-verdier er unike og uten hull (1..n).
- Alle ScheduledStopPointRef finnes i samme Route som RouteRef peker på.
