# PassengerStopAssignment — Example

NeTEx XML fragment illustrating a default assignment of a planned stop to a specific quay. The example uses the ERP codespace/namespace for all identifiers.

```xml
<netex:PublicationDelivery xmlns:netex="http://www.netex.org.uk/netex" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.09">
  <netex:dataObjects>
    <netex:CompositeFrame id="ERP:CompositeFrame:CF_1" version="1">
      <netex:frames>
        <netex:ServiceFrame id="ERP:ServiceFrame:SF_1" version="1">
          <netex:scheduledStopPoints>
            <netex:ScheduledStopPoint id="ERP:ScheduledStopPoint:SSP_1" version="1"/>
          </netex:scheduledStopPoints>
          <netex:stopPlaces>
            <netex:StopPlace id="ERP:StopPlace:SP_10" version="1">
              <netex:quays>
                <netex:Quay id="ERP:Quay:Q_101" version="1"/>
              </netex:quays>
            </netex:StopPlace>
          </netex:stopPlaces>
          <netex:stopAssignments>
            <netex:PassengerStopAssignment id="ERP:PassengerStopAssignment:PSA_1" version="1">
              <netex:ScheduledStopPointRef ref="ERP:ScheduledStopPoint:SSP_1"/>
              <netex:StopPlaceRef ref="ERP:StopPlace:SP_10"/>
              <netex:QuayRef ref="ERP:Quay:Q_101"/>
            </netex:PassengerStopAssignment>
          </netex:stopAssignments>
        </netex:ServiceFrame>
      </netex:frames>
    </netex:CompositeFrame>
  </netex:dataObjects>
</netex:PublicationDelivery>
```

Notes
- The ScheduledStopPointRef, StopPlaceRef and QuayRef are all within the same ServiceFrame for consistent resolution.
- For dated overrides, provide an additional PassengerStopAssignment scoped to the specific dated service/journey context.
