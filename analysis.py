"""
Sales Data Analysis
Beginner-friendly data analytics project using Pandas and Matplotlib.
Run: python analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).parent / "sales_data.csv"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    # 1. Load data
    df = pd.read_csv(DATA_FILE)
    print("\n=== SALES DATA ANALYSIS ===")
    print("\nFirst five rows:")
    print(df.head())

    # 2. Clean data
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")
    df = df.dropna(subset=["Date", "Region", "Product", "Quantity", "Unit_Price"])
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] >= 0)]
    df = df.drop_duplicates()
    df["Revenue"] = df["Quantity"] * df["Unit_Price"]
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    # 3. Key performance indicators (KPIs)
    total_revenue = df["Revenue"].sum()
    total_units = int(df["Quantity"].sum())
    total_orders = len(df)
    average_order_value = total_revenue / total_orders if total_orders else 0

    print("\n=== KEY METRICS ===")
    print(f"Total revenue:       Rs. {total_revenue:,.2f}")
    print(f"Units sold:          {total_units:,}")
    print(f"Sales records:       {total_orders:,}")
    print(f"Average record value: Rs. {average_order_value:,.2f}")

    # 4. Product and region analysis
    product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()

    print("\n=== REVENUE BY PRODUCT ===")
    print(product_revenue.to_string())
    print("\n=== REVENUE BY REGION ===")
    print(region_revenue.to_string())
    print("\n=== MONTHLY REVENUE ===")
    print(monthly_revenue.to_string())

    # 5. Save summary tables
    product_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "revenue_by_product.csv")
    region_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "revenue_by_region.csv")
    monthly_revenue.rename("Revenue").to_csv(OUTPUT_DIR / "monthly_revenue.csv")

    # 6. Create charts and save them
    plt.figure(figsize=(9, 5))
    product_revenue.sort_values().plot(kind="barh")
    plt.title("Revenue by Product")
    plt.xlabel("Revenue (Rs.)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_product.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    region_revenue.sort_values().plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_region.png", dpi=150)
    plt.close()

    plt.figure(figsize=(10, 5))
    monthly_revenue.plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue_trend.png", dpi=150)
    plt.close()

    # 7. Simple business insights
    best_product = product_revenue.idxmax()
    best_region = region_revenue.idxmax()
    best_month = monthly_revenue.idxmax()

    insights = [
        f"Highest-revenue product: {best_product} (Rs. {product_revenue.max():,.2f})",
        f"Highest-revenue region: {best_region} (Rs. {region_revenue.max():,.2f})",
        f"Highest-revenue month: {best_month} (Rs. {monthly_revenue.max():,.2f})",
    ]
    print("\n=== BUSINESS INSIGHTS ===")
    for insight in insights:
        print("- " + insight)

    with open(OUTPUT_DIR / "business_insights.txt", "w", encoding="utf-8") as file:
        file.write("BUSINESS INSIGHTS\n")
        file.write("\n".join("- " + insight for insight in insights))
        file.write("\n")

    print(f"\nDone! Charts and summary files are saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
