VERSION: 5.0.4-beta.3
DETAILS:

🐞 bug fix: Live widget content is no longer compressed into the persisted footprint — the user's 1–4 cell selection is treated as a minimum and the widget requests additional whole cells whenever its visible tiles require them (Bluetooth Battery with three or more accessories)
🐞 bug fix: iPhone Mirroring/Handoff reverse-DNS device identifiers exposed by the native Dock through AXStatusLabel were rendered as a fixed-size red notification capsule spanning several dock icons; both live badge tiers now share one system-value parser that rejects reverse-DNS identifiers, URLs, control text, oversized labels, and non-count text from numeric-only fallback fields
🐞 bug fix: Badge display content is independently capped at eight characters at the renderer, so an unexpected future source cannot expand a capsule across neighboring items even if it bypasses the live readers
