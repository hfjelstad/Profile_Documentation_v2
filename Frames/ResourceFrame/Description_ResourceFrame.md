# ResourceFrame – description

**Purpose:** Common resources shared across other frames (organisations, code lists, types, responsibilities).

**Typical elements:** Organisations (Authority/Operator), ResponsibilitySet, TypesOfValue, Codespaces.

**Keys:** id, version, codespace, dataSourceRef.

**Example:**
```xml
<netex:ResourceFrame id="NO:ResourceFrame:1" version="1">
  <netex:organisations>
    <netex:Authority id="NO:Authority:ENTUR" version="1"/>
  </netex:organisations>
  <netex:typesOfValue>
    <netex:TypeOfValue id="NO:TOV:LineType:bus" version="1" name="bus"/>
  </netex:typesOfValue>
</netex:ResourceFrame>
```

**XSD:** See definitions for ResourceFrame in NeTEx.