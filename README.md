# ExtraDock 5 Updates

Sparkle update feed and release distribution for [ExtraDock 5](https://github.com/AppitStudio/ExtraDock5) by AppIt Studio.

- **Appcast:** https://appitstudio.github.io/extra-dock5-updates/appcast.xml
- **Release notes:** https://appitstudio.github.io/extra-dock5-updates/release-notes.html
- **Downloads:** hosted on this repo's GitHub Releases (betas are pre-releases tagged `v{version}`)

Beta builds are delivered through the same appcast using Sparkle 2 channels (`<sparkle:channel>beta</sparkle:channel>`); users opt in via the app's update-channel setting.

## License-safe feed publishing

GitHub Pages must use **GitHub Actions** as its publishing source. The
`Register releases and publish feed` workflow validates the appcast, registers
its releases with Keyper, verifies Keyper's product/track/version/download
response, and only then deploys the feed and release notes. Do not re-enable
branch-based Pages publishing: it bypasses the registration gate.

A registration failure (including an Imunify360 firewall rejection) keeps the
previous feed live. Check the failed workflow, resolve the failure, then rerun
it or dispatch the workflow on `main`. The registrar retries transient failures
three times; it never treats a firewall challenge or an unrelated response as
successful registration. Persistent firewall blocks need a narrowly scoped
hosting rule for authenticated release registration or a trusted runner.

Stable and beta releases are retained under Keyper's `v5-stable` compatibility
track because the shipped app sends that track for both channels. Keyper must
validate installed beta versions while selecting only stable releases for the
stable latest-version and recovery-download fields.
