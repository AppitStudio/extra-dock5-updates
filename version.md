VERSION: 5.0.3-beta.8
DETAILS:

🐞 bug fix: `/System/Applications/Apps.app` and other `LSUIElement` launcher bundles hand their UI to another service and terminate within milliseconds, so `openApplication` delivered no timely completion and no `NSRunningApplication`; ExtraDock had no terminal evidence and ran the bounce plus click suppression out to the full 20-second `ed5-oqhk` watchdog
🔧 improved: Launch routing now derives its API from bundle metadata — an `LSUIElement` bundle uses `NSWorkspace.open(_:)`, whose synchronous Boolean is LaunchServices acceptance evidence, and a current accepted request ends bounce through the existing generation-fenced no-process handoff. No Apple bundle identifier is special-cased
🔧 improved: Launch completion distinguishes process-bearing success, successful no-process handoff, and failure; ordinary app bundles keep asynchronous `openApplication` plus lifecycle ownership, and failure, replacement, retry and the 20-second last-resort fence are unchanged so stale callbacks cannot affect a replacement attempt
