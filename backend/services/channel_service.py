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

def compare_channels(
    db,
    channel1: str,
    channel2: str
):
    c1 = (
        db.query(Channel)
        .filter(Channel.channel_name.ilike(channel1))
        .first()
    )

    c2 = (
        db.query(Channel)
        .filter(Channel.channel_name.ilike(channel2))
        .first()
    )

    if not c1:
        return {"error": f"{channel1} not found"}

    if not c2:
        return {"error": f"{channel2} not found"}

    return {
        "channel_1": c1.channel_name,
        "channel_2": c2.channel_name,

        "health_score_1": c1.health_score,
        "health_score_2": c2.health_score,

        "growth_score_1": c1.growth_score,
        "growth_score_2": c2.growth_score,

        "health_winner":
            c1.channel_name
            if c1.health_score > c2.health_score
            else c2.channel_name,

        "growth_winner":
            c1.channel_name
            if c1.growth_score > c2.growth_score
            else c2.channel_name
    }



from sqlalchemy import func


def get_genre_analysis(db):

    genres = (
        db.query(
            Channel.genre,
            func.count(Channel.id).label("total_channels"),
            func.avg(Channel.health_score).label("avg_health"),
            func.avg(Channel.growth_score).label("avg_growth")
        )
        .group_by(Channel.genre)
        .all()
    )

    return [
        {
            "genre": g.genre,
            "total_channels": g.total_channels,
            "avg_health_score": round(g.avg_health, 2),
            "avg_growth_score": round(g.avg_growth, 2)
        }
        for g in genres
    ]

def get_channel_data_for_ai(
    db,
    channel_name: str
):
    channel = (
        db.query(Channel)
        .filter(
            Channel.channel_name.ilike(
                channel_name
            )
        )
        .first()
    )

    if not channel:
        return None

    return {
        "channel_name": channel.channel_name,
        "genre": channel.genre,
        "health_score": channel.health_score,
        "growth_score": channel.growth_score,
        "creator_segment": channel.creator_segment,
        "channel_age": channel.channel_age
    }


def get_competitor_data(
    db,
    channel1,
    channel2
):
    c1 = (
        db.query(Channel)
        .filter(
            Channel.channel_name.ilike(channel1)
        )
        .first()
    )

    c2 = (
        db.query(Channel)
        .filter(
            Channel.channel_name.ilike(channel2)
        )
        .first()
    )

    if not c1 or not c2:
        return None

    return (
        {
            "channel_name": c1.channel_name,
            "genre": c1.genre,
            "health_score": c1.health_score,
            "growth_score": c1.growth_score,
            "creator_segment": c1.creator_segment
        },
        {
            "channel_name": c2.channel_name,
            "genre": c2.genre,
            "health_score": c2.health_score,
            "growth_score": c2.growth_score,
            "creator_segment": c2.creator_segment
        }
    )