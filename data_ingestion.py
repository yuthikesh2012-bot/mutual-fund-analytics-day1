import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

for file in csv_files:
    print(f"\nDataset: {file}")
    try:
        df = pd.read_csv(os.path.join(DATA_PATH, file))
        print("Shape:", df.shape)
        print(df.dtypes)
        print(df.head())
        print("Missing Values:", df.isnull().sum().sum())
    except Exception as e:
        print(f"Error reading {file}: {e}")
