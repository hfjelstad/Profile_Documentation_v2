# SiteFrame – description

**Purpose:** Site model (stop places, terminals, entrances, walking links).

**Typical elements:** StopPlace (with Quay), Access/Entrance, PathLink, NavigationPath, Parking.

**Keys:** id, version, stopPlaceRef/quayRef/pathLinkRef.

**Example:**
```xml
<netex:SiteFrame id="NO:SiteFrame:1" version="1">
  <netex:stopPlaces>
    <netex:StopPlace id="NO:StopPlace:123" version="1" name="Jernbanetorget">
      <netex:quays>
        <netex:Quay id="NO:Quay:123-1" version="1"/>
      </netex:quays>
    </netex:StopPlace>
  </netex:stopPlaces>
</netex:SiteFrame>
```

**XSD:** See SiteFrame in NeTEx.