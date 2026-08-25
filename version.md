VERSION: 5.0.4-beta.1
DETAILS:

🐞 bug fix: Two displays of the same model shared one screen identity — toggling or removing one affected its twin and per-app placement could capture the wrong panel; duplicate rows are now instance-qualified and independent
🐞 bug fix: Selecting a screen now records the user-confirmed topology, so a recycled runtime display ID after sleep/wake no longer moves docks to the sibling monitor; genuine ties stay ambiguous instead of resolving by iteration order
🐞 bug fix: Display-service matching gates identical vendor/product candidates on the CoreGraphics display UUID and refuses unresolved ties, so one panel can no longer inherit its sibling's EDID UUID
🐞 bug fix: Explicitly hidden screens and unreferenced V4 ghost entries no longer clutter Known Screens, while referenced offline assignments remain manageable
🐞 bug fix: Legacy attachedToScreen intent imports as a restrictive assignment, and movable V4 docks keep a nonrestrictive preferred screen
🔧 improved: CFBundleDisplayName is set, so macOS shows the app as ExtraDock everywhere
