# Separation of Concerns i NeTEx

Denne guiden sammenfatter anbefalinger og mønstre for tydelig separasjon mellom passasjerinformasjon, operasjonell planlegging og infrastrukturkapasitet. Målet er å redusere koblinger på tvers av domener, gjøre integrasjoner enklere og forenkle vedlikehold, samtidig som man bevarer presis, operasjonell kontroll.

## 1. Domenekart

- Timetable (publisering) — TimetableFrame
  - Fokus: publikumsvendte data (linjer, ruter, stopp og tider).
  - Nøkkelobjekter: ServiceJourney, JourneyPattern, ScheduledStopPoint.
  - Relatert ramme: [ServiceFrame](../Frames/ServiceFrame/Description_ServiceFrame.md).

- Operasjon (ressurser/kjøretøy) — VehicleScheduleFrame
  - Fokus: faktisk drift og ressursdisponering.
  - Nøkkelobjekter: Block/TrainBlock, TrainPart, Vehicle, materialComposition.
  - Relatert ramme: [VehicleScheduleFrame](../Frames/VehicleScheduleFrame/Description_VehicleScheduleFrame.md).

- Infrastruktur (kapasitetsallokering) — Train Slot / Path Allocation
  - Fokus: søknad om og tildeling av ruteleie fra infrastrukturforvalter (TAP/TAF TSI-domenet).
  - NeTEx har ikke et eksplisitt «Train Slot»-objekt. Anbefalt: modellere som ekstern referanse, eller som profilutvidelse (se InfrastructureSlotFrame nedenfor).

## 2. Koblingsstrategier mellom domener

- VehicleTypeRef på ServiceJourney (Timetable)
  - Brukes til å indikere kjøretøytype for publisering. Lettvekts og stabilt for sluttbrukerinfo.
  - Gir ikke operasjonelle detaljer (ingen faktisk sammensetning/kjøretøy).

- Block/TrainBlock og TrainPart (VehicleSchedule)
  - Representerer den faktiske planlagte kjøringen, med konkrete kjøretøy og materialkomposisjon.
  - Presis for drift, men bør ikke lekke inn i publiseringsdomenet.

- Direkte kobling (ServiceJourney → BlockRef)
  - Enkelt, men skaper sterk kobling og øker avhengighet mellom domener.

- Mellomliggende kobling (anbefalt): ObjectsLink / ServiceBlockAssociation
  - Et dedikert assosiasjonsobjekt med ServiceJourneyRef og BlockRef (ev. validityPeriod, operationalContext, external PathRef).
  - Ligger i egen ramme (f.eks. OperationalAssignmentFrame) for tydelig separasjon.

- DatedServiceJourney (DSJ) som koblingsmekanisme
  - Fordeler: eksisterer i NeTEx, kan referere både ServiceJourney og Block per dato.
  - Ulemper: semantisk overlast hvis DSJ brukes som «catch-all» (salg, avvik, sanntid, kobling). Anbefaling: behold DSJ til datospesifikk kjøring/sanntid; vurder ObjectsLink for ren kobling.

## 3. TrainParts med identisk materialkomposisjon

Hvorfor skjer det?
- Operasjonelle segmenter: bytte av tognummer/personell eller regulatoriske rapporteringsbehov per delstrekning.
- Ulike JourneyPatterns/ServiceLinks per segment, selv om materiellet er identisk.

Kan man slå sammen?
- Ja, for ren sluttbrukervisning, hvis segmentene ikke har egne operasjonelle særtrekk.
- Sjekkliste før sammenslåing:
  - Samme materiell og materialComposition over hele strekningen.
  - Ingen faktisk splitting/merging av sett underveis.
  - Ingen segmentspesifikke avvik eller separate forsinkelser som må vises.
  - Identisk gyldighet og samme operative kontekst.

## 4. Integrasjon med infrastruktur (Train Slot / Path)

- Hendelsesflyt (anbefalt):
  1) Path Request (søknad) sendes fra operatør → infrastrukturforvalter.
  2) Path Allocation (tildeling) returneres, kan avvike fra søknad.
  3) Oppdater TimetableFrame (publisering) og VehicleScheduleFrame (drift) med avvik/ny tider.

- Feltmapping/eksterne referanser:
  - Lagre tildelt Path/Slot-ID som ekstern referanse i Block/TrainBlock eller i et mellomobjekt (ObjectsLink).
  - Bruk OperationalContext/Notes for detaljerte avvik.

- Forslag til profilutvidelse: InfrastructureSlotFrame
  - TrainSlot: requestedPathRef, allocatedPathRef, infrastructureManagerRef, validityPeriod, trackSections.
  - Refereres fra TrainBlock via TrainSlotRef (indirekte kobling bevares).

## 5. Beste praksis

- ID-stabilitet
  - Block/TrainBlock-ID bør være stabil nok til referanser, men endres ved vesentlige planendringer.
  - DSJ-ID brukes for datospesifikke instanser; ikke som generell koblingsnøkkel.
  - ObjectsLink (eller ServiceBlockAssociation) får egen ID og versjonering.

- Versjonering og endringslogg
  - Versjoner per ramme; unngå at publisering må republeres ved operasjonelle endringer som ikke påvirker passasjer.

- Validering
  - Konsistenskontroller mellom ServiceJourney, DSJ, Block og (ev.) ObjectsLink.
  - Varsling når Path Allocation avviker fra søknad.

## 6. Minieksempler

ServiceJourney med VehicleTypeRef (publisering):
```xml
<ServiceJourney id="SJ:1" version="1">
  <Name>Oslo S – Kristiansand</Name>
  <VehicleTypeRef ref="VT:InterCitySet"/>
</ServiceJourney>
```

VehicleSchedule med TrainBlock/TrainPart (drift):
```xml
<TrainBlock id="TB:GA-601" version="1">
  <TrainParts>
    <TrainPart id="TP:GA-601-1" version="1">
      <Name>Oslo – Kongsberg</Name>
      <MaterialCompositionRef ref="MC:GA-IC-7"/>
    </TrainPart>
    <TrainPart id="TP:GA-601-2" version="1">
      <Name>Kongsberg – Kristiansand</Name>
      <MaterialCompositionRef ref="MC:GA-IC-7"/>
    </TrainPart>
  </TrainParts>
</TrainBlock>
```

DatedServiceJourney som dagsinstans og kobling:
```xml
<DatedServiceJourney id="DSJ:2026-03-12-GA-601" version="1">
  <ServiceJourneyRef ref="SJ:1"/>
  <BlockRef ref="TB:GA-601"/>
  <OperatingDayRef ref="OD:2026-03-12"/>
</DatedServiceJourney>
```

Profilutvidelse: ObjectsLink (assosiasjon mellom domener):
```xml
<ObjectsLink id="OL:SJ1-TB601" version="1" xmlns:ext="http://example.org/netex/profile">
  <ServiceJourneyRef ref="SJ:1"/>
  <BlockRef ref="TB:GA-601"/>
  <ext:PathRef ref="PATH:IM-123456"/>
  <ValidityPeriod>
    <FromDate>2026-03-01</FromDate>
    <ToDate>2026-12-12</ToDate>
  </ValidityPeriod>
</ObjectsLink>
```

## 7. Anbefalt navngivning

- ObjectsLink — generisk navn for koblingsobjekt mellom domener.
- Alternativer: ServiceBlockAssociation, OperationalAssignment.

## 8. Relaterte guider

- [Frames Overview](FramesOverview.md)
- [Get Started Guide](GetStarted_Guide.md)
- [Main Guide](README.md)