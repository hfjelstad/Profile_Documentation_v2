# Glossary

## View

Definition
- In this profile, the term “View” is used in two complementary senses:
  1) Publication view: The way data is selected and packaged inside a NeTEx PublicationDelivery for a specific purpose or audience (for example, a Timetable publication view or a Network publication view).
  2) Thematic view: A conceptual grouping used in the profile to scope content and requirements (for example, Timetable, Network, Fares). It helps readers navigate the documentation but does not imply a distinct NeTEx structure on its own.

Clarifications
- DatedCalls are not a separate “view”. They are child elements of a DatedServiceJourney within a TimetableFrame and describe the stop-by-stop call sequence for a specific operating day.
- DatedServiceJourney and its DatedCalls belong to the Timetable publication view. In practice, they appear in a PublicationDelivery that contains a TimetableFrame.

Notes
- The “view” wording is purely to reduce ambiguity in documentation. When in doubt, prefer the precise NeTEx model terms (e.g., PublicationDelivery, TimetableFrame, DatedServiceJourney, DatedCalls).

See also
- Objects/DatedServiceJourney (profile object documentation)
