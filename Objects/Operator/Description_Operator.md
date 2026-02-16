# Description: Operator

The **Operator** element in NeTEx represents an organization that provides public transport services. It is a core entity used to identify the company responsible for operating scheduled journeys, lines, or other transport services.

## Purpose
The Operator element is used to define the legal or commercial entity that runs the transport services. It can be referenced by other NeTEx elements such as `Line`, `ServiceJourney`, and `DatedServiceJourney`.

## Key Relationships
- **Authority**: The Authority is the organization responsible for planning and managing the transport network, while the Operator executes the services.
- **ResponsibilitySet**: Defines roles and responsibilities, which can include the Operator's obligations.

## Usage
Operators are typically defined in the `organisations.xml` file within a NeTEx dataset and referenced by their unique ID in other elements.

