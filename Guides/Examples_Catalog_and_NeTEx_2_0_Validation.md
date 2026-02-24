# Examples Catalog and NeTEx 2.0 Validation

Purpose
This guide provides a complete inventory of XML examples in this repository and a practical checklist for validating NeTEx 2.0 files. It also includes known fixes (XSLT snippets) and batch validation examples for Bash and PowerShell with a lightweight reporting template.

1) XML Example Inventory
The list below covers all Example_*.xml files under Objects, including an OPR marker when present in the file name.

| Path | File | OPR |
|---|---|---|
| Objects/Authority | Example_Authority.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney_Extended_01_Reinforcement.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney_Extended_02_Replacement.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney_Extended_03_BlockLinked.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney_Extended_04_MultiRef.xml |  |
| Objects/DatedServiceJourney | Example_DatedServiceJourney_OPR.xml | YES |
| Objects/DayType | Example_DayType.xml |  |
| Objects/Interchange | Example_Interchange.xml |  |
| Objects/JourneyPattern | Example_JourneyPattern.xml |  |
| Objects/JourneyPattern | Example_JourneyPattern_OPR.xml | YES |
| Objects/Line | Example_Line.xml |  |
| Objects/Line | Example_Line_OPR.xml | YES |
| Objects/Operator | Example_Operator.xml |  |
| Objects/PassengerStopAssignment | Example_PassengerStopAssignment.xml |  |
| Objects/Quay | Example_Quay.xml |  |
| Objects/Route | Example_Route.xml |  |
| Objects/ScheduledStopPoint | Example_ScheduledStopPoint.xml |  |
| Objects/ServiceJourney | Example_ServiceJourney.xml |  |
| Objects/ServiceJourney | Example_ServiceJourney_OPR.xml | YES |
| Objects/StopPlace | Example_StopPlace.xml |  |
| Objects/TrainBlock | Example_TrainBlock.xml |  |
| Objects/Vehicle | Example_Vehicle.xml |  |
| Objects/VehicleType | Example_VehicleType.xml |  |

2) OPR Files
Files with OPR in the name (often denoting operator-oriented examples):
- Objects/DatedServiceJourney/Example_DatedServiceJourney_OPR.xml
- Objects/JourneyPattern/Example_JourneyPattern_OPR.xml
- Objects/Line/Example_Line_OPR.xml
- Objects/ServiceJourney/Example_ServiceJourney_OPR.xml

3) NeTEx 2.0 Validation Checklist
Use this checklist when preparing or validating NeTEx 2.0 documents:
- Root element and envelope
  - Document is rooted at PublicationDelivery and contains a valid PublicationTimestamp, ParticipantRef and PublicationRequest / data frame section(s) as applicable.
- Namespaces
  - Default namespace (xmlns) is http://www.netex.org.uk/netex
  - XML Schema Instance namespace (xmlns:xsi) is http://www.w3.org/2001/XMLSchema-instance
  - Optional prefixes (e.g., siri:) are declared only if used.
- xsi:schemaLocation
  - Contains a mapping for the NeTEx namespace to an appropriate XSD. Example (adjust paths/versions as needed):
    - http://www.netex.org.uk/netex https://netex-cen.eu/schema/2.0/NeTEx_publication.xsd
  - Use local resolved paths if validating offline (e.g., file:///.../NeTEx_publication.xsd).
- Identifiers and references
  - All @id values are unique within the document.
  - All @ref values resolve to an existing @id of the same conceptual type and within the correct codespace.
  - Codespace prefixes are used consistently (e.g., ERP:Line:123) and match Codespace/Namespace configuration.
- Enumerations and codelists
  - Enumeration values are valid, case-sensitive and match the NeTEx 2.0 specification (avoid free-text or mis-cased values like Bus when bus is required).
- Dates and times
  - Use ISO 8601 formats:
    - Date: YYYY-MM-DD (e.g., 2026-02-24)
    - Time: HH:MM:SS (24-hour, zero-padded)
    - DateTime: YYYY-MM-DDThh:mm:ss[Z|±hh:mm]
  - Periods use FromDate/ToDate or StartTime/EndTime consistently and with valid ranges.
- Structural integrity
  - Frames (e.g., ServiceFrame, TimetableFrame, SiteFrame, ResourceFrame) only include objects allowed in those frames and reference each other consistently.
  - No empty mandatory elements; optional elements omitted if unknown rather than left empty.

4) Known Fixes (XSLT Snippets)
The following generic XSLT examples can help normalize common issues. Adapt as needed for your pipeline. Identity transforms are included to avoid altering unaffected content.

4.1 Normalize default namespace and schemaLocation (XSLT 1.0)
```xslt
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns:netex="http://www.netex.org.uk/netex"
  exclude-result-prefixes="xsi netex">

  <!-- Identity -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- Rebuild PublicationDelivery with default netex namespace and schemaLocation -->
  <xsl:template match="/*[local-name()='PublicationDelivery']">
    <PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <xsl:attribute name="xsi:schemaLocation">
        <xsl:text>http://www.netex.org.uk/netex https://netex-cen.eu/schema/2.0/NeTEx_publication.xsd</xsl:text>
      </xsl:attribute>
      <xsl:apply-templates select="@*[name()!='xsi:schemaLocation']|node()"/>
    </PublicationDelivery>
  </xsl:template>
</xsl:stylesheet>
```

4.2 Normalize common enumeration casing (example mapping, XSLT 2.0)
```xslt
<xsl:stylesheet version="2.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:netex="http://www.netex.org.uk/netex"
  exclude-result-prefixes="netex">

  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- Example: normalize VehicleMode enumerations to lower-case per spec -->
  <xsl:template match="netex:ServiceJourney/netex:TransportSubmode | netex:Line/netex:TransportMode">
    <xsl:copy>
      <xsl:variable name="v" select="normalize-space(lower-case(.))"/>
      <xsl:choose>
        <xsl:when test="$v='bus' or $v='coach' or $v='tram' or $v='rail' or $v='metro'">
          <xsl:value-of select="$v"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="."/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
```

4.3 Remove empty optional elements and trim whitespace (XSLT 1.0)
```xslt
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:netex="http://www.netex.org.uk/netex"
  exclude-result-prefixes="netex">

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- Drop elements that are empty or whitespace-only and not mandatory in your profile -->
  <xsl:template match="*[not(node()) or normalize-space(.)='']"/>

  <!-- Trim text nodes -->
  <xsl:template match="text()"><xsl:value-of select="normalize-space(.)"/></xsl:template>
</xsl:stylesheet>
```

5) Batch Validation Examples and Reporting
Below are simple batch examples using xmllint against an XSD. Replace XSD_ROOT with a local folder or use a remote URL. For comprehensive rules (Schematron), run Saxon + Schematron in a similar loop.

5.1 Bash (macOS/Linux)
```bash
#!/usr/bin/env bash
set -euo pipefail

INPUT_ROOT="./Objects"
XSD="${XSD_ROOT:-./schema/NeTEx_publication.xsd}"
REPORT="validation_report.csv"

echo "file,valid,errors_count,first_error,hasOPR" > "$REPORT"

# find all XML examples
while IFS= read -r -d '' f; do
  HAS_OPR="no"
  [[ "$(basename "$f")" == *OPR* ]] && HAS_OPR="yes"
  # validate
  ERR=$(xmllint --noout --schema "$XSD" "$f" 2>&1 || true)
  if [[ -z "$ERR" ]]; then
    echo "${f},yes,0,,${HAS_OPR}" >> "$REPORT"
  else
    FIRST=$(echo "$ERR" | head -n 1 | tr ',' ';')
    COUNT=$(echo "$ERR" | wc -l | tr -d ' ')
    echo "${f},no,${COUNT},${FIRST},${HAS_OPR}" >> "$REPORT"
  fi
done < <(find "$INPUT_ROOT" -type f -name 'Example_*.xml' -print0 | sort -z)

echo "Wrote $(wc -l < "$REPORT") lines to $REPORT"
```

5.2 PowerShell (Windows)
```powershell
$InputRoot = "./Objects"
$Xsd = $env:XSD_ROOT
if ([string]::IsNullOrWhiteSpace($Xsd)) { $Xsd = "./schema/NeTEx_publication.xsd" }
$Report = "validation_report.csv"
"file,valid,errors_count,first_error,hasOPR" | Out-File -FilePath $Report -Encoding UTF8

Get-ChildItem -Path $InputRoot -Recurse -Filter "Example_*.xml" | Sort-Object FullName | ForEach-Object {
  $f = $_.FullName
  $hasOPR = (Split-Path $f -Leaf) -like "*OPR*" ? "yes" : "no"
  $p = Start-Process -FilePath "xmllint" -ArgumentList @("--noout", "--schema", $Xsd, $f) -NoNewWindow -Wait -PassThru -RedirectStandardError temp_err.txt
  $err = Get-Content temp_err.txt -Raw
  if ([string]::IsNullOrWhiteSpace($err)) {
    Add-Content -Path $Report -Value "$f,yes,0,,${hasOPR}"
  } else {
    $lines = ($err -split "`n").Count
    $first = ($err -split "`n")[0].Replace(',', ';')
    Add-Content -Path $Report -Value "$f,no,$lines,$first,${hasOPR}"
  }
}
Remove-Item temp_err.txt -ErrorAction SilentlyContinue
Write-Host "Wrote $((Get-Content $Report).Count) lines to $Report"
```

5.3 Reporting template
A minimal CSV header you can reuse:
- file, valid, errors_count, first_error, hasOPR

Notes
- Use the Checklist (Section 3) alongside XSD/Schematron validation to ensure both structural and semantic correctness.
- If your environment lacks xmllint, consider alternatives (Saxon + XSD 1.1, or other XML validators). Adjust paths and versions to the NeTEx 2.0 schema set used in your project.
