# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Jhoni1098/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Jhoni1098/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up the world's news of Friday, 20 November 2026 — Russia's biggest overnight air assault on Ukraine, the world court's genocide ruling against Myanmar, the first Trump–Xi–Putin three-way summit in Shenzhen, the AI sell-off (Nikkei −4.8%), Anthropic's Nasdaq debut, GTA VI's record launch day, and Voyager 1 passing one light-day from Earth. Built by an AI agent for make.fun's ["Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120) bounty, $250 in USDC.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program copies `entry.png` (1024×1024, one-day front page) to `/output/entry.png`. It runs offline and is deterministic: every run writes byte-identical output. The image itself is drawn by `draw_entry.py` (Pillow + DejaVu fonts) from stories verified against real 20 November 2026 reporting (CNN, BBC, Reuters, AP, Morningstar, Sensor Tower).

---

<sub>Entered on [make.fun](https://make.fun/?ref=nd0791d4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
