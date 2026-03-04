# Table of Examples

## Description
This document provides a comprehensive table of XML examples for NeTEx objects, ensuring consistency and clarity in documentation. Each example demonstrates correct usage of the ERP codespace and adheres to NeTEx version 2.0 standards.

## Examples Table
| **Object**       | **Description**                          | **Example File**        |
|-------------------|------------------------------------------|--------------------------|
| StopPlace         | Example of a StopPlace element          | `examples/StopPlace.xml`|
| ServiceJourney    | Example of a ServiceJourney element     | `examples/ServiceJourney.xml`|
| Route             | Example of a Route element              | `examples/Route.xml`    |

## XML Example (ERP Codespace)
```xml
<StopPlace xmlns="http://www.netex.org.uk/netex" version="2.0" id="ERP:StopPlace:SP001">
    <Name>Main Station</Name>
    <Centroid>
        <Location>
            <Longitude>10.7522</Longitude>
            <Latitude>59.9139</Latitude>
        </Location>
    </Centroid>
</StopPlace>
```