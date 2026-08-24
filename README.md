# ExtraDock 5 Updates

Sparkle update feed and release distribution for [ExtraDock 5](https://github.com/AppitStudio/ExtraDock5) by AppIt Studio.

- **Appcast:** https://appitstudio.github.io/extra-dock5-updates/appcast.xml
- **Release notes:** https://appitstudio.github.io/extra-dock5-updates/release-notes.html
- **Downloads:** hosted on this repo's GitHub Releases (betas are pre-releases tagged `v{version}`)

Beta builds are delivered through the same appcast using Sparkle 2 channels (`<sparkle:channel>beta</sparkle:channel>`); users opt in via the app's update-channel setting.

## Update-entitlement release history

The production appcast is append-only. Keep every stable item and every beta item that may still be the newest update released within a customer's update window. Never replace an item's `pubDate`; update eligibility compares that signed feed date with Keyper's server-issued expiry date.

`scripts/register_releases.py` validates every retained item and registers it idempotently with Keyper after an appcast change reaches `main`. Configure the dedicated server-only GitHub secret `KEYPER_RELEASE_TOKEN`. It is the release-write credential for the `v5-stable` feed track; both stable and Sparkle beta-channel items belong to that feed track. Never use the validation bearer embedded in the shipped app.

The stable 5.0.0–5.0.3 entries were reconstructed from their original committed appcasts, including their original `pubDate`, build number, archive length, URL, and EdDSA signature. Beta rebuilds before this change remain available in Git history but are not republished as install candidates; future beta items must remain in the appcast until they are no longer needed for update-window eligibility.
