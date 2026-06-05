from sqlalchemy.orm import Session

from backend.database.models import Channel


def get_top_health_channels(db: Session):

    channels = (
        db.query(Channel)
        .order_by(Channel.health_score.desc())
        .limit(10)
        .all()
    )

    return [
        {
            "channel_name": c.channel_name,
            "health_score": c.health_score
        }
        for c in channels
    ]


def get_top_growth_channels(db: Session):

    channels = (
        db.query(Channel)
        .order_by(Channel.growth_score.desc())
        .limit(10)
        .all()
    )

    return [
        {
            "channel_name": c.channel_name,
            "growth_score": c.growth_score
        }
        for c in channels
    ]


def get_channel_profile(
    db: Session,
    channel_name: str
):

    channel = (
        db.query(Channel)
        .filter(
            Channel.channel_name.ilike(channel_name)
        )
        .first()
    )

    if not channel:

        return {
            "error": "Channel not found"
        }

    return {
        "channel_name": channel.channel_name,
        "genre": channel.genre,
        "health_score": channel.health_score,
        "growth_score": channel.growth_score,
        "creator_segment": channel.creator_segment,
        "channel_age": channel.channel_age
    }