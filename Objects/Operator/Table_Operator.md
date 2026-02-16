# Table: Operator Attributes

| **Attribute**       | **Type**   | **Usage**       | **Description** |
|----------------------|-----------|-----------------|-----------------|
| `id`               | Identifier | Mandatory       | Unique identifier for the Operator. |
| `version`          | String     | Optional        | Version of the Operator element. |
| `Name`             | String     | Mandatory       | Name of the Operator organization. |
| `ShortName`        | String     | Optional        | Abbreviated name of the Operator. |
| `ContactDetails`   | Element    | Optional        | Contact information for the Operator. |
| `OrganisationType` | String     | Optional        | Type of organization (e.g., company, cooperative). |

## Relationships
- **Authority**: Linked via `AuthorityRef`.
- **ResponsibilitySet**: Linked via `ResponsibilitySetRef`.

