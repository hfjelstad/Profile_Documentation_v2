# Codespace

## Structure Overview

```text
Codespace
  ├─ @id (1..1)
  ├─ Xmlns (1..1)
  └─ XmlnsUrl (1..1)
```

## Table

| Element | Type | XSD | Description | Path |
|---------|------|-----|-------------|------|
| @id | ID | 1..1 | Unique identifier for the codespace | Codespace/@id |
| Xmlns | String | 1..1 | XML namespace prefix (e.g., ERP, NSR) | Codespace/Xmlns |
| XmlnsUrl | String | 0..1 | Full namespace URL for global uniqueness | Codespace/XmlnsUrl |
