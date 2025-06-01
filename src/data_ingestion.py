import pandas as pd
import os

# Create raw data directory path
data_path = os.path.join("data", "raw")
os.makedirs(data_path, exist_ok=True)

# Load dataset (replace with actual loading if needed)
train_data = pd.read_csv("data/raw/train.csv")
test_data = pd.read_csv("data/raw/test.csv")

# Save again to mimic ingestion (optional but useful for pipeline consistency)
train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)

print("Data ingestion complete.")
