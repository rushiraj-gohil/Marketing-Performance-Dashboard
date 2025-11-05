import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# =========================
# CONFIGURATION
# =========================
platforms = ["Meta", "Google", "Amazon", "TikTok"]
campaigns = {
    "Meta": ["Summer_Sale", "Holiday_Promo", "Brand_Reach", "Flash_Deals", "Festival_Blast"],
    "Google": ["Search_Shoes", "Shopping_Campaign", "Retargeting", "App_Promo", "Black_Friday"],
    "Amazon": ["Prime_Deals", "Sponsored_Brands", "Lightning_Sale", "Back_to_School", "New_Arrivals"],
    "TikTok": ["GenZ_Drop", "TrendBoost", "Influencer_Promo", "Creator_Series", "Flash_Challenge"]
}

regions = ["North America", "Europe", "Asia-Pacific", "India"]
device_types = ["Mobile", "Desktop", "Tablet"]
audience_segments = ["New Customers", "Returning Customers", "High-Value Customers"]
campaign_objectives = ["Awareness", "Traffic", "Conversions", "Retention"]

start_date = datetime(2025, 6, 1)
days = 120
# =========================

data = []

for platform in platforms:
    for campaign in campaigns[platform]:
        for day in range(days):
            date = start_date + timedelta(days=day)

            # Random context attributes
            region = random.choice(regions)
            device = random.choice(device_types)
            segment = random.choice(audience_segments)
            objective = random.choice(campaign_objectives)

            # ========== Marketing metrics ==========
            impressions = random.randint(80_000, 300_000)
            reach = random.randint(int(impressions * 0.6), impressions)
            frequency = round(impressions / reach, 2)
            clicks = random.randint(1500, 9000)
            ctr = round(clicks / impressions * 100, 2)
            cpc = round(random.uniform(0.25, 1.5), 2)
            spend = round(clicks * cpc, 2)
            conversions = random.randint(100, 1200)
            conv_rate = round(conversions / clicks * 100, 2)
            cpm = round(spend / impressions * 1000, 2)

            # Engagements
            engagements = random.randint(1000, 12000)
            engagement_rate = round(engagements / impressions * 100, 2)
            cost_per_engagement = round(spend / engagements, 2)

            # ========== Financial metrics ==========
            avg_order_value = round(random.uniform(15, 50), 2)
            revenue = round(conversions * avg_order_value, 2)
            profit_margin = round(random.uniform(0.25, 0.55), 2)
            profit = round(revenue * profit_margin, 2)
            roas = round(revenue / spend, 2) if spend else 0
            cac = round(spend / conversions, 2) if conversions else 0
            roi = round((revenue - spend) / spend * 100, 2) if spend else 0
            revenue_per_dollar = round(revenue / spend, 2) if spend else 0

            # Append row
            data.append([
                platform, campaign, date.date(), region, device, segment, objective,
                impressions, reach, frequency, clicks, ctr, cpc, cpm, spend,
                engagements, engagement_rate, cost_per_engagement, conversions,
                conv_rate, avg_order_value, revenue, profit, profit_margin, roas,
                cac, roi, revenue_per_dollar
            ])

# ========== Create DataFrame ==========
df = pd.DataFrame(data, columns=[
    "Platform", "Campaign_Name", "Date", "Region", "Device_Type", "Audience_Segment", "Campaign_Objective",
    "Impressions", "Reach", "Frequency", "Clicks", "CTR(%)", "CPC($)", "CPM($)", "Spend($)",
    "Engagements", "Engagement_Rate(%)", "Cost_per_Engagement($)", "Conversions", "Conversion_Rate(%)",
    "Avg_Order_Value($)", "Revenue($)", "Profit($)", "Profit_Margin", "ROAS", "CAC($)", "ROI(%)", "Revenue_per_Dollar"
])

# ========== Save to CSV ==========
df.to_csv("marketing_performance_dashboard_full_v4.csv", index=False)

print("✅ Full marketing performance dataset generated successfully!")
print(f"Total Rows: {len(df)}")
print("File saved as: marketing_performance_dashboard_full.csv")
print(df.head(5))