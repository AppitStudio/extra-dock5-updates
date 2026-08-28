VERSION: 5.0.4-beta.4
DETAILS:

🐞 bug fix: A dock combining Hide Automatically with Toggle with keyboard shortcut could be locked out of edge reveal — both a shortcut-initiated hide and the shortcut's configured re-hide timer installed a manual hidden override, and manual hide outranks auto-hide, so the mouse reveal strip could never reopen the dock (DockFlow only appeared to repair it because a profile switch clears that override)
🐞 bug fix: In combined auto-hide + hotkey mode the keyboard shortcut is now a temporary visibility overlay — a press can reveal an auto-hidden or fullscreen-hidden dock, and a second press or the timed re-hide releases the override and returns the dock to automatic policy, so subsequent edge dwell reveals it normally
🔒 unchanged: Explicit menu/App Intent hide remains sticky and still beats the reveal strip; docks without auto-hide keep the existing sticky hotkey toggle and timed manual-hide behavior, preserving V4's delay and hover-paused re-hide timing; the DockFlow protocol and implementation are unchanged
