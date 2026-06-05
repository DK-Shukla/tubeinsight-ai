import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("datasets/top-300-youtube-channels.csv")

# Remove useless column
df.drop(columns=["Unnamed: 0"], inplace=True)

# ------------------------
# Feature 1: Channel Age
# ------------------------
CURRENT_YEAR = 2026

df["Channel_Age"] = CURRENT_YEAR - df["Channel_Started"]

# ------------------------
# Feature 2: Avg Views Per Video
# ------------------------
df["Avg_Views_Per_Video"] = (
    df["Video_Views"] / df["Video_Count"]
)

# ------------------------
# Feature 3: Upload Consistency
# ------------------------
df["Upload_Consistency"] = (
    df["Video_Count"] / df["Channel_Age"]
)

# ------------------------
# Feature 4: Normalize Metrics
# ------------------------
scaler = MinMaxScaler()

metrics = [
    "Subscriber_Count",
    "Video_Views",
    "Avg_Views_Per_Video",
    "Upload_Consistency"
]

df[metrics] = scaler.fit_transform(df[metrics])

# ------------------------
# Feature 5: Creator Health Score
# ------------------------
df["Health_Score"] = (
    df["Subscriber_Count"] * 0.35 +
    df["Video_Views"] * 0.30 +
    df["Avg_Views_Per_Video"] * 0.20 +
    df["Upload_Consistency"] * 0.15
)

df["Health_Score"] = (
    df["Health_Score"] * 100
).round(2)

# Save cleaned dataset
df.to_csv(
    "datasets/cleaned_channels.csv",
    index=False
)

print("\nDataset saved successfully!")
print(df.head())

print("\nTop 10 Channels by Health Score:")
print(
    df[
        ["Channel_Name", "Health_Score"]
    ]
    .sort_values(
        by="Health_Score",
        ascending=False
    )
    .head(10)
)