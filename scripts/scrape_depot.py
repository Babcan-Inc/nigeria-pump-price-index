#!/usr/bin/env python3
"""
Scrape daily depot (gantry) fuel prices from awajis.com
and save as a dated CSV in data/depot/.

This is intentionally simple and low-maintenance.
"""

import csv
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

URL = "https://awajis.com/fuel-price-in-nigeria-today/"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "depot"


def clean_price(text: str) -> float | None:
    """Convert price strings like '1,135.00' or '1,135' to float."""
    if not text:
        return None
    cleaned = re.sub(r"[^\d.]", "", text.replace(",", ""))
    try:
        return float(cleaned)
    except ValueError:
        return None


def extract_tables(soup: BeautifulSoup):
    """Extract depot price tables for PMS, AGO, LPG."""
    results = []

    # Look for tables that follow headings containing product names
    for heading in soup.find_all(["h2", "h3", "h4"]):
        heading_text = heading.get_text(strip=True).lower()

        product = None
        if "petrol" in heading_text or "pms" in heading_text:
            product = "PMS"
        elif "diesel" in heading_text or "ago" in heading_text:
            product = "AGO"
        elif "cooking gas" in heading_text or "lpg" in heading_text:
            product = "LPG"

        if not product:
            continue

        # Find the next table after this heading
        table = heading.find_next("table")
        if not table:
            continue

        rows = table.find_all("tr")
        if len(rows) < 2:
            continue

        # Skip header row
        for row in rows[1:]:
            cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
            if len(cols) < 3:
                continue

            depot = cols[0]
            state = cols[1]
            price = clean_price(cols[2])
            change = cols[3] if len(cols) > 3 else ""

            if price is None:
                continue

            results.append({
                "product": product,
                "depot": depot,
                "state": state,
                "price_ngn": price,
                "change": change,
            })

    return results


def main():
    print(f"Fetching {URL} ...")
    headers = {
        "User-Agent": "NigeriaPumpPriceIndex/0.1 (public research data project)"
    }
    resp = requests.get(URL, headers=headers, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    records = extract_tables(soup)

    if not records:
        print("WARNING: No depot price rows extracted. Page structure may have changed.")
        return

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"depot_{today}.csv"

    fieldnames = ["date", "product", "depot", "state", "price_ngn", "change", "source"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow({
                "date": today,
                "product": r["product"],
                "depot": r["depot"],
                "state": r["state"],
                "price_ngn": r["price_ngn"],
                "change": r["change"],
                "source": "awajis.com",
            })

    print(f"Saved {len(records)} rows to {out_path}")


if __name__ == "__main__":
    main()
