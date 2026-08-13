VERSION: 5.0.1-beta.3
DETAILS:

✨ new: DockFlow integration bridge — ExtraDock publishes its docks to DockFlow so the two apps can work together
🐛 bug fix: Running indicators stay fully visible at Small, Medium and Large on every edge and floating orientation
🐛 bug fix: App artwork refreshes on appearance change — no more stale light-mode icons in Dark Mode
🐛 bug fix: Clicking Microsoft Teams no longer risks terminating it; running Teams is routed through public activation only
🐛 bug fix: Launcher and static widgets fill their full cell again (the global 0.8× artwork inset no longer shrinks Medium/Large)
🐛 bug fix: Dragging a dock across displays no longer shakes or jumps at the screen seam, with steadier edge/corner snapping
🐛 bug fix: Diagnostics log export no longer fails with an opaque error — it retries without the predicate, writes atomically and verifies the artifact
