# Line

The Line object represents a public transport line within a ServiceFrame.

Schema/XSD observations for the current variant used in this repository:
- TransportMode is not present directly under Line. If line classification is required, use an allowed alternative modelling pattern (e.g., OperationalContextRef) or document it as a profile-specific rule. Do not place TransportMode under Line for this XSD variant.
- TypeOfLineRef is not accepted directly under Line in this schema variant. If needed by the profile, reference it via an allowed context or profile construct, not as a direct child of Line.
- Presentation must be a direct child of Line. Do not add @id or @version to Presentation. Colour and TextColour shall be six uppercase hexadecimal digits without a leading # (e.g., 005EB8, FFFFFF).
- Use lowerCamelCase for collection elements in examples and guidance: dataObjects, frames, lines, organisations.

Validated minimal example (ERP codespace)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" version="1.0">
  <PublicationTimestamp>2026-02-27T12:59:00Z</PublicationTimestamp>
  <ParticipantRef>ERP</ParticipantRef>
  <dataObjects>
    <CompositeFrame id="ERP:CompositeFrame:LineExample:1" version="1">
      <frames>
        <ResourceFrame id="ERP:ResourceFrame:LineExample:1" version="1">
          <organisations>
            <Operator id="ERP:Operator:OP1" version="1">
              <Name>Example Operator</Name>
            </Operator>
          </organisations>
        </ResourceFrame>
        <ServiceFrame id="ERP:ServiceFrame:LineExample:1" version="1">
          <lines>
            <Line id="ERP:Line:1" version="1">
              <Name>Line 1</Name>
              <OperatorRef ref="ERP:Operator:OP1" version="1"/>
              <Presentation>
                <Colour>005EB8</Colour>
                <TextColour>FFFFFF</TextColour>
              </Presentation>
            </Line>
          </lines>
        </ServiceFrame>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

Notes
- The XML above has been validated against the repository's XSD setup and demonstrates the required structure and constraints for Line, including resolution of OperatorRef in ResourceFrame and the permitted Presentation structure.

See also
- Objects/Line/Table_Line.md for the synchronized requirements table.
- Objects/Line/Example_Line.xml for the standalone example file matching the snippet above.
