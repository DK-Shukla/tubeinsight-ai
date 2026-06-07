from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Channel

from backend.services.ai_service import (
    generate_growth_strategy
)

router = APIRouter(
    prefix="/ai",
    tags=["AI Growth Strategy"]
)


@router.get("/growth-strategy/{channel_name}")
def growth_strategy(
    channel_name: str,
    db: Session = Depends(get_db)
):
    channel = (
        db.query(Channel)
        .filter(
            Channel.channel_name == channel_name
        )
        .first()
    )

    if not channel:
        return {
            "error": "Channel not found"
        }

    strategy = generate_growth_strategy(
        {
            "channel_name": channel.channel_name,
            "genre": channel.genre,
            "health_score": channel.health_score,
            "growth_score": channel.growth_score,
            "creator_segment": channel.creator_segment,
            "channel_age": channel.channel_age,
        }
    )

    return {
        "channel": channel_name,
        "strategy": strategy
    }