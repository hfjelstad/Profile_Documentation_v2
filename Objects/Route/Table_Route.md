# Route – feltoversikt

Denne tabellen beskriver de viktigste feltene for NeTEx Route slik de brukes i profilen. Struktur og kolonner følger samme mal som for ServiceJourney og DatedServiceJourney.

| Felt | Type | Kardinalitet | Påkrevd | Beskrivelse |
|---|---|---:|:---:|---|
| id | xs:ID | 1..1 | Ja | Global unik identifikator for Route. |
| version | xs:integer | 0..1 | Nei | Versjon av objektet. Standard 1 hvis ikke oppgitt. |
| Name | MultilingualString | 1..1 | Ja | Visningsnavn for ruten. |
| ShortName | xs:string | 0..1 | Nei | Kortnavn/nummer for ruten. |
| PublicCode | xs:string | 0..1 | Nei | Offentlig kode/nummer som vises til kunder. |
| Description | MultilingualString | 0..1 | Nei | Utfyllende beskrivelse. |
| PrivateCode | xs:string | 0..1 | Nei | Intern kode. |
| LineRef | VersionRef | 1..1 | Ja | Referanse til Line som ruten tilhører. |
| DirectionType | DirectionTypeEnumeration | 0..1 | Nei | Retningsangivelse (inbound, outbound, clockwise, counterclockwise). |
| PointsInSequence | complex | 1..n | Ja | Sekvens av PointOnRoute som beskriver rekkefølgen av stopp langs ruten. |
| PointOnRoute@order | xs:integer | 1..1 | Ja | Rekkefølgenummer for punktet i ruten. |
| PointOnRoute.ScheduledStopPointRef@ref | VersionRef | 1..1 | Ja | Referanse til ScheduledStopPoint. |

Merknader
- Route beskriver den topologiske rekkefølgen av stopp for en gitt Line og retning.
- For konsistens: bruk samme navngivnings- og versjonspraksis som i ServiceJourney og DatedServiceJourney.
- Dersom flere delruter finnes for samme Line og DirectionType, skill dem med egne id-er og/eller PrivateCode.
