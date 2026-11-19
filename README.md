# The World Desk · R5

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

The World Desk covers Wednesday 18 November 2026 in 31 reports: three lead scenes, ten illustrated secondary stories, and eighteen briefs. It spans six continents and includes Voyager 1’s milestone.

## Reproducible entry

```sh
MAKEFUN_OUTPUT_DIR=out python3.13 main.py
```

`main.py` checks the PNG framing, CRCs, fixed RGB header, and decompressed rows before atomically publishing the deterministic `frontpage.png` as `out/entry.png`. The image is 1024×1024 and under 1 MiB. The judging runtime uses only the Python standard library and requires no network.

Open `index.html` in Chromium with a 1024×1024 CSS viewport at device scale 1 to view the print composition. `stories.js` keeps the reporting in source-note order; `illustrations.js` and `icons.js` provide symbolic editorial art, not documentary images. The same page reflows at mobile widths.

## Editorial scope

R5 restores the complete [R3 reporting ledger](SOURCES.md), with R4’s color scenes and a new three-column brief section. Forecasts, official attributions, and unresolved claims remain qualified. Lead headlines anchor the 300×300 preview; use the native render to read the smaller reports.

Built for [make.fun](https://make.fun/bounty/news-image-20261118).
