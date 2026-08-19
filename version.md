VERSION: 5.0.2-beta.2
DETAILS:

✨ new: Bar thickness moved under Icon size and defaults to Auto — the bar fits the tallest cell plus padding, so large icons no longer overflow a bar that never grew
✨ new: Custom bar thickness slider; picking any preset or dragging Custom pins the bar permanently
✨ new: Icon size gains a Custom segment with the exact 20–128 pt slider; the "Huge" preset folds into Custom so quick-set and the Style tab share one Small/Medium/Large vocabulary
⚡ improved: Menu quick-set, "Match macOS Dock Size", themes, paste and import all refit an Auto bar, carrying the matching Soft/Round corner radius
🐛 bug fix: Auto bars normalize on load as well as on mutation — a bar its icons had outgrown is corrected at launch, and the control can never show Auto while the bar disagrees
🐛 bug fix: Custom absolute corner radii are never rescaled by a refit
