# Market Access Dashboard

Market access strategy KPI monitoring and payer landscape dashboard

## Features
- Data ingestion from CSV/Excel input files
- Automated analysis and KPI calculation
- Summary statistics and trend reporting
- Sample data generator for testing and development

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.main import MarketAccessDashboard

analyzer = MarketAccessDashboard()
df = analyzer.load_data("data/sample.csv")
result = analyzer.analyze(df)
print(result)
```

## Data Format

Expected CSV columns: `product, market, formulary_coverage_pct, reimbursed_pct, unrestricted_access_pct, time_to_access_days, period`

## Project Structure

```
market-access-dashboard/
├── src/
│   ├── main.py          # Core analysis logic
│   └── data_generator.py # Sample data generator
├── data/                # Data directory (gitignored for real data)
├── examples/            # Usage examples
├── requirements.txt
└── README.md
```

## License

MIT License — free to use, modify, and distribute.
