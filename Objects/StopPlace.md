# StopPlace

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

NeTEx-minieksempel (codespace/namespace: ERP)

```xml
<PublicationDelivery xmlns="http://www.netex.org.uk/netex"
                     xmlns:gml="http://www.opengis.net/gml/3.2"
                     version="1.0">
  <PublicationTimestamp>2026-02-15T11:00:00Z</PublicationTimestamp>
  <ParticipantRef>ERP</ParticipantRef>
  <dataObjects>
    <SiteFrame id="ERP:SiteFrame:StopPlaceExample" version="1">
      <stopPlaces>
        <!-- Monomodal StopPlace med Quay-er -->
        <StopPlace id="ERP:StopPlace:1001" version="1">
          <Name>Oslo gate 1</Name>
          <TransportMode>bus</TransportMode>
          <StopPlaceType>onstreetBus</StopPlaceType>
          <Centroid>
            <Location>
              <gml:pos srsName="urn:ogc:def:crs:EPSG::4326">59.9123 10.7461</gml:pos>
            </Location>
          </Centroid>
          <tariffZones>
            <TariffZoneRef ref="ERP:TariffZone:R1"/>
          </tariffZones>
          <quays>
            <Quay id="ERP:Quay:1001-1" version="1">
              <Name>Retning sentrum</Name>
              <Centroid>
                <Location>
                  <gml:pos srsName="urn:ogc:def:crs:EPSG::4326">59.91235 10.74608</gml:pos>
                </Location>
              </Centroid>
            </Quay>
            <Quay id="ERP:Quay:1001-2" version="1">
              <Name>Retning vest</Name>
              <Centroid>
                <Location>
                  <gml:pos srsName="urn:ogc:def:crs:EPSG::4326">59.91226 10.74622</gml:pos>
                </Location>
              </Centroid>
            </Quay>
          </quays>
        </StopPlace>

        <!-- Multimodal parent uten Quay -->
        <StopPlace id="ERP:StopPlace:3000" version="1">
          <Name>Oslo knutepunkt</Name>
        </StopPlace>

        <!-- Underordnet monomodal som peker til parent -->
        <StopPlace id="ERP:StopPlace:3001" version="1">
          <Name>Oslo knutepunkt (buss)</Name>
          <TransportMode>bus</TransportMode>
          <StopPlaceType>busStation</StopPlaceType>
          <ParentSiteRef ref="ERP:StopPlace:3000"/>
          <quays>
            <Quay id="ERP:Quay:3001-A" version="1">
              <Name>Terminal A</Name>
            </Quay>
          </quays>
        </StopPlace>
      </stopPlaces>
    </SiteFrame>
  </dataObjects>
</PublicationDelivery>
```

Se også
- PassengerStopAssignment (ServiceFrame) – logisk stoppunkt til fysisk StopPlace/Quay
- Quay – detaljert modell av holdeplassposisjon
