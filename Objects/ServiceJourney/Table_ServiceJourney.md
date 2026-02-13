# ServiceJourney – Felter (minimum)

Denne tabellen oppsummerer de viktigste feltene for ServiceJourney i norsk NeTEx‑profil. Se også konseptuell beskrivelse og feltforklaringer i Entur‐håndboken for «timetable» (ServiceJourney) og tilhørende datamodeller.

| Type       | Navn                      | Type (XSD/Ref)                | Kardinalitet | Beskrivelse |
|------------|---------------------------|-------------------------------|--------------|-------------|
| Element    | ServiceAlteration         | ServiceAlterationEnumeration  | 0:1          | Angir type av avgang: planned, extraJourney, replaced, cancellation. |
| Element    | DepartureTime             | xsd:time                      | 0:1          | Avgangstid (for enkelrepresentasjon uten full passingTimes). |
| Element    | Frequency                 | Frequency                     | 0:1          | Frekvens/interval for avganger (brukes for frekvensruter). |
| Element    | JourneyDuration           | xsd:duration                  | 0:1          | Total varighet for reisen. |
| Referanse  | dayTypes                  | DayTypeRef                    | 1:*          | Referanser til DayType som beskriver hvilke dager avgangen gjelder. |
| Referanse  | JourneyPatternRef         | JourneyPatternRef             | 1:1          | Referanse til JourneyPattern som definerer stoppsekvensen. |
| Referanse  | JourneyFrequencyGroupRef  | JourneyFrequencyGroupRef      | 0:1          | Referanse til JourneyFrequencyGroup (for rytme-/intervallavgang). |
| Referanse  | VehicleTypeRef            | VehicleTypeRef                | 0:1          | Referanse til kjøretøytype. |
| Referanse  | OperatorRef               | OperatorRef                   | 0:1          | Referanse til operatør. |
| Referanser | trainNumbers              | TrainNumberRef                | 0:*          | Referanser til TrainNumber. |
| Elementer  | passingTimes              | TimetabledPassingTime         | 1:*          | Planlagte passeringstider per stopp langs reisen. |
| Elementer  | parts                     | JourneyPart                   | 0:*          | Delstrekninger (for spesialtilfeller, f.eks. sammensatte tog). |
| Elementer  | checkConstraints          | CheckConstraint               | 0:*          | Informasjon om kontroller/sperrer som kan gi forsinkelse. |
| Element    | TrainSize                 | TrainSize                     | 0:1          | Størrelse/struktur for tog. |
| Element    | FlexibleServiceProperties | FlexibleServiceProperties     | 0:1          | Egenskaper for fleksibel (bestillings-)transport på avgangen. |

Merknader
- Minst to stopp må være definert for en ServiceJourney via passingTimes. Stoppene er gitt av StopPointInJourneyPattern på det refererte JourneyPattern.  
- ServiceJourney er en VehicleJourney for passasjertrafikk og modelleres i TimetableFrame.

Kilder (normative/autoritative)
- Entur håndbok – «timetable» (ServiceJourney) inkl. felttabell og kardinalitet.  
- Entur håndbok – «Data models» (sammenhenger mellom ServiceJourney, JourneyPattern og DayType).  
