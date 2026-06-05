import pandas as pd

from backend.database.connection import SessionLocal
from backend.database.models import Channel

# Load dataset
df = pd.read_csv(
    "datasets/final_creator_dataset.csv"
)

db = SessionLocal()

# Clear old records
db.query(Channel).delete()

for _, row in df.iterrows():

    channel = Channel(
        rank=int(row["Rank"]),
        channel_name=row["Channel_Name"],
        genre=row["Genre"],
        subscriber_count=float(row["Subscriber_Count"]),
        video_views=float(row["Video_Views"]),
        video_count=float(row["Video_Count"]),
        channel_age=float(row["Channel_Age"]),
        health_score=float(row["Health_Score"]),
        growth_score=float(row["Growth_Score"]),
        creator_segment=str(row["Creator_Segment"])
    )

    db.add(channel)

db.commit()

db.close()

print(f"{len(df)} channels imported successfully!")