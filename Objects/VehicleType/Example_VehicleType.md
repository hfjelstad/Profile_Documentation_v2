# VehicleType Example

```xml
<VehicleType id="ERP:VehicleType:Bus_Standard" version="1">
    <Name>Standard Bus</Name>
    <Description>Standard 12m low-floor bus with wheelchair access</Description>
    <PrivateCode>STD_BUS_12M</PrivateCode>
    <TypeOfFuel>diesel</TypeOfFuel>
    <EuroClass>Euro6</EuroClass>
    <capacities>
        <PassengerCapacity>
            <SeatedCapacity>45</SeatedCapacity>
            <StandingCapacity>30</StandingCapacity>
            <WheelchairPlaceCapacity>2</WheelchairPlaceCapacity>
        </PassengerCapacity>
    </capacities>
    <LowFloor>true</LowFloor>
    <HasLiftOrRamp>true</HasLiftOrRamp>
    <Length>12.0</Length>
    <facilities>
        <ServiceFacilitySetRef ref="ERP:ServiceFacilitySet:WiFi"/>
    </facilities>
</VehicleType>
```