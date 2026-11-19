# The World Desk · R4

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/fenel-git/world-desk-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

The World Desk is a focused 11-story visual edition for Wednesday 18 November 2026. It uses three lead scenes and eight secondary cards across Asia, North America, Europe, Africa, Oceania, and South America.

## Reproducible entry

```sh
MAKEFUN_OUTPUT_DIR=out python3.13 main.py
```

`main.py` validates every PNG chunk, checksum, dimension, color depth, consecutive IDAT sequence, and IEND boundary before copying the deterministic `frontpage.png` to `out/entry.png`. The image is 1024×1024 and under 1 MiB. All artwork and copy are local; the sandbox requires no network.

`index.html` is the editable HTML/SVG source. `stories.js` holds only the selected stories and their concise, attribution-preserving decks. `illustrations.js` contains symbolic vector artwork; it is not documentary photography.

## Editorial scope

This revision removes the dense brief strip and keeps the most consequential verified items from the audited `SOURCES.md`. Forecasts, official attributions, and unresolved claims remain explicitly qualified. The image is designed for a 300×300 thumbnail as well as its native 1024×1024 render.

Built for [make.fun](https://make.fun/bounty/news-image-20261118).
