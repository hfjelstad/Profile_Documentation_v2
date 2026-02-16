# ServiceFrame – description

**Purpose:** Network and route offer; lines, routes, and patterns for traffic.

**Typical elements:** Lines, Routes, RoutePoints/Links, ServiceLinks, DestinationDisplays, StopAssignments.

**Keys:** id, version, routeRef/serviceLinkRef/lineRef.

**Example:**
```xml
<netex:ServiceFrame id="NO:ServiceFrame:1" version="1">
  <netex:lines>
    <netex:Line id="NO:Line:10" version="1" name="Linje 10"/>
  </netex:lines>
  <netex:routes>
    <netex:Route id="NO:Route:10A" version="1"/>
  </netex:routes>
</netex:ServiceFrame>
```

**XSD:** See ServiceFrame in NeTEx.