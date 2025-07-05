import pandas as pd

# Load the data from CSV
df = pd.read_csv('finance.csv')

# Columns to clean and convert
financial_cols = ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow from Operating Activities']

# Clean commas and convert to float
for col in financial_cols:
    df[col] = df[col].str.replace(',', '').astype(float)

# Sort by Company and Year ascending
df = df.sort_values(by=['Company', 'Year'])

# Calculate YoY % change per company
for col in financial_cols:
    df[col + ' YoY % Change'] = df.groupby('Company')[col].pct_change() * 100

# Round to 2 decimal places
df = df.round(2)

# Example helper function to get latest metric value
def get_latest_value(company: str, metric: str) -> str:
    df_comp = df[df["Company"].str.lower() == company.lower()]
    if df_comp.empty or metric not in df_comp.columns:
        return None
    latest_year = df_comp["Year"].max()
    value = df_comp[df_comp["Year"] == latest_year][metric].values[0]
    return f"{value / 1e9:.2f} billion USD ({company}, {latest_year})"

# Helper function for YoY % change
def get_latest_yoy_change(company: str, metric: str) -> str:
    col_name = metric + ' YoY % Change'
    df_comp = df[df["Company"].str.lower() == company.lower()]
    if df_comp.empty or col_name not in df_comp.columns:
        return None
    latest_year = df_comp["Year"].max()
    yoy_change = df_comp[df_comp["Year"] == latest_year][col_name].values[0]
    if pd.isna(yoy_change):
        return "No previous year data available for YoY % change."
    direction = "increased" if yoy_change > 0 else "decreased"
    return f"{direction} by {abs(yoy_change):.2f}% ({company}, {latest_year})"
