# Example: Route in NeTEx

```xml
<Route id="ERP:Route:1" version="1" name="City Center to Airport" directionType="outbound">
    <LineRef ref="ERP:Line:10"/>
    <PointsInSequence>
        <PointOnRoute id="ERP:PointOnRoute:1" order="1">
            <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:100"/>
        </PointOnRoute>
        <PointOnRoute id="ERP:PointOnRoute:2" order="2">
            <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:101"/>
        </PointOnRoute>
        <PointOnRoute id="ERP:PointOnRoute:3" order="3">
            <ScheduledStopPointRef ref="ERP:ScheduledStopPoint:102"/>
        </PointOnRoute>
    </PointsInSequence>
</Route>
```