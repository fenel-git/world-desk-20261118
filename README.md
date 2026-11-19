# The World Desk · 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

The World Desk for **Wednesday 18 November 2026** covers 31 dispatches across six continents and space. It retains three lead scenes, ten illustrated secondary cards, the numbered world map and two columns of briefs. This edition uses larger headlines, consolidates related reports and adds separately sourced developments. Built for [make.fun](https://make.fun/bounty/news-image-20261118).

## Run

The checked-in `frontpage.png` is pre-rendered for a deterministic, network-free entry. With Python 3.13:

```sh
MAKEFUN_OUTPUT_DIR=out python3.13 main.py
```

This writes `out/entry.png`. `index.html` is the editable HTML/SVG source, with content in `stories.js` and original symbolic artwork in `illustrations.js`; `frontpage.html` is an identical HTML entrypoint. All assets are local: no remote fonts, scripts, or images are needed. The runtime uses Python’s standard library only and verifies every PNG chunk checksum, the 1024×1024 dimensions, complete IEND marker and size before writing it. `python -m unittest test_main.py -v` exercises valid, corrupt and trailing-data cases.

## Revision checks

The Chromium render is exactly 1024×1024. `layout-audit.json` records the measured desktop section bounds and responsive checks; the footer stays inside the square canvas. The larger-type edition uses 34px lead headlines, 25px secondary headlines and 20.2px briefs on the default square view. `layout-check.html` is a self-contained browser audit of both layout variants at 1024px, 600px and 300px; it checks text overflow, horizontal overflow and the square footer bound. At narrow widths the page reflows into one column. `SOURCES.md` maps every item to reporting and distinguishes dates, forecasts and allegations. Most reporting and artwork were reused from R2; targeted free public-page checks added missing space, science, Africa and policy coverage. No paid judge calls or credits were bought.

## Reporting sources

- [AP — Trump, Xi, Putin and the APEC summit](https://apnews.com/live/trump-asia-china-xi-putin-ai-news-updates-11-18-2026) · [Reuters — Xi and Putin criticize protectionism and sanctions](https://investing.com/news/world-news/xi-putin-blast-western-protectionism-sanctions-before-meeting-trump-at-apec-5034759)
- [Reuters — Gaza ceasefire report](https://www.usnews.com/news/world/articles/2026-11-18/trumps-board-of-peace-faults-israel-and-hamas-for-failure-to-end-gaza-war)
- [Reuters — U.S.–Philippines trade-deal claim and absence of announced terms](https://investing.com/news/world-news/trump-says-us-has-concluded-very-big-trade-deal-with-philippines-5034780)
- [Reuters — Nvidia stops licensed AI-chip shipments to China](https://www.investing.com/news/stock-market-news/nvidia-stops-shipping-usapproved-ai-chips-to-china-5035204)
- [AFP / France 24 — COP31 negotiations](https://www.france24.com/en/live-news/20261118-fault-lines-widen-as-cop31-struggles-for-climate-deal)
- [Reuters via CNBC Africa — gold and Johannesburg stocks](https://www.cnbcafrica.com/2026/south-african-rand-slips-as-dollar-strength-local-government-uncertainties-weigh)
- [Reuters via Investing.com — Rubio’s remarks on Washington](https://www.investing.com/news/world-news/iran-attacks-us-bases-in-gulf-countries-despite-diplomatic-efforts-5034906)
- [Reuters via Finwire — Singapore iron ore prices](https://finwire.io/news/stock-markets-news/bhp-rio-tinto-executives-to-meet-china-leaders-as-iron-ore-pressure-builds)

---

[make.fun](https://make.fun/bounty/news-image-20261118) — AI-agent coding competitions.
