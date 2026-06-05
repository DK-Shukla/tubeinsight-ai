import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_csv("datasets/segmented_channels.csv")

# Growth Features
growth_features = [
    "Subscriber_Count",
    "Video_Views",
    "Video_Count",
    "Channel_Age"
]

# Normalize
scaler = MinMaxScaler()

scaled = scaler.fit_transform(
    df[growth_features]
)

scaled_df = pd.DataFrame(
    scaled,
    columns=growth_features
)

# Growth Formula
df["Growth_Score"] = (
    scaled_df["Subscriber_Count"] * 0.40 +
    scaled_df["Video_Views"] * 0.30 +
    scaled_df["Video_Count"] * 0.20 +
    (1 - scaled_df["Channel_Age"]) * 0.10
) * 100

df["Growth_Score"] = (
    df["Growth_Score"]
    .round(2)
)

# Save
df.to_csv(
    "datasets/final_creator_dataset.csv",
    index=False
)

print(
    df[
        ["Channel_Name", "Growth_Score"]
    ]
    .sort_values(
        by="Growth_Score",
        ascending=False
    )
    .head(20)
)