***

# E-Commerce Marketing Performance Dashboard

## Overview

This project implements an advanced Streamlit dashboard for e-commerce marketing analytics, designed to meet the reporting needs of both the CMO and CFO, as well as executive leadership. The dashboard features three dedicated views: Executive Summary, CMO Dashboard, and CFO Dashboard. Data is fully synthetic, simulating 120 days of multi-platform advertising across Meta, Google, Amazon, and TikTok.

***

## Features

###  Multi-Tab Design
- **Executive Summary**: Top/bottom campaign rankings, strategic insights, platform radar comparison.
- **CMO Dashboard**: Campaign, audience, device, and region breakdowns; funnel analysis, engagement/conversion trends.
- **CFO Dashboard**: Financial performance, unit economics, ROI, profit, budget and cost analysis by segment and platform.

###  Metrics & Visualizations
- More than 20 KPIs including Impressions, Reach, CTR, Conversions, ROAS, CAC, Revenue, Profit, ROI, Profit Margin.
- Filters for Platform, Region, Campaign Objective, Audience Segment, Device Type, and Date Range.
- Advanced Plotly visualizations: radar, funnel, heatmap, trend lines, pie, and bar charts.
- Period-over-period comparisons and weighted averages for core performance metrics.
- Error handling, professional layout, and custom CSS styling.

***

## Project Structure

```
├── data_gen_vf.py         # Synthetic data generator script
├── streamlit_app_vf.py    # Streamlit dashboard app (main entry point)
├── marketing_performance_dashboard_realistic_v5.csv   # Generated dataset
└── README.md              # This file
```

***

## Getting Started

### Prerequisites

- Python 3.8+
- Required libraries: `streamlit`, `pandas`, `numpy`, `plotly`, `matplotlib`

### Installation & Usage

```bash
# Install dependencies
pip install streamlit pandas numpy plotly

# Generate data
python data_gen_vf.py

# Launch dashboard
streamlit run streamlit_app_vf.py
```

***

## Data

- **Synthetic period:** June 1 - Sept 28, 2025 (120 days)
- **Breakdowns:** 4 platforms × 5 campaigns × 4 regions × 3 devices × 3 audience segments × 4 objectives
- **Metrics:** Impressions, Reach, Clicks, CTR, CPC, Spend, Conversions, Conversion Rate, ROAS, CAC, Revenue, Profit, Profit Margin, and more.

***

## Design Rationale

- **Three-tab layout**: separates executive, marketing, and finance perspectives for clarity.
- **Rich synthetic data**: enables realistic demo without data privacy risk.
- **Streamlit + Plotly**: chosen for customizability, wide data control, and interactive UX.
- **Advanced features**: includes responsive design, professional formatting, dynamic filters, and performance optimization via caching.

***
