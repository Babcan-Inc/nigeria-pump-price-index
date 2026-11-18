# Nigeria Pump Price Index

Open, low-maintenance daily fuel price data for Nigeria — focused on research, analysis, and policy use.

## What this project is

A lightweight, largely automated system that collects and publishes:

- **Depot / gantry prices** (automated daily collection)
- **Actual pump prices**, starting with Lagos and Abuja (lightweight crowdsourcing)

The goal is to produce clean, usable, day-over-day data that is currently missing or too fragmented from official sources (NBS monthly surveys and NMDPRA factsheets).

This is a **public-good / research project**. It is not a commercial product, consumer app, or real-time station finder.

## Why it exists

Official fuel price data in Nigeria is either:
- Monthly and lagged (NBS Price Watch), or
- Fragmented and hard to use for continuous analysis

There is a clear gap for consistent, higher-frequency, transparent data that researchers, analysts, journalists, and policy people can rely on.

## Scope (intentionally limited)

**In scope**
- Automated collection of depot prices
- Simple crowdsourced pump price reports focused on Lagos + Abuja first
- Clean daily/periodic CSVs and simple summaries
- Transparent methodology
- Open data (public GitHub + downloadable files)

**Out of scope (for now)**
- Full national real-time station-level coverage
- Consumer-facing mobile app or map
- Paid incentives for reporters
- Complex forecasting or commercial features

We prioritise **reliability and low maintenance** over breadth.

## Data sources

1. **Depot prices** — primarily automated from public sources (e.g. awajis.com and similar)
2. **Pump prices** — voluntary submissions, starting with Lagos and Abuja
3. **Official benchmarks** — NBS monthly Price Watch for calibration and historical context

## How the automation works (high level)

- Daily GitHub Action scrapes/collects depot prices
- Crowdsourced submissions flow into a simple form → sheet → repo
- Aggregation scripts produce clean daily files
- Data is versioned in this repository and made publicly available

## Status

Early stage. Structure and first automated depot pipeline being set up.

## Contributing data

If you are in Lagos or Abuja and want to contribute occasional pump price observations, a simple form will be linked here once ready.

## License & use

Data is intended for open research and policy use. Full license and methodology details will be added as the project matures.

---

Maintained as a low-effort public research project.