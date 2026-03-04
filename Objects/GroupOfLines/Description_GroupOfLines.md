# GroupOfLines

Purpose
- Groups multiple Line objects into a logical set within a ServiceFrame for common management, branding, distribution, or filtering.

Scope
- Used in ServiceFrame/groupsOfLines to reference existing Line instances via LineRef.

Key characteristics
- Identified by stable id and version.
- Human-readable Name and optional ShortName.
- Optional Description and PrivateCode for back-office usage.
- Members are one or more LineRef elements.

Usage notes
- Define all Line objects before referencing them as members of a GroupOfLines.
- Use a consistent codespace (e.g., ERP) for all identifiers.
- GroupOfLines does not create new Lines; it only references existing Lines.
