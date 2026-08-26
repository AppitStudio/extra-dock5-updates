VERSION: 5.0.4-beta.2
DETAILS:

🐞 bug fix: DockFlow profile-selected docks were routed through the sticky Show Dock command, installing a manual override that outranked auto-hide and fullscreen policy until toggled by hand; they now clear the override and return to their configured visibility, while profile-hidden docks stay sticky-hidden
🐞 bug fix: A dock restored to automatic hiding is ordered back into WindowServer at the correct level with its hidden reveal geometry, so its edge and halo can reveal it again
🐞 bug fix: Clearing a manual override now propagates to all-screen replicas instead of leaving them in the previous state
🐞 bug fix: A pending hotkey rehide timer is cancelled when a profile releases a dock back to automatic
