VERSION: 5.0.3-beta.7
DETAILS:

🐞 bug fix: Finder representations (FinderWidget, pinned Finder, Live Dock Finder) executed lifecycle-seeded `ClickSemantics` machines against a 150 ms CG snapshot, so alternating the native Dock with ExtraDock could minimize, reopen or dead-click Finder from contradictory state
🔧 improved: Every Finder representation now enters one `ActivationService` transaction using a live `NSWorkspace` process plus the owning dock's frontmost action; native-Dock policy applies None/Minimize/Hide/Cycle only when the live frontmost PID and a live on-screen user-facing window agree, otherwise it focuses/restores/reopens
🔧 improved: CG caches are transaction-local and the reopen path can restore a live AX main/focused minimized window without accepting cached descriptors or V4's residual ghosts, so a minimize/restore cycle returns the same window ID with no duplicate
new: Finder widget and Live Dock Finder expose the Finder-standard **New Finder Window** context-menu command (widget opens its configured location, app element opens Home), gated on the authoritative `com.apple.finder` bundle ID
🐞 bug fix: AX move/resize callbacks now sample `NSEvent.pressedMouseButtons` at event time, so keyboard/automation window writes get one debounced PID-targeted correction plus a settle recheck and land inside reserved dock space even with Active on Drag off
