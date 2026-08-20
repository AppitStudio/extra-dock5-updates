VERSION: 5.0.3-beta.1
DETAILS:

🐛 bug fix: Valid historical V4/V5 `dockState.json` files whose duplicated docks reuse element UUIDs now import successfully — ExtraDock 4's dock-copy path retained item identities before 2026-03-23, colliding with V5's app-global `dock_element.id` primary key (SQLite error 19)
🐛 bug fix: Identity repair keeps the first occurrence's original UUID and gives every later collision a deterministic replacement derived from stable import inputs, preserving V4 order and content without weakening V5's uniqueness invariant
✨ new: The import report gains a "Repaired automatically" section listing each repaired dock/element and stating that no action is required; migrated-element report IDs and review flags follow the repaired identity
