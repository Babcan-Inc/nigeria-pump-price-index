# Methodology

## Data Collection

### Depot Prices
- Primary source: public depot price tables (currently awajis.com)
- Collected daily via automated script
- Captures PMS, AGO, and LPG where available
- Includes depot name, state, price, and change when reported

### Pump Prices
- Lightweight voluntary submissions
- Initial focus: Lagos and Abuja only
- Fields: location, product, price, optional station name, timestamp

### Official Benchmarks
- NBS monthly Price Watch used for calibration and longer-term context

## Aggregation
- Daily files stored as dated CSVs
- Simple medians and coverage metrics calculated
- Transparent about sample size and limitations

## Principles
- Prefer reliability and low maintenance over perfect national coverage
- All data is public and versioned
- Clear separation between depot (wholesale) and pump (retail) prices