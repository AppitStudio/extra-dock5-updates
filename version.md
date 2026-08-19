VERSION: 5.0.2
DETAILS:

✨ new: Bluetooth Battery widget ported from ExtraDock 4 — charge and connection state for AirPods (per-bud + case), Magic Keyboard/Mouse/Trackpad, controllers and any accessory macOS publishes a level for, with a 1–4 cell span; third-party BLE keyboards and mice are read directly over the standard GATT Battery Service
✨ new: Icon size gains a Custom segment with the exact 20–128 pt slider (the "Huge" preset folds into Custom); Bar thickness moved directly under it and gained Auto and Custom
✨ new: Auto bar thickness is the default on every dock, including existing ones — the bar stays exactly as tall as the tallest icon plus padding, and applies to the menu-bar quick-set, "Match macOS Dock Size", themes, paste and import; picking any thickness yourself pins it permanently
✨ new: Right-clicking either drag handle or any dock item (app, file, folder, Trash, widget) now ends in an ExtraDock submenu — Hide Dock, Pin to Edge, Copy Settings, Paste Settings, Open ExtraDock Management
✨ new: Drag handle on hover for floating docks — with "Show drag handle" off, hovering an unlocked floating dock for 1 second reveals a compact move affordance that fades 2.5s after you leave; it renders outside the bar, so nothing about size or position changes
✨ new: First-appearance animation — docks fade and scale in (0.30s) once, after they're authoritatively positioned; Reduce Motion gets an 0.18s crossfade instead
🐛 bug fix: Floating docks no longer jitter near the macOS Dock — a one-point oscillation traced to programmatic frame updates being misread as user moves; frame ownership is now explicit and floating positions sit on a stable physical-screen basis
🐛 bug fix: Dragging an icon no longer drags the whole dock — one owner is decided at mouse-down, so item starts always reorder and only genuine empty bar space moves a floating unlocked dock
🐛 bug fix: "Reserve space for this dock" recovers on its own after a lost Accessibility observer or event, with bounded retries and a convergence sweep — no toggle-off/on needed
🐛 bug fix: Item names appear on hover after a 0.3s dwell for apps, files, folders, widgets and Trash, independent of Screen Recording permission; "Always show label" renders inside the existing slot and survives relaunch, import and export
🐛 bug fix: Divider footprint is back to V4's max(2, side spacing × 2) points, and Side spacing actually changes occupancy
🐛 bug fix: Empty Trash confirmation can no longer hide behind the Manager window — it activates only for itself and restores your previous app afterward
🐛 bug fix: Launcher apps can't get stuck bouncing — every launch attempt is fenced by identity and generation
🐛 bug fix: No position flash at startup — screen-dependent docks stay hidden until display topology settles, then appear directly at their saved location
🐛 bug fix: Hide Dock is back at the top of the dock background right-click menu
🐛 bug fix: Auto bars normalize on load as well as on mutation, and custom absolute corner radii are never rescaled by a refit
