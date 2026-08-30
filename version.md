VERSION: 5.0.5-beta.1
DETAILS:

renamed: "Hide native macOS Dock" is now "Deep-hide native macOS Dock", and the setting states that macOS can still reveal its Dock at the physical screen edge or in Mission Control
improved: A failed Dock reload gets one bounded retry instead of rewriting preference keys or looping
improved: Deep-hide is re-applied automatically when macOS replaces the Dock process, and never touches your Dock while deep-hide is off
improved: All Docks Diagnostics captures live Dock preferences, apply/retry state, Dock process identity, on-screen Dock window geometry, screen frames, and pointer-to-edge context — never window titles
