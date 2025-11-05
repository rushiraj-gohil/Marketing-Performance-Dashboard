***

# Marketing Performance Dashboard for E-Commerce

## Project Overview

This project delivers a dual-perspective marketing performance dashboard designed to serve both the Chief Marketing Officer (CMO) and Chief Financial Officer (CFO) of an e-commerce organization. The dashboard provides real-time, stakeholder-relevant insights into advertising performance across Meta, Google, Amazon, and TikTok platforms.

## Dashboard Features

### Dual-Tab Architecture
- **CMO Dashboard:** Campaign performance, audience reach, engagement, conversion metrics.
- **CFO Dashboard:** Financial efficiency, ROI, profitability, and cost control.

### CMO Metrics
- Total Impressions & Reach
- Click-Through Rate (CTR)
- Conversion Rate
- ROAS (Return on Ad Spend)
- Engagement Rate
- Regional, Device, and Campaign-level breakdowns

### CFO Metrics
- Total Spend & Revenue
- Profit & Profit Margin
- ROI (Return on Investment)
- CAC (Customer Acquisition Cost)
- Platform & Region ROI Analysis
- Spend vs Revenue Trends

### Interactive Filters
- Platform, Region, Campaign Objective, Audience Segment, Date Range

## Technology Stack

| Component         | Technology     |
|-------------------|---------------|
| Framework         | Streamlit      |
| Data Processing   | pandas, numpy  |
| Data Generation   | Python         |
| Deployment        | Streamlit Cloud|
| Data Storage      | CSV            |

## Project Structure

```
├── data_gen.py            # Synthetic data generator
├── dashboard.py           # Main Streamlit dashboard code
└── README.md              # This file
```

## Getting Started

### Prerequisites
- Python 3.8+
- Libraries: `streamlit`, `pandas`, `numpy`, `plotly`, `random`, `datetime`

### Installation

```bash
pip install streamlit pandas numpy
python data_gen.py                # Generate dataset
streamlit run dashboard.py        # Launch dashboard
```

### Deployment on Streamlit Cloud

1. Push project files to GitHub.
2. Create an app at Streamlit Cloud, select `dashboard.py` as entry point.
3. Add `requirements.txt` as needed.

## Dataset Details

- 120 days of synthetic data (June–Sept 2025)
- 4 Platforms × 5 campaigns each × 4 regions × 3 devices × 3 audience segments
- KPIs cover impressions, clicks, spend, conversions, revenue, profit, ROI, CAC, etc.

## Design Decisions

- **Synthetic data** ensures all required metrics for realistic demo.
- **Streamlit** chosen over traditional BI tools for speed and flexible code-based customization.
- **Dual-tab** layout allows tailored insights for both stakeholder roles without duplicating effort or losing context.

