# Sales Data Analysis using Python

A beginner-friendly data analytics project that explores sample sales data using **Python, Pandas, and Matplotlib**. It calculates key metrics, cleans data, compares products and regions, and creates charts.

## Project objectives

- Load and inspect a CSV dataset.
- Clean missing, invalid, and duplicate records.
- Calculate revenue using `Quantity × Unit_Price`.
- Calculate key metrics: total revenue, units sold, number of sales records, and average record value.
- Compare revenue by product, region, and month.
- Save charts and summary tables for further analysis.

## Tools used

- Python
- Pandas
- Matplotlib
- CSV

## Folder structure

```text
sales-data-analysis/
├── analysis.py
├── sales_data.csv
├── requirements.txt
├── README.md
└── output/                 # created automatically when the script runs
    ├── revenue_by_product.png
    ├── revenue_by_region.png
    ├── monthly_revenue_trend.png
    ├── revenue_by_product.csv
    ├── revenue_by_region.csv
    ├── monthly_revenue.csv
    └── business_insights.txt
```

## How to run the project

### 1. Install Python

Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/). During installation on Windows, select **Add Python to PATH** if that option appears.

### 2. Open a terminal in this folder

Open the `sales-data-analysis` folder in VS Code, then choose **Terminal → New Terminal**.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If `python` is not recognized on Windows, try:

```bash
py -m pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python analysis.py
```

On Windows, you can also try `py analysis.py`.

The script prints the metrics and business insights in the terminal. It creates an `output` folder containing three charts, three summary CSV files, and a text file with insights.

## Questions explored

1. Which product generates the most revenue?
2. Which region generates the most revenue?
3. How does revenue change month by month?
4. What are total revenue and total units sold?

## Example business uses

A sales team could use this analysis to compare product performance, identify strong regions, and review monthly revenue trends. The included data is **sample data created for practice**, not real company data.

## Possible improvements

- Add profit and discount analysis.
- Build an interactive dashboard using Streamlit.
- Connect the dataset to SQL.
- Add more data and handle additional data-quality issues.
- Create a Power BI dashboard from the cleaned CSV files.

## Author

Created by Pranshu | MCA Student | Aspiring Data Analyst