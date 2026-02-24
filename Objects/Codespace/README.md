# Codespace

## Description
A codespace is the namespace for NeTEx @id and @ref values. It ensures global uniqueness across datasets and deliveries by prefixing identifiers so that there are no collisions when data is exchanged or merged.

Governance: The codespace is designated by the receiver of the delivery. In this documentation, "ERP" is used only as an example. Replace "ERP" with the actual codespace agreed with the receiver.

Recommended identifier pattern: {CODESPACE}:{ObjectType}:{LocalId}
- CODESPACE: The receiver-assigned short code for the namespace (e.g., ERP, OPR, NSR)
- ObjectType: The concrete NeTEx element type (e.g., Line, JourneyPattern, Quay, Operator)
- LocalId: A stable, producer-defined identifier that is unique within the chosen codespace for the given ObjectType

## Table
Examples of recommended identifier formatting across multiple objects:

| Object        | Recommended pattern                      | Example (with CODESPACE=ERP) |
|--------------|-------------------------------------------|------------------------------|
| Line         | {CODESPACE}:Line:{LocalId}                | ERP:Line:10                  |
| JourneyPattern | {CODESPACE}:JourneyPattern:{LocalId}    | ERP:JourneyPattern:JP_10_1   |
| Quay         | {CODESPACE}:Quay:{LocalId}                | ERP:Quay:Q_100               |
| Operator     | {CODESPACE}:Operator:{LocalId}            | ERP:Operator:OPR_1           |

Notes:
- ObjectType should match the NeTEx element names used in the delivery.
- LocalId should be stable across updates; use the NeTEx version attribute for change tracking.

## PublicationDelivery
ParticipantRef MUST match the chosen {CODESPACE} (the receiver’s designation). All @id/@ref values in the delivery MUST be scoped with the same {CODESPACE}: prefix.

## Minimal XML example (using {CODESPACE})
```xml
<PublicationDelivery xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    version="1.0">
  <ParticipantRef>{CODESPACE}</ParticipantRef>
  <Description>Minimal example showing consistent codespace usage</Description>
  <dataObjects>
    <CompositeFrame id="{CODESPACE}:CompositeFrame:CF_1" version="1">
      <frames>
        <ServiceFrame id="{CODESPACE}:ServiceFrame:SF_1" version="1">
          <lines>
            <Line id="{CODESPACE}:Line:10" version="1"/>
          </lines>
          <journeyPatterns>
            <JourneyPattern id="{CODESPACE}:JourneyPattern:JP_10_1" version="1">
              <RouteRef ref="{CODESPACE}:Route:R_10"/>
            </JourneyPattern>
          </journeyPatterns>
          <operators>
            <Operator id="{CODESPACE}:Operator:OPR_1" version="1"/>
          </operators>
        </ServiceFrame>
        <SiteFrame id="{CODESPACE}:SiteFrame:ST_1" version="1">
          <quays>
            <Quay id="{CODESPACE}:Quay:Q_100" version="1"/>
          </quays>
        </SiteFrame>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

## Minimal XML example (with CODESPACE=ERP)
This example is provided to align with documentation rules that require at least one example using the codespace "ERP". Replace "ERP" with the receiver-assigned codespace in real deliveries.
```xml
<PublicationDelivery xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    version="1.0">
  <ParticipantRef>ERP</ParticipantRef>
  <Description>Minimal example using ERP as the codespace</Description>
  <dataObjects>
    <CompositeFrame id="ERP:CompositeFrame:CF_1" version="1">
      <frames>
        <ServiceFrame id="ERP:ServiceFrame:SF_1" version="1">
          <lines>
            <Line id="ERP:Line:10" version="1"/>
          </lines>
          <journeyPatterns>
            <JourneyPattern id="ERP:JourneyPattern:JP_10_1" version="1">
              <RouteRef ref="ERP:Route:R_10"/>
            </JourneyPattern>
          </journeyPatterns>
          <operators>
            <Operator id="ERP:Operator:OPR_1" version="1"/>
          </operators>
        </ServiceFrame>
        <SiteFrame id="ERP:SiteFrame:ST_1" version="1">
          <quays>
            <Quay id="ERP:Quay:Q_100" version="1"/>
          </quays>
        </SiteFrame>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>
```

## Validation checklist
- ParticipantRef equals the chosen {CODESPACE}; do not include a trailing colon in ParticipantRef.
- Every @id and @ref begins with "{CODESPACE}:" and uses the recommended pattern {CODESPACE}:{ObjectType}:{LocalId}.
- The same {CODESPACE} is used consistently within one delivery unless the receiver explicitly requires multiple codespaces.
- ObjectType segment reflects the NeTEx element type in use.
- LocalId is stable across versions; use the version attribute for updates.
- Case and punctuation are consistent (codespaces and ObjectType names are case-sensitive; avoid double colons, spaces, or trailing colons).

## Common pitfalls
- Treating "ERP" as a mandatory profile requirement (it is not); the receiver designates the codespace.
- Mismatch between ParticipantRef and the prefix used in @id/@ref.
- Omitting the ObjectType segment or mixing naming styles across objects.
- Mixing different codespaces within a single delivery without receiver approval.
- Changing LocalId between deliveries, breaking referential stability.
