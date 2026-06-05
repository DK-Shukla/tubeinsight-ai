import pandas as pd

print("Loading dataset...")

df = pd.read_csv("datasets/top-300-youtube-channels.csv")

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== FIRST 5 ROWS =====")
print(df.head())