VERSION: 5.0.3-beta.3
DETAILS:

✨ new: `DockDiagnosticsExporter` writes a human-readable support report for the selected dock, reached from a new Dock Actions menu in the Manager toolbar ("Export Dock Diagnostics…"), restoring V4's `DockSettingsService.copyTroubleshootingSummary` behavior as a saved file
✨ new: Settings → Diagnostics gains an All Docks export that emits one report covering every persisted dock, alongside the existing screen-decision-log and log exports
✨ new: Reports embed app version, OS version, Accessibility/Screen Recording permission state, persisted `DockConfig`/`AppSettings` JSON, and per-instance runtime snapshots (panel frame, alpha, window number, resolved visibility, collapse/reveal fractions, screen frames and fingerprint) — one persisted dock yields several snapshots when Show on All Screens is on
🔧 improved: Item paths, bundle IDs, custom item names, folder/network URLs and raw widget `configJSON` payloads are redacted from the embedded configuration before writing, so exports are safe to attach to a support email
🔧 improved: Both exports are indexed by Settings search; report formatting is pure and headless-testable, with collection and `NSSavePanel` presentation kept app-side
