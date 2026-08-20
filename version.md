VERSION: 5.0.3-beta.2
DETAILS:

✨ new: The ExtraDock status-item dropdown now renders every configured dock as a submenu — Show/Hide, Enabled, Position Mode, Size and Open in Manager… — with New Dock at the top, composed through the same `MenuBarDockMenu` used by the status item so state cannot drift
✨ new: Floating docks regain V4's `DockQuickMenuBuilder` Lock Position toggle, placed between Position Mode and Size; pinned docks omit it
✨ new: Custom Text collapse labels accept and persist up to five Swift characters (was three), matching current V4 behavior; composed emoji still count as one character
🔧 improved: The collapse button now consumes the largest square that fits its runtime slot (`min(iconSize, innerThickness)`) instead of the old 38pt cap — 33pt → 48pt at default settings, with the text viewport growing ~28pt → ~45pt
🐛 bug fix: `MenuBarExtra` read `AppDelegate.coordinator` directly while its scene was built before `applicationDidFinishLaunching`, leaving a stale nil branch that dropped Media and every dock row; status-menu content now lives in `MenuBarMenuRoot`, which observes `AppDelegate` and rebuilds when the published coordinator arrives
🐛 bug fix: Collapse-label font sizes are derived from the canonical inline-button square through one explicit shared text viewport, so expanded and collapsed rendering resolve to the same size and the label no longer jumps during the morph
🐛 bug fix: The global click-through monitor wrote `interaction.cursor` on every mouse move, and geometry's reads of the single observable struct reran the whole frame/effects/window pass; `InteractionState` is now nested per-property observable and pass-through reassigns `ignoresMouseEvents` only on a real interactive-region crossing
