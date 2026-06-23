import pandas as pd

df = pd.read_csv("data/raw/fund_master.csv")

print("Columns:")
print(df.columns.tolist())

for col in df.columns:
    print(f"\n{col}")
    print(df[col].head())