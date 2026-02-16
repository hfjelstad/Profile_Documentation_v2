# VehicleScheduleFrame – description

**Purpose:** Operational vehicle schedules; blocks, duties, and assignments.

**Typical elements:** Blocks, VehicleServices, VehicleTypeAssignments, Duties.

**Keys:** id, version, vehicleServiceRef/blockRef.

**Example:**
```xml
<netex:VehicleScheduleFrame id="NO:VehicleScheduleFrame:1" version="1">
  <netex:blocks>
    <netex:Block id="NO:Block:10A" version="1"/>
  </netex:blocks>
</netex:VehicleScheduleFrame>
```

**XSD:** See VehicleScheduleFrame in NeTEx.