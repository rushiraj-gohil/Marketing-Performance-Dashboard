# Marketing Performance Dashboard — Technical Documentation

## 1. Project Overview

This documentation describes the design, implementation, and business rationale of the Marketing Performance Dashboard, fulfilling the assignment requirements for delivering actionable insights to both the Chief Marketing Officer (CMO) and Chief Financial Officer (CFO) of an e-commerce organization[1].

## 2. Assignment Context

The dashboard serves:
- **CMO:** Needs actionable metrics for brand growth, audience engagement, and campaign optimization.
- **CFO:** Requires visibility on cost, revenue, profitability, and the financial efficiency of marketing investments.
- Data is generated synthetically to mimic real omnichannel ad performance across Meta, Google, Amazon, and TikTok[1][2].

## 3. Data Generation (`data_gen.py`)

- **Purpose:** Created due to lack of comprehensive public datasets.
- **Scope:** 120 days, 4 platforms, 5 campaigns/platform, 4 regions, 3 audience segments, 3 devices, 4 objectives.
- **KPIs:** Includes all marketing and financial measures needed for realistic business analysis.

## 4. Dashboard Structure and KPI Logic (`dashboard.py`)

The dashboard is built in Streamlit. It uses a dual-tab (or stakeholder-driven) UI with shared interactive filters.

### Filters

Both stakeholder views support filters for:
- **Platform**
- **Region**
- **Campaign Objective**
- **Audience Segment**
- **Date Range**

*Rationale:* Filters allow both CMO and CFO to drill into specific business contexts—channel, market, audience, and time—to drive precise, tailored decisions[3].

### CMO Dashboard

#### KPIs:
- **Total Impressions:** Measures ad visibility, critical for assessing campaign reach and brand awareness.
- **Total Reach:** Tracks audience size exposed to ads, foundational for market penetration.
- **Average CTR (Click-Through Rate):** Shows creative and targeting effectiveness, guiding improvements for engagement.
- **Average Conversion Rate:** Captures marketing funnel strength from click to transaction.
- **Average ROAS (Return on Ad Spend):** Links spend to direct revenue, supporting budget allocation.
- **Average Engagement Rate:** Reflects the quality of audience interaction, guiding content and experience refinement.

#### Visual Breakdowns:
- **CTR & Conversion Rate Over Time:** Tracks momentum, pinpointing trends and shifts.
- **Spend vs. Conversions per Platform:** Reveals channel effectiveness, highlighting where investment generates results.
- **Regional Reach Analysis:** Informs geo-targeting and expansion strategies.
- **Device Spend Share:** Supports device-level ad formatting and budget allocation.
- **Campaign Table Breakdown:** Permits granular competitive analysis at the campaign level.

*Why these KPIs?*  
Each metric targets a specific step in understanding or optimizing the marketing funnel, aiming for actionable insight into creative, targeting, conversion, and overall audience impact—all vital for a growth-focused marketing leader[3].

### CFO Dashboard

#### KPIs:
- **Total Spend:** Absolute view of costs to manage budget and spending discipline.
- **Total Revenue:** Core outcome for marketing investment, showing return.
- **Total Profit:** Net financial outcome, integrating both spend and revenue.
- **Average ROI (Return on Investment):** Evaluates effectiveness, guiding future allocation.
- **Average CAC (Customer Acquisition Cost):** Measures cost-efficiency per new customer.
- **Average Profit Margin:** Tracks operational and marketing profitability.

#### Analytical Breakdowns:
- **Spend vs. Revenue Over Time:** Highlights whether increased spend results in increased revenue.
- **Profit & ROI by Platform:** Ranks channels by financial value—not just volume.
- **ROI by Region:** Drives geographically-targeted financial decisions.
- **Platform Financial Summary Table:** Provides comparative decision power on multiple financial KPIs.

*Why these KPIs?*  
Chosen to allow the CFO to monitor budgets, revenue, efficiency, and profitability; every metric addresses a key lever for financial optimization in marketing spend[3].

## 5. Business Rationale for KPI/Filter Selection

- All KPIs align with either marketing growth (CMO) or financial efficiency (CFO), following standard industry practices for performance marketing.
- Filters enable precise, actionable analysis—making insights relevant and contextual per stakeholder needs.
- Using Streamlit allows rapid development, flexibility, and deployment directly to the cloud, meeting assignment criteria for a working demo.

## 6. Key Technical Notes

- Data generated to ensure coverage of all assignment requirements.
- Streamlit used for speed and code-driven flexibility versus traditional BI tools.
- Individual stakeholder views are implemented within a single application, leveraging dynamic filtering for focused experiences.

## 7. Limitations and Opportunities

- Synthetic data is not reflective of an actual brand's numbers; real API integrations could be added.
- Future work could include drill-down analytics, scheduled reports, user role-based access, mobile optimization, and advanced alerts.

## 8. Getting Started

- Install Python (>=3.8) and required packages.
- Run `data_gen.py` to create the CSV dataset.
- Launch using `streamlit run dashboard.py`.
