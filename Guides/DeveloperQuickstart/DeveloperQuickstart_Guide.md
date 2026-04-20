# Developer Quickstart — Retrieve, Parse & Interpret NeTEx

> A hands-on guide for software developers who need to work with real NeTEx data. All code examples use Python, but every step is explained generically so you can adapt to any language with an XML parser.
>
> This guide transposes the concepts from the [DGITM NeTEx Training](https://github.com/etalab/netex-france-formation/) into a language-agnostic, developer-oriented format.

---

## Prerequisites

- A programming language with an XML parser (Python + `lxml` used here)
- Command-line basics (downloading files, unzipping)
- No prior NeTEx knowledge required (but the [FAQ](/Guides/FAQ/FAQ.md) is a useful companion)

## Setup (Python)

```bash
pip install lxml requests
```

---

## Step 1 — Find and Download NeTEx Data

NeTEx datasets are published as open data through **National Access Points (NAPs)** across Europe. Pick any feed to follow along:

| Country | Feed | URL | Notes |
|---------|------|-----|-------|
| France | Rochefort Océan R'Bus | [transport.data.gouv.fr](https://transport.data.gouv.fr/datasets?q=r%C3%A9seau+urbain+r%27bus) | Small city network, good for learning |
| France | Île-de-France Mobilités | [data.iledefrance-mobilites.fr](https://data.iledefrance-mobilites.fr/) | Large urban network |
| Norway | All Norwegian transit | [developer.entur.org](https://developer.entur.org/) | Nordic Profile, high quality |
| UK | All bus data | [data.bus-data.dft.gov.uk](https://data.bus-data.dft.gov.uk/) | EPIP-based |
| Sweden | National data | [trafiklab.se](https://www.trafiklab.se/) | Nordic Profile variant |
| Finland | National data | [fintraffic.fi](https://www.fintraffic.fi/en/fintraffic/open-data) | Nordic Profile variant |
| Netherlands | National data | [ndovloket.nl](https://ndovloket.nl/) | Dutch profile |
| Germany | Regional operators | [opendata-oepnv.de](https://www.opendata-oepnv.de/) | NeTEx-DE profile |
| Switzerland | National data | [opentransportdata.swiss](https://opentransportdata.swiss/) | Swiss profile |

### Download Example

```python
import requests, zipfile, io, os

# Example: download a small French NeTEx dataset
url = "https://transport.data.gouv.fr/resources/80840/download"  # adjust to current URL
response = requests.get(url)

os.makedirs("netex_data", exist_ok=True)
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    z.extractall("netex_data")
    print("Extracted files:")
    for name in z.namelist():
        print(f"  {name}")
```

> [!NOTE]
> NeTEx deliveries are almost always **ZIP archives** containing one or more XML files. The file organisation varies by producer — some use one file per line, others a single large file.

---

## Step 2 — Understand the File Structure

A typical NeTEx delivery contains:

```
netex_data/
├── commun.xml              # Shared data: Network, Lines, Operators
├── ligne_B.xml             # Per-line file: Routes, Stops, Timetable
├── ligne_F.xml
├── calendrier.xml          # Calendar: DayTypes, OperatingPeriods
└── arrets.xml              # Stop places (sometimes separate)
```

Every NeTEx file is wrapped in a `PublicationDelivery`:

```xml
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" version="1.0">
  <PublicationTimestamp>2025-03-03T00:07:07Z</PublicationTimestamp>
  <ParticipantRef>PRODUCER_CODE</ParticipantRef>
  <dataObjects>
    <!-- One or more Frames here -->
  </dataObjects>
</PublicationDelivery>
```

### Listing the Top-Level Structure

```python
from lxml import etree

NS = {"n": "http://www.netex.org.uk/netex"}

def list_structure(xml_file):
    """Print the top-level frame structure of a NeTEx file."""
    tree = etree.parse(xml_file)
    root = tree.getroot()

    print(f"File: {xml_file}")
    print(f"  PublicationTimestamp: {root.findtext('.//n:PublicationTimestamp', namespaces=NS)}")
    print(f"  ParticipantRef: {root.findtext('.//n:ParticipantRef', namespaces=NS)}")

    # Find all frames (direct children of dataObjects, or inside CompositeFrame)
    for frame in root.iter():
        tag = etree.QName(frame.tag).localname
        if tag.endswith("Frame") and tag != "dataObjects":
            frame_id = frame.get("id", "no-id")
            children = [etree.QName(c.tag).localname for c in frame if not isinstance(c, etree._Comment)]
            print(f"  {tag} id={frame_id}")
            # Count members if it's a GeneralFrame or similar
            members = frame.find("n:members", namespaces=NS)
            if members is not None:
                child_types = {}
                for m in members:
                    tname = etree.QName(m.tag).localname
                    child_types[tname] = child_types.get(tname, 0) + 1
                for tname, count in child_types.items():
                    print(f"    {tname}: {count}")

# Run on all XML files in the directory
import glob
for f in sorted(glob.glob("netex_data/*.xml")):
    list_structure(f)
    print()
```

---

## Step 3 — Extract the Network and Lines

The **Network** and **Line** objects are usually defined in a shared file (e.g. `commun.xml`). A `Network` groups `Line`s; each `Line` describes a transit service known to passengers.

```python
def extract_lines(xml_file):
    """Extract all Lines from a NeTEx file."""
    tree = etree.parse(xml_file)

    lines = []
    for line_el in tree.iter("{http://www.netex.org.uk/netex}Line"):
        line_id = line_el.get("id")
        name = line_el.findtext("{http://www.netex.org.uk/netex}Name")
        short_name = line_el.findtext("{http://www.netex.org.uk/netex}ShortName")
        transport_mode = line_el.findtext("{http://www.netex.org.uk/netex}TransportMode")
        colour = line_el.findtext("{http://www.netex.org.uk/netex}Presentation/{http://www.netex.org.uk/netex}Colour")

        lines.append({
            "id": line_id,
            "name": name,
            "short_name": short_name,
            "transport_mode": transport_mode,
            "colour": colour,
        })

    return lines

# Example
for line in extract_lines("netex_data/commun.xml"):
    print(f"Line {line['short_name']}: {line['name']} ({line['transport_mode']}) colour=#{line['colour']}")
```

Expected output:
```
Line B: Parc des Fourriers - Hôpital (bus) colour=#FF6600
Line F: Centre Ville - Zone Commerciale (bus) colour=#009933
...
```

---

## Step 4 — Extract Routes and Stops

Each line file defines the **topology**: routes, stops, and journey patterns.

### Routes

A `Route` is an ordered sequence of points through the network in one direction:

```python
def extract_routes(xml_file):
    """Extract Routes and their associated Line reference."""
    tree = etree.parse(xml_file)
    ns = "http://www.netex.org.uk/netex"

    routes = []
    for route_el in tree.iter(f"{{{ns}}}Route"):
        route_id = route_el.get("id")
        name = route_el.findtext(f"{{{ns}}}Name")
        line_ref = route_el.find(f"{{{ns}}}LineRef")
        line_ref_id = line_ref.get("ref") if line_ref is not None else None

        routes.append({
            "id": route_id,
            "name": name,
            "line_ref": line_ref_id,
        })

    return routes

for route in extract_routes("netex_data/ligne_B.xml"):
    print(f"Route: {route['name']} → Line: {route['line_ref']}")
```

### Scheduled Stop Points

`ScheduledStopPoint`s are the logical stops along a route (as opposed to physical `StopPlace`s):

```python
def extract_stops(xml_file):
    """Extract ScheduledStopPoints with their coordinates."""
    tree = etree.parse(xml_file)
    ns = "http://www.netex.org.uk/netex"

    stops = []
    for ssp in tree.iter(f"{{{ns}}}ScheduledStopPoint"):
        stop_id = ssp.get("id")
        name = ssp.findtext(f"{{{ns}}}Name")
        lat = ssp.findtext(f"{{{ns}}}Location/{{{ns}}}Latitude")
        lon = ssp.findtext(f"{{{ns}}}Location/{{{ns}}}Longitude")

        stops.append({
            "id": stop_id,
            "name": name,
            "lat": float(lat) if lat else None,
            "lon": float(lon) if lon else None,
        })

    return stops

stops = extract_stops("netex_data/ligne_B.xml")
print(f"Found {len(stops)} stops")
for s in stops[:5]:
    print(f"  {s['name']} ({s['lat']}, {s['lon']})")
```

---

## Step 5 — Extract the Timetable

The timetable is defined by `ServiceJourney`s — each one represents a single trip of a vehicle along a `ServiceJourneyPattern` with specific passing times.

```python
def extract_timetable(xml_file):
    """Extract ServiceJourneys with their passing times."""
    tree = etree.parse(xml_file)
    ns = "http://www.netex.org.uk/netex"

    journeys = []
    for sj in tree.iter(f"{{{ns}}}ServiceJourney"):
        journey_id = sj.get("id")

        # Which pattern does this journey follow?
        jp_ref = sj.find(f".//{{{ns}}}JourneyPatternRef")
        if jp_ref is None:
            jp_ref = sj.find(f".//{{{ns}}}ServiceJourneyPatternRef")
        pattern_ref = jp_ref.get("ref") if jp_ref is not None else None

        # Which day types is it valid on?
        day_type_refs = []
        for dtr in sj.iter(f"{{{ns}}}DayTypeRef"):
            day_type_refs.append(dtr.get("ref"))

        # Extract passing times
        times = []
        for tt in sj.iter(f"{{{ns}}}TimetabledPassingTime"):
            departure = tt.findtext(f"{{{ns}}}DepartureTime")
            arrival = tt.findtext(f"{{{ns}}}ArrivalTime")
            times.append({
                "arrival": arrival,
                "departure": departure,
            })

        journeys.append({
            "id": journey_id,
            "pattern_ref": pattern_ref,
            "day_types": day_type_refs,
            "passing_times": times,
        })

    return journeys

journeys = extract_timetable("netex_data/ligne_B.xml")
print(f"Found {len(journeys)} service journeys")

# Show first journey
j = journeys[0]
print(f"\nJourney: {j['id']}")
print(f"  Pattern: {j['pattern_ref']}")
print(f"  Day types: {j['day_types']}")
print(f"  Stops: {len(j['passing_times'])}")
for i, t in enumerate(j['passing_times']):
    print(f"    Stop {i+1}: arrive={t['arrival']} depart={t['departure']}")
```

---

## Step 6 — Resolve References (Building the Full Picture)

NeTEx is a **graph of references**. To build a human-readable timetable, you need to resolve the chain:

```
ServiceJourney
  → JourneyPatternRef  → ServiceJourneyPattern
                            → pointsInSequence → StopPointInJourneyPattern
                                                    → ScheduledStopPointRef → ScheduledStopPoint
                            → RouteRef             → Route → LineRef → Line
```

Here is a complete resolver that builds a printable timetable:

```python
def build_timetable(xml_files):
    """
    Parse one or more NeTEx XML files and build a resolved timetable.
    Returns a list of dicts: {journey_id, line_name, route_name, stops: [{name, arrival, departure}]}
    """
    ns = "http://www.netex.org.uk/netex"

    # Index all objects by ID across all files
    lines = {}
    routes = {}
    patterns = {}
    stop_points = {}
    journeys = []

    for xml_file in xml_files:
        tree = etree.parse(xml_file)

        for el in tree.iter(f"{{{ns}}}Line"):
            lines[el.get("id")] = el.findtext(f"{{{ns}}}Name")

        for el in tree.iter(f"{{{ns}}}Route"):
            route_id = el.get("id")
            line_ref = el.find(f"{{{ns}}}LineRef")
            routes[route_id] = {
                "name": el.findtext(f"{{{ns}}}Name"),
                "line_ref": line_ref.get("ref") if line_ref is not None else None,
            }

        for el in tree.iter(f"{{{ns}}}ServiceJourneyPattern"):
            pattern_id = el.get("id")
            route_ref = el.find(f"{{{ns}}}RouteRef")
            stop_refs = []
            for spjp in el.iter(f"{{{ns}}}StopPointInJourneyPattern"):
                ssp_ref = spjp.find(f"{{{ns}}}ScheduledStopPointRef")
                if ssp_ref is not None:
                    stop_refs.append(ssp_ref.get("ref"))
            patterns[pattern_id] = {
                "route_ref": route_ref.get("ref") if route_ref is not None else None,
                "stop_refs": stop_refs,
            }

        for el in tree.iter(f"{{{ns}}}ScheduledStopPoint"):
            stop_points[el.get("id")] = el.findtext(f"{{{ns}}}Name")

        for el in tree.iter(f"{{{ns}}}ServiceJourney"):
            jp_ref = el.find(f".//{{{ns}}}JourneyPatternRef")
            if jp_ref is None:
                jp_ref = el.find(f".//{{{ns}}}ServiceJourneyPatternRef")
            times = []
            for tt in el.iter(f"{{{ns}}}TimetabledPassingTime"):
                times.append({
                    "arrival": tt.findtext(f"{{{ns}}}ArrivalTime"),
                    "departure": tt.findtext(f"{{{ns}}}DepartureTime"),
                })
            journeys.append({
                "id": el.get("id"),
                "pattern_ref": jp_ref.get("ref") if jp_ref is not None else None,
                "passing_times": times,
            })

    # Resolve references
    resolved = []
    for j in journeys:
        pattern = patterns.get(j["pattern_ref"], {})
        route = routes.get(pattern.get("route_ref"), {})
        line_name = lines.get(route.get("line_ref"), "Unknown line")
        route_name = route.get("name", "Unknown route")

        stops = []
        for i, stop_ref in enumerate(pattern.get("stop_refs", [])):
            stop_name = stop_points.get(stop_ref, stop_ref)
            time_entry = j["passing_times"][i] if i < len(j["passing_times"]) else {}
            stops.append({
                "name": stop_name,
                "arrival": time_entry.get("arrival"),
                "departure": time_entry.get("departure"),
            })

        resolved.append({
            "journey_id": j["id"],
            "line_name": line_name,
            "route_name": route_name,
            "stops": stops,
        })

    return resolved

# Usage
timetable = build_timetable(glob.glob("netex_data/*.xml"))
for entry in timetable[:3]:
    print(f"\n{'='*60}")
    print(f"Line: {entry['line_name']} | Route: {entry['route_name']}")
    print(f"Journey: {entry['journey_id']}")
    print(f"{'─'*60}")
    for stop in entry['stops']:
        dep = stop['departure'] or '      '
        arr = stop['arrival'] or '      '
        print(f"  {arr}  {dep}  {stop['name']}")
```

---

## Step 7 — Understand the Calendar

`ServiceJourney`s reference `DayType`s to express _when_ they run. The calendar file defines:

- **`DayType`** — A named type of day (e.g., "Monday–Friday except holidays")
- **`OperatingPeriod`** — A date range (e.g., 2025-01-06 to 2025-07-05)
- **`DayTypeAssignment`** — Binds a `DayType` to specific dates or `OperatingPeriod`s

```python
def extract_calendar(xml_file):
    """Extract the calendar (DayTypes, OperatingPeriods, DayTypeAssignments)."""
    tree = etree.parse(xml_file)
    ns = "http://www.netex.org.uk/netex"

    day_types = {}
    for dt in tree.iter(f"{{{ns}}}DayType"):
        dt_id = dt.get("id")
        name = dt.findtext(f"{{{ns}}}Name")
        # Properties like DaysOfWeek
        props = []
        for prop in dt.iter(f"{{{ns}}}PropertyOfDay"):
            dow = prop.findtext(f"{{{ns}}}DaysOfWeek")
            if dow:
                props.append(dow)
        day_types[dt_id] = {"name": name, "days_of_week": props}

    operating_periods = {}
    for op in tree.iter(f"{{{ns}}}OperatingPeriod"):
        op_id = op.get("id")
        from_date = op.findtext(f"{{{ns}}}FromDate")
        to_date = op.findtext(f"{{{ns}}}ToDate")
        operating_periods[op_id] = {"from": from_date, "to": to_date}

    assignments = []
    for dta in tree.iter(f"{{{ns}}}DayTypeAssignment"):
        dt_ref = dta.find(f"{{{ns}}}DayTypeRef")
        op_ref = dta.find(f"{{{ns}}}OperatingPeriodRef")
        date = dta.findtext(f"{{{ns}}}Date")
        is_available = dta.findtext(f"{{{ns}}}isAvailable")

        assignments.append({
            "day_type_ref": dt_ref.get("ref") if dt_ref is not None else None,
            "operating_period_ref": op_ref.get("ref") if op_ref is not None else None,
            "date": date,
            "is_available": is_available,
        })

    return day_types, operating_periods, assignments

day_types, periods, assignments = extract_calendar("netex_data/calendrier.xml")

print("Day Types:")
for dt_id, dt in day_types.items():
    print(f"  {dt_id}: {dt['name']} ({', '.join(dt['days_of_week'])})")

print("\nOperating Periods:")
for op_id, op in periods.items():
    print(f"  {op_id}: {op['from']} → {op['to']}")

print(f"\n{len(assignments)} DayTypeAssignments link day types to dates/periods")
```

---

## Adapting to Other Languages

The approach is the same in any language. Here are the key libraries:

| Language | XML Parser | XPath Support | Notes |
|----------|-----------|---------------|-------|
| **Python** | `lxml` | Full XPath 1.0 | Used in this guide |
| **Java** | `javax.xml`, `JAXB` | Full XPath | JAXB can generate classes from XSD |
| **C#** | `System.Xml.Linq` | XPath via `XPathNavigator` | LINQ to XML is idiomatic |
| **JavaScript/Node** | `fast-xml-parser`, `saxes` | Limited | Consider streaming for large files |
| **Elixir** | `saxy`, `xmerl` | Via `:xmerl_xpath` | Used in the [DGITM Livebook training](https://github.com/etalab/netex-france-formation/) |
| **Rust** | `quick-xml`, `roxmltree` | Via `roxmltree` | Good for high-performance parsing |
| **Go** | `encoding/xml` | Via `xmlquery` | Built-in streaming support |

### Key Patterns That Transfer

Regardless of language, the workflow is:

1. **Parse the XML** into a DOM or stream it with SAX/StAX
2. **Namespace-aware queries** — NeTEx uses `http://www.netex.org.uk/netex` as the default namespace
3. **Build an index** — Map object IDs to their parsed representations
4. **Resolve references** — Follow `*Ref` elements by looking up their `ref` attribute in your index
5. **Handle missing data** — Not all producers include all optional fields; code defensively

### XPath Cheat Sheet for NeTEx

```xpath
# All Lines in the document
//n:Line

# A specific Line by ID
//n:Line[@id='OPERATOR:Line:42:LOC']

# All ServiceJourneys referencing a specific pattern
//n:ServiceJourney[.//n:JourneyPatternRef/@ref='OPERATOR:ServiceJourneyPattern:B_001:LOC']

# All departure times
//n:TimetabledPassingTime/n:DepartureTime

# All ScheduledStopPoints with coordinates
//n:ScheduledStopPoint[n:Location]
```

(Where `n` is bound to `http://www.netex.org.uk/netex`)

---

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Forgetting the NeTEx namespace | Always register `http://www.netex.org.uk/netex` in your queries |
| Assuming one file = one frame | A single XML may contain multiple frames in a `CompositeFrame` |
| Parsing IDs for meaning | IDs are opaque; use `Name`, `ShortName`, `TransportMode` etc. for semantics |
| Ignoring `version` attributes | When resolving references, match on both `ref` and `version` if the producer uses versioned references |
| Loading everything into memory | For large national feeds, use streaming (SAX/StAX) or process per-file |
| Hardcoding element order | Different profiles and producers may include different optional elements; query by name, not position |

---

## Next Steps

| Goal | Resource |
|------|----------|
| Validate your own NeTEx XML | [Validation Guide](/Guides/Validation/Validation.md) |
| Understand NeTEx conventions (IDs, casing, ordering) | [NeTEx Conventions](/Guides/NeTExConventions/NeTEx_Conventions.md) |
| Build a consumer application (journey planner, MaaS) | [MaaS Consumers Guide](/Guides/MaaSConsumers/MaaSConsumers_Guide.md) |
| Understand EU regulatory context | [Regulatory Compliance Guide](/Guides/RegulatoryCompliance/RegulatoryCompliance_Guide.md) |
| Interactive training with live code (Elixir) | [DGITM NeTEx Training](https://github.com/etalab/netex-france-formation/) — runs free in [Livebook](https://livebook.dev/) |
| Look up specific NeTEx objects | Browse the Objects section in the sidebar |
