# Line

Formål
- Line representerer en kollektivlinje slik den kommuniseres til reisende (linjenummer/navn), uavhengig av rutevarianter og avganger.

Omfang
- Dette dokumentet beskriver minimumskrav og anbefalinger for Line i profilen. Se felttabell for detaljerte regler.

Profilregler (kort)
- id (påkrevd): Bruk ERP-kodespace. Mønster: "ERP:Line:<lokalId>". Stabil over tid.
- version (påkrevd): Start på "1" og øk ved endringer som påvirker Line-objektet.
- Name (påkrevd): Visningsnavn for linjen (f.eks. "Linje 10").
- PublicCode (påkrevd): Kortkode mot publikum, normalt tilsvarende linjenummer (f.eks. "10"). Unik innenfor Operatør.
- ShortName (anbefalt): Forkortet visningsnavn når Name er lang.
- TransportMode (påkrevd): Kjøretøy-/transporttype (f.eks. bus, tram, rail, metro, ferry).
- OperatorRef (anbefalt): Referanse til ansvarlig operatør (ERP:Operator:<id>).
- Description (valgfritt): Kort beskrivelse.
- BrandingRef (valgfritt): Referanse til profil/branding der dette brukes.

Relasjoner
- Line refereres fra ServiceJourney via JourneyPattern (indirekte) og benyttes for gruppering/visning mot reisende.
- OperatorRef peker til Operator definert i Resource-/ServiceFrame.

Versjonering og identifikatorer
- id skal ha ERP som kodespace/namespace. Eksempel: ERP:Line:10
- Bruk samme id på tvers av leveranser; version økes ved endring.

Eksempel
- Se Objects/Line/Example_Line.xml for et minimalt NeTEx-eksempel med ERP-kodespace.
