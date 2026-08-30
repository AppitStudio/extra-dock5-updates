VERSION: 5.0.5-beta.2
DETAILS:

bug fix: Desktop-widget docks no longer claim hovers and clicks through an app window covering them — pointer ownership is now hit-tested against the real window order instead of geometry alone
bug fix: Hover name pills for desktop-widget docks follow their dock's layer (above desktop icons, below normal app windows) instead of popping up at popup-menu level above every window
