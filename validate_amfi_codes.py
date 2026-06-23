import pandas as pd

fund_master = pd.read_csv("data/raw/fund_master.csv")
nav_history = pd.read_csv("data/raw/nav_history.csv")

# Normalize column names
fund_master.columns = fund_master.columns.str.strip().str.lower()
nav_history.columns = nav_history.columns.str.strip().str.lower()

print("Fund Master Columns:")
print(fund_master.columns.tolist())

print("\nNAV History Columns:")
print(nav_history.columns.tolist())