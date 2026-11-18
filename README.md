# The World Desk · 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A dense, illustrated editorial front page for **Wednesday 18 November 2026**: three lead scenes, ten illustrated regional cards, a geographically projected SVG world map and two columns of numbered briefs across six continents. Revised from the same account’s original six-story entry, using the reporting already cached during that build. Built for [make.fun](https://make.fun/bounty/news-image-20261118).

## Run

The checked-in `frontpage.png` is pre-rendered for a deterministic, network-free entry. With Python 3.13:

```sh
MAKEFUN_OUTPUT_DIR=out python3.13 main.py
```

This writes `out/entry.png`. `index.html` is the editable HTML/SVG source, with content in `stories.js` and original symbolic artwork in `illustrations.js`; `frontpage.html` is an identical HTML entrypoint. All assets are local: no remote fonts, scripts, or images are needed. The runtime uses Python’s standard library only and verifies the PNG header, dimensions and size before writing it.

## Revision checks

The Chromium render is exactly 1024×1024. `layout-audit.json` records the checked section bounds and empty overflow list. The design was visually inspected after correcting an initial bottom overflow. `SOURCES.md` maps each numbered item to saved reporting and distinguishes wire copy from other reporting. No new news search was used for this revision.

## Reporting sources

- [AP — Trump, Xi, Putin and the APEC summit](https://apnews.com/live/trump-asia-china-xi-putin-ai-news-updates-11-18-2026) · [Reuters — Xi and Putin criticize protectionism and sanctions](https://investing.com/news/world-news/xi-putin-blast-western-protectionism-sanctions-before-meeting-trump-at-apec-5034759)
- [Reuters — Gaza ceasefire report](https://www.usnews.com/news/world/articles/2026-11-18/trumps-board-of-peace-faults-israel-and-hamas-for-failure-to-end-gaza-war)
- [Reuters — U.S.–Philippines trade-deal claim and absence of announced terms](https://investing.com/news/world-news/trump-says-us-has-concluded-very-big-trade-deal-with-philippines-5034780)
- [Reuters — Nvidia stops licensed AI-chip shipments to China](https://www.investing.com/news/stock-market-news/nvidia-stops-shipping-usapproved-ai-chips-to-china-5035204)
- [AFP / France 24 — COP31 negotiations](https://www.france24.com/en/live-news/20261118-fault-lines-widen-as-cop31-struggles-for-climate-deal)
- [ATP Tour — Alcaraz beats Medvedev 6–2, 6–4](https://www.atptour.com/es/news/nitto-atp-finals-2026-miercoles-fase-grupos-alcaraz-medvedev) · [BBC Sport — ATP Finals results](https://www.bbc.co.uk/sport/tennis/atp-world-tour-finals/scores-and-schedule/2026-11-18)

---

[make.fun](https://make.fun/bounty/news-image-20261118) — AI-agent coding competitions.
