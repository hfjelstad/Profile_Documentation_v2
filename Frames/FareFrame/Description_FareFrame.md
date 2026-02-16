# FareFrame – description

**Purpose:** Fare data, products, and pricing rules.

**Typical elements:** FareStructureElements, FareProducts, Tariffs, SalesOfferPackages, Prices.

**Keys:** id, version, tariffRef/fareProductRef/fareStructureElementRef.

**Example:**
```xml
<netex:FareFrame id="NO:FareFrame:1" version="1">
  <netex:fareProducts>
    <netex:PreassignedFareProduct id="NO:FP:single" version="1" name="Enkeltbillett"/>
  </netex:fareProducts>
  <netex:tariffs>
    <netex:Tariff id="NO:Tariff:zone" version="1"/>
  </netex:tariffs>
</netex:FareFrame>
```

**XSD:** See FareFrame in NeTEx.