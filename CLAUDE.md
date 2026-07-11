# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository manages the Sparkle auto-update feed for **ExtraDock 5**, the AppIt Studio rewrite of ExtraDock (bundle id `com.appitstudio.ExtraDock`). It is 100% separate from the v4 feed (`extra-dock-updates`): its own appcast, its own EdDSA key (keychain account `ExtraDock5`), its own GitHub releases.

## Architecture

- **`appcast.xml`** — Production Sparkle feed, served at `https://appitstudio.github.io/extra-dock5-updates/appcast.xml` (this is the `SUFeedURL` baked into the app).
  - Stable items carry no channel tag; **beta items carry `<sparkle:channel>beta</sparkle:channel>`** — the app is Sparkle 2 and gates betas via `allowedChannels` (user's "Beta" setting), NOT via a separate feed URL.
  - Keep the latest stable item and (optionally) the latest beta item newer than stable. Remove a beta item once the matching stable ships.
  - Critical fields per item: `sparkle:version` (integer build counter — V5 uses a monotonic counter, NOT dots-removed), `sparkle:shortVersionString`, `enclosure url` (GitHub release DMG), `sparkle:edSignature`.
- **`release-notes.html`** — Styled notes page linked via `sparkle:fullReleaseNotesLink`. New `<div data-sparkle-version="X.Y.Z">` blocks go at the top of `<body>`.
- **`version.md`** — Human-readable summary of the latest published version.
- **`dmg/`** — Local staging folder for `generate_appcast` (DMG + generated appcast are gitignored; only root `appcast.xml` is the published feed).

## Publishing

Signing: `generate_appcast --account ExtraDock5 dmg/` (the EdDSA key lives in the keychain under account `ExtraDock5`; public key `vcOnM1QRnMarzsooeDUiviiBWw6HplEusi+dO+lfZaM=` is in the app's Info.plist).

DMG hosting: GitHub Releases on this repo. Stable: tag `v{version}`. Beta: tag `v{version}` (e.g. `v5.0.0-beta.1`) marked pre-release — versioned tags, never a reused `beta` tag, because appcast beta items must have stable URLs.

The full pipeline is driven by the `/full-publish` skill and `publish.sh` in `/Users/asafmazuz/Documents/MacApps/updates` (app key: `extradock5`). Note: V5's version lives in `Config/Shared.xcconfig` (`MARKETING_VERSION` / `CURRENT_PROJECT_VERSION`), not in the pbxproj.
