# ServiceCalendarFrame – description

**Purpose:** Calendar definitions and validity periods.

**Typical elements:** DayTypes, OperatingPeriods, DayTypeAssignments, OperatingDays.

**Keys:** id, version, operatingPeriodRef/dayTypeRef.

**Example:**
```xml
<netex:ServiceCalendarFrame id="NO:ServiceCalendarFrame:1" version="1">
  <netex:dayTypes>
    <netex:DayType id="NO:DayType:WKD" version="1" name="Hverdager"/>
  </netex:dayTypes>
</netex:ServiceCalendarFrame>
```

**XSD:** See ServiceCalendarFrame in NeTEx.