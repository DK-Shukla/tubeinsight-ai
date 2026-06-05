from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.services.channel_service import (
    get_top_health_channels,
    get_top_growth_channels,
    get_channel_profile
)

app = FastAPI(
    title="TubeInsight AI",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "TubeInsight AI API Running"
    }


@app.get("/top-health")
def top_health(
    db: Session = Depends(get_db)
):
    return get_top_health_channels(db)


@app.get("/top-growth")
def top_growth(
    db: Session = Depends(get_db)
):
    return get_top_growth_channels(db)


@app.get("/channel/{channel_name}")
def channel_profile(
    channel_name: str,
    db: Session = Depends(get_db)
):
    return get_channel_profile(
        db,
        channel_name
    )