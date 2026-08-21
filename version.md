VERSION: 5.0.3-beta.6
DETAILS:

🐞 bug fix: An unlocked floating `DockPanel` accepted *any* same-size origin write while `allowsUserDrag` was true, so AppKit/SwiftUI layout and hover probes moved an idle panel one point off its engine frame at ~0.37 s cadence — the reporter's dock parked beside the native Dock hopped up and down continuously without being touched
🔧 improved: `allowsUserDrag` is now treated as a capability, not frame ownership — `shouldAcceptFrameChange` only lets a same-size origin write through inside an explicit transaction: `DockController`'s new `applyExplicitDragOrigin(_:)` latch or the existing native AppKit background-drag latch
🔧 improved: `DockController`'s idle frame-origin reconciliation routes through `applyExplicitDragOrigin(_:)` instead of calling `setFrameOrigin` directly, so the choke point has no general-purpose escape hatch
🔧 improved: No positioning-engine, screen-resolver, or persistence rule changed — `PanelChokePointTests` covers the idle-probe rejection alongside the accepted explicit-drag and native-background paths
