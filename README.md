# benchmark-analytics
Analytics dashboard based on different benchmarks used by Frontier model providers

## The Benchmark Wars

Six charts and an article built from 197 official launch posts by 11 labs (Jun 2018 – Nov 2026). Scores are as self-reported by the labs.

| Path | Contents |
| --- | --- |
| `data/` | Source CSV and the two Excel workbooks |
| `charts/` | Chart scripts (`c0.py` cover, `c1.py`–`c6.py` charts) |
| `visuals/` | Rendered 2160×2700 PNGs and the 7-page `benchmark_wars_carousel.pdf` |
| `article/the-benchmark-wars.md` | Website article that embeds the charts |

### Rebuild the visuals

```bash
pip install -r requirements.txt
python charts/build_all.py
```

The charts use the [Inter](https://github.com/rsms/inter) and [Space Grotesk](https://github.com/floriankarsten/space-grotesk) fonts. Install them, or put the `.ttf` files in a `fonts/` folder at the repo root; otherwise Matplotlib falls back to its default font.
