VERSION: 5.0.3-beta.5
DETAILS:

🐞 bug fix: `DockScreensEditor`'s private `ScreenAssignmentModel` stayed bound to the previously selected dock's UUID when the sidebar selection changed while the **Screens** tab was active — the title and row selection moved to dock B while assignment state and toggle writes still targeted dock A, making per-dock screen settings look universal
🐞 bug fix: Known-screen toggles and **Show on All Screens** now write to the dock you actually have selected, not the one you switched away from
🔧 improved: `DockDetailEditor` keys the dock-scoped Screens editor by `config.id`, so a selection change rebuilds the immutable-ID model and clears its repair/rename/forget/export transient state; the Manager-owned Screens tab selection is unchanged
🔧 improved: No resolver, EDID, registry, confidence, persistence-schema, or runtime placement rule changed — a hosted two-dock regression test proves only the selected dock mutates
