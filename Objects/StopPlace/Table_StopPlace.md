# StopPlace – feltoversikt

| Type | Name | SubElement | Beskrivelse | Kardinalitet |
|---|---|---|---|---|
| Attribute | id |  | Globalt identifikator (ERP:StopPlace:…) | 1:1 |
| Attribute | version |  | Versjonsnummer | 1:1 |
| Attribute | created |  | Opprettet-dato | 0:1 |
| Attribute | changed |  | Endret-dato | 0:1 |
| Attribute | modification |  | Endringstype (f.eks. delete ved avvikling) | 0:1 |
| Element | Name |  | Navn på stoppestedet | 1:1 |
| Element | alternativeNames | AlternativeName | Alternative navn/alias | 0:* |
| Element | TransportMode |  | Hovedmodus (bus, rail, metro, tram, water, …) | 1:1 |
| Element | AirSubmode / BusSubmode / … |  | Valgfri underkategori for modus | 0:1 |
| Element | StopPlaceType |  | onstreetBus, railStation, metroStation, busStation, … (påkrevd når Quay finnes) | 0:1 |
| Reference | TopographicPlaceRef |  | Referanse til by/område | 0:1 |
| Reference | ParentSiteRef |  | Referanse til multimodal parent StopPlace | 0:1 |
| List | keyList | KeyValue | Alternative nøkler (eks. eksterne ID-er) | 0:1 |
| Element | Centroid | Location | Geometrisk punktrepresentasjon | 0:1 |
| List | tariffZones | TariffZoneRef | Referanser til takstsoner | 0:* |
| List | quays | Quay | Underliggende holdeplassposisjoner (ikke på multimodal parent) | 0:* |
| List | ValidBetween | FromDate/ToDate | Enkel gyldighetsperiode | 0:* |
| List | adjacentSites | SiteRef | Nærliggende/tilknyttede sites | 0:* |
| List | accessSpaces | AccessSpace | Ventearealer/interne arealer | 0:* |
| List | pathLinks | PathLink | Gående lenker | 0:* |
| List | pathJunctions | PathJunction | Kryss i gangnett | 0:* |
| List | navigationPaths | NavigationPath | Gangebeskrivelser/overstyringer | 0:* |

Merknader
- Multimodal StopPlace (parent) har ingen quays.
- Monomodal StopPlace må ha minst én Quay og kan kun ha én transporttype.
