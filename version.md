VERSION: 5.0.3-beta.4
DETAILS:

🐞 bug fix: `IconGeometry.liftVector` gave neutral floating **vertical** docks the horizontal floating transform `(x: 0, y: -lift)`, so every cursor-derived magnification change translated icons along the bar's own main axis — the same axis the mouse was traversing — producing the reported hover "shake"
🐞 bug fix: Magnification lift is now orientation-aware — a neutral floating vertical dock grows symmetrically from its slot center with zero translation, matching what `growthAnchor` already did
🔧 improved: Floating horizontal docks keep bottom-Dock-style upward lift and edge-resolved top/left/right docks keep their directional lift — only the neutral-vertical case changed
🔧 improved: The same helper still drives both rendered pixels and reported magnified hit regions, so a magnified icon's click target continues to match its appearance; the discrete launch/attention bounce is unchanged
