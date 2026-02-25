# NeTEx Conventions Guide

## **Elementnavn og casing**
- NeTEx følger **lowerCamelCase** for alle listeelementer.
- Eksempler:
  - `<dataObjects>` (ikke `DataObjects`)
  - `<frames>`
  - `<journeyPatterns>`

Dette gjelder alle samlinger i XML-strukturen.

## **Eksempel på korrekt struktur**
```xml
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" version="2.0">
  <PublicationTimestamp>2026-02-25T14:22:00Z</PublicationTimestamp>
  <ParticipantRef>ENTUR</ParticipantRef>
  <dataObjects>
    <CompositeFrame id="ENT:CompositeFrame:Example:1" version="1">
      <frames>
        <ResourceFrame id="ENT:ResourceFrame:1" version="1"/>
        <ServiceFrame id="ENT:ServiceFrame:1" version="1"/>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

## **Best practice**
- Bruk alltid lowerCamelCase for lister.
- Følg NeTEx 2.0 valideringsregler.

Se også: [Frames/Example_PublicationDelivery.xml](../Frames/Example_PublicationDelivery.xml)
