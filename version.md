VERSION: 5.0.3
DETAILS:

✨ new: Every configured dock now appears as its own submenu in the ExtraDock status-icon menu and app menu — Show/Hide, Enabled, Position Mode, Size and Open in Manager…, with New Dock at the top
✨ new: Lock Position is back for floating docks, right in the dock's menu
✨ new: Export Dock Diagnostics from the Manager or Settings → Diagnostics — one dock or all docks, with paths, custom names and locations redacted
🔧 improved: The collapse button now fills the largest square its slot allows (33 pt → 48 pt at default settings) and accepts up to five characters of custom text
🐞 bug fix: Floating docks no longer drift, shake or hop from pointer movement or idle layout — only a real drag moves a dock
🐞 bug fix: Magnified icons on vertical floating docks grow symmetrically in place instead of sliding along the bar, with hit targets matching what is drawn
🐞 bug fix: Finder now honors the dock's frontmost action (None, Minimize, Hide, Cycle), restores the minimized window instead of duplicating it, and no longer dead-clicks when alternating with the macOS Dock; both Finder menus gained New Finder Window
🐞 bug fix: Apps, Screenshot and other LSUIElement launchers settle the moment they hand off instead of bouncing 20–30 seconds with clicks suppressed
🐞 bug fix: Reserve Dock Space now yields to keyboard and window-manager moves, so shortcut/Raycast tiling settles inside the reserved space even with Active on Drag off
🐞 bug fix: The Screens tab re-binds to the newly selected dock, so per-dock screen toggles stop writing to the previous dock
🐞 bug fix: ExtraDock 4 dock copies made before March 2026 reused item IDs and failed on import — collisions are now repaired automatically, preserving V4 order and content
