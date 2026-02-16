# Get Started Guide

## Introduction to NeTEx
NeTEx (Network Timetable Exchange) is a CEN standard for exchanging public transport data, including timetables, fares, and related information. It is based on XML and designed to support interoperability between different systems.

## Basic Structure
A NeTEx document is organized into **Frames**, each containing related data elements. Common frames include:

### Common Frames
- [ServiceFrame](../Frames/ServiceFrame/Description_ServiceFrame.md): Contains routes, lines, and scheduled stop points.
- [FareFrame](../Frames/FareFrame/Description_FareFrame.md): Defines fare structures and pricing information.
- [ResourceFrame](../Frames/ResourceFrame/Description_ResourceFrame.md): Holds shared resources like operators and organizations.

## Validation
To ensure data quality, validate your NeTEx files against the official schema. Tools like **NeTEx Validator** or **ENTUR Validator** can be used for this purpose.

## Useful Links
- [CEN NeTEx Standard](https://www.cen.eu)
- [ENTUR Developer Portal](https://developer.entur.org)

## Relaterte rammer
Denne guiden gir en introduksjon til NeTEx og peker til rammer som er vanlige i norske profiler. For detaljerte beskrivelser, se de respektive rammebeskrivelsene i dokumentasjonen.