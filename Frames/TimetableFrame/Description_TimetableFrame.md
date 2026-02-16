# TimetableFrame – description

**Purpose:** Operational journeys/times for the public; departure and arrival times.

**Typical elements:** ServiceJourney/VehicleJourney, DayType associations, PassingTimes.

**Keys:** id, version, journeyPatternRef/serviceJourneyPatternRef, dayTypeRef.

**Example:**
```xml
<netex:TimetableFrame id="NO:TimetableFrame:1" version="1">
  <netex:vehicleJourneys>
    <netex:ServiceJourney id="NO:SJ:10-1" version="1" lineRef="NO:Line:10">
      <netex:passingTimes>
        <netex:TimetabledPassingTime stopPointInJourneyPatternRef="NO:SPJP:1" departureTime="08:00:00"/>
      </netex:passingTimes>
    </netex:ServiceJourney>
  </netex:vehicleJourneys>
</netex:TimetableFrame>
```

**XSD:** See TimetableFrame in NeTEx.