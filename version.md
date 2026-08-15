VERSION: 5.0.1
DETAILS:

✨ new: DockFlow integration — ExtraDock publishes docks to DockFlow, surviving Dock restarts triggered by preset switches
✨ new: App-wide master toggle in Settings → Behavior to show or hide running-app indicator dots across every dock (per-dock opt-outs still respected)
✨ new: App-wide running indicator color override — pick one color for all docks, or keep Default for each dock's accent color with the adaptive light/dark palette
✨ new: Custom Finder widget icons with one-click Use Default revert
✨ new: Type Size control on the Clock widget
⚡ improved: Running indicators use native-Dock spacing and sizing, legible in light and dark appearance
⚡ improved: Launch bounce respects the macOS "Animate opening applications" setting (Reduce Motion still wins)
⚡ improved: Item menus surface app-wide gesture state with Enable Click/Scroll Gestures shortcuts
⚡ improved: Deeper integration diagnostics — Dock restarts, dock repairs, and DockFlow request/response logging
🐛 bug fix: Docks self-repair after a macOS Dock restart; hidden docks stay hidden and show/hide is state-confirmed
🐛 bug fix: Gauge widget text color modes restored (Automatic / White / Black / Custom, incl. V4 imports)
🐛 bug fix: Imported clocks keep full two-cell width; flexible spacer width restored to 2–3000 pts with correct V4 import
🐛 bug fix: Per-app click/scroll gesture overrides persist across restarts
🐛 bug fix: V4 import of hidden docks and multi-display dock placement corrected
🐛 bug fix: Smooth multi-display dragging without seam shake; steadier edge/corner snapping
🐛 bug fix: App Stack custom icons restored to full V4 parity
🐛 bug fix: Launcher-style apps can no longer bounce forever (20-second safety net)
🐛 bug fix: Chrome web apps restore properly from minimize; Microsoft Teams no longer risks termination on click
🐛 bug fix: Running indicators no longer clip at any size, edge, or floating orientation
🐛 bug fix: Dark mode icon artwork refreshes immediately on appearance change
🐛 bug fix: Launcher and static widgets fill their cells at Medium and Large
🐛 bug fix: Relaunching ExtraDock no longer leaves two instances running
🐛 bug fix: Diagnostics export retries, verifies the file, and reports real errors
