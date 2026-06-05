import pandas as pd

# Load segmented dataset
df = pd.read_csv("datasets/segmented_channels.csv")

print("\n===== CHANNEL COUNT BY GENRE =====")
print(df["Genre"].value_counts())

print("\n===== AVG HEALTH SCORE BY GENRE =====")
print(
    df.groupby("Genre")["Health_Score"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== AVG VIEWS BY GENRE =====")
print(
    df.groupby("Genre")["Video_Views"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== AVG SUBSCRIBERS BY GENRE =====")
print(
    df.groupby("Genre")["Subscriber_Count"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== TOP CHANNEL PER GENRE =====")

top_channels = (
    df.sort_values(
        "Health_Score",
        ascending=False
    )
    .groupby("Genre")
    .first()
)

print(
    top_channels[
        ["Channel_Name", "Health_Score"]
    ]
)