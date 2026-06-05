import pandas as pd
from sklearn.cluster import KMeans

# Load cleaned dataset
df = pd.read_csv("datasets/cleaned_channels.csv")

# Features for clustering
features = [
    "Health_Score",
    "Channel_Age"
]

X = df[features]

# KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Creator_Segment"] = kmeans.fit_predict(X)

# Rename segments
segment_names = {
    0: "Growing Creator",
    1: "Elite Creator",
    2: "Stable Creator",
    3: "Emerging Creator"
}

df["Creator_Segment"] = (
    df["Creator_Segment"]
    .map(segment_names)
)

# Save
df.to_csv(
    "datasets/segmented_channels.csv",
    index=False
)

print(
    df["Creator_Segment"]
    .value_counts()
)