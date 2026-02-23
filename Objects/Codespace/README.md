# Codespace

## Description
A codespace in NeTEx is a namespace used to scope all @id and @ref values, ensuring globally unique identifiers across datasets and deliveries. By prefixing identifiers with a constant codespace, collisions are avoided when data is exchanged or merged.

In this profile, the codespace is fixed to ERP and must be used consistently for all identifiers and references.

## Profile Requirements
- All identifiers (@id) and references (@ref) MUST be prefixed with the codespace ERP.
- The recommended identifier pattern is: ERP:{ObjectType}:{LocalId}
- The codespace MUST be reflected in PublicationDelivery headers via ParticipantRef = "ERP".

### Identifier and Reference Rules
| Property | Requirement | Example |
|---|---|---|
| Codespace prefix | MUST be ERP | ERP:Line:10 |
| Identifier pattern | MUST follow ERP:{ObjectType}:{LocalId} | ERP:JourneyPattern:JP_10_1 |
| References | MUST point to existing ERP-scoped ids | ref="ERP:Quay:12345" |
| PublicationDelivery.ParticipantRef | MUST be set to ERP | <ParticipantRef>ERP</ParticipantRef> |

## Naming Conventions by Object Type
Use the pattern ERP:{ObjectType}:{LocalId}. Examples:
- Line: ERP:Line:10
- JourneyPattern: ERP:JourneyPattern:JP_10_1
- Quay: ERP:Quay:12345
- StopPlace: ERP:StopPlace:SP_987

Choose LocalId values that are stable within the producing system. Avoid whitespace and special characters; use letters, digits, underscore.

## PublicationDelivery Header Template
A minimal header that mirrors the codespace usage:

```xml
<PublicationDelivery xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns="http://www.netex.org.uk/netex"
                    version="1.09">
  <ParticipantRef>ERP</ParticipantRef>
  <PublicationTimestamp>2025-01-01T00:00:00Z</PublicationTimestamp>
  <Description>ERP scoped delivery</Description>
  <!-- DataObjects go here -->
</PublicationDelivery>
```

## Validation Checklist
- All @id values start with ERP: and follow ERP:{ObjectType}:{LocalId}.
- All @ref values point to existing @id values with the ERP: prefix.
- ParticipantRef is exactly ERP.
- ObjectType matches the actual element type (e.g., Line, JourneyPattern, Quay).

Common pitfalls:
- Missing ERP prefix on either @id or @ref.
- Mismatch between ObjectType in the id and the element (e.g., ERP:Quay:… on a StopPlace).
- ParticipantRef left empty or set to a different value.

## Minimal XML Example (ERP Codespace)
The example shows PublicationDelivery with ERP codespace applied to @id and @ref across Line, JourneyPattern and Quay.

```xml
<PublicationDelivery xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xmlns="http://www.netex.org.uk/netex"
                    version="1.09">
  <ParticipantRef>ERP</ParticipantRef>
  <PublicationTimestamp>2025-01-01T00:00:00Z</PublicationTimestamp>
  <DataObjects>
    <CompositeFrame id="ERP:CompositeFrame:CF_1" version="1">
      <frames>
        <ServiceFrame id="ERP:ServiceFrame:SF_1" version="1">
          <lines>
            <Line id="ERP:Line:10" version="1">
              <Name>Line 10</Name>
            </Line>
          </lines>
          <journeyPatterns>
            <JourneyPattern id="ERP:JourneyPattern:JP_10_1" version="1">
              <Name>Line 10 Pattern 1</Name>
            </JourneyPattern>
          </journeyPatterns>
        </ServiceFrame>
        <SiteFrame id="ERP:SiteFrame:Sites_1" version="1">
          <quays>
            <Quay id="ERP:Quay:12345" version="1">
              <Name>Quay A</Name>
            </Quay>
          </quays>
        </SiteFrame>
      </frames>
      <frameDefaults>
        <DefaultLocale>
          <TimeZone>UTC</TimeZone>
          <DefaultLanguage>en</DefaultLanguage>
        </DefaultLocale>
      </frameDefaults>
    </CompositeFrame>
  </DataObjects>
</PublicationDelivery>
```

## Notes
- The ERP prefix is case-sensitive and must be used exactly as shown.
- LocalId values are producer-assigned; ensure stability over time to avoid identifier churn.
