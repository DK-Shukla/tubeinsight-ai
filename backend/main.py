from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.connection import SessionLocal
from backend.database.models import Channel

from backend.services.ai_service import (
    generate_channel_review,
    generate_competitor_review
)

from backend.services.youtube_service import (
    get_channel_data
)

from backend.services.scoring_service import (
    calculate_health_score,
    calculate_growth_score,
    calculate_creator_segment
)

from backend.routes.growth_strategy import (
    router as growth_router
)

from backend.routes.report import (
    router as report_router
)

app = FastAPI(
    title="TubeInsight AI"
)

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROUTERS
# =========================

app.include_router(growth_router)
app.include_router(report_router)

# =========================
# HOME
# =========================

@app.get("/")
def root():
    return {
        "message": "TubeInsight AI Backend Running"
    }

# =========================
# AI REVIEW
# =========================

@app.get("/ai-review/{channel_name}")
def ai_review(channel_name: str):

    db = SessionLocal()

    try:

        channel = (
            db.query(Channel)
            .filter(
                Channel.channel_name == channel_name
            )
            .first()
        )

        if not channel:

            youtube_data = get_channel_data(
                channel_name
            )

            if not youtube_data:
                return {
                    "error": "Channel not found on YouTube"
                }

            subscriber_count = float(
                youtube_data["statistics"].get(
                    "subscriberCount",
                    0
                )
            )

            video_views = float(
                youtube_data["statistics"].get(
                    "viewCount",
                    0
                )
            )

            video_count = float(
                youtube_data["statistics"].get(
                    "videoCount",
                    0
                )
            )

            health_score = calculate_health_score(
                subscriber_count,
                video_views,
                video_count
            )

            growth_score = calculate_growth_score(
                subscriber_count,
                video_views
            )

            creator_segment = calculate_creator_segment(
                subscriber_count
            )

            channel = Channel(
                channel_name=youtube_data["snippet"]["title"],
                genre="Unknown",
                subscriber_count=subscriber_count,
                video_views=video_views,
                video_count=video_count,
                channel_age=1,
                health_score=health_score,
                growth_score=growth_score,
                creator_segment=creator_segment
            )

            db.add(channel)
            db.commit()
            db.refresh(channel)

        channel_data = {
            "channel_name": channel.channel_name,
            "genre": channel.genre,
            "health_score": channel.health_score,
            "growth_score": channel.growth_score,
            "creator_segment": channel.creator_segment,
            "channel_age": channel.channel_age,
        }

        review = generate_channel_review(
            channel_data
        )

        return {
            "channel": channel.channel_name,
            "review": review
        }

    finally:
        db.close()

# =========================
# COMPETITOR ANALYSIS
# =========================

@app.get("/competitor-analysis/{channel1}/{channel2}")
def competitor_analysis(
    channel1: str,
    channel2: str
):

    db = SessionLocal()

    try:

        c1 = (
            db.query(Channel)
            .filter(
                Channel.channel_name == channel1
            )
            .first()
        )

        c2 = (
            db.query(Channel)
            .filter(
                Channel.channel_name == channel2
            )
            .first()
        )

        if not c1 or not c2:
            return {
                "error": "One or both channels not found"
            }

        result = generate_competitor_review(
            {
                "channel_name": c1.channel_name,
                "genre": c1.genre,
                "health_score": c1.health_score,
                "growth_score": c1.growth_score,
                "creator_segment": c1.creator_segment,
            },
            {
                "channel_name": c2.channel_name,
                "genre": c2.genre,
                "health_score": c2.health_score,
                "growth_score": c2.growth_score,
                "creator_segment": c2.creator_segment,
            }
        )

        return {
            "comparison": result
        }

    finally:
        db.close()

# =========================
# TOP HEALTH
# =========================

@app.get("/top-health")
def top_health():

    db = SessionLocal()

    try:

        channels = (
            db.query(Channel)
            .order_by(
                Channel.health_score.desc()
            )
            .limit(10)
            .all()
        )

        return [
            {
                "channel_name": c.channel_name,
                "health_score": c.health_score,
            }
            for c in channels
        ]

    finally:
        db.close()

# =========================
# TOP GROWTH
# =========================

@app.get("/top-growth")
def top_growth():

    db = SessionLocal()

    try:

        channels = (
            db.query(Channel)
            .order_by(
                Channel.growth_score.desc()
            )
            .limit(10)
            .all()
        )

        return [
            {
                "channel_name": c.channel_name,
                "growth_score": c.growth_score,
            }
            for c in channels
        ]

    finally:
        db.close()

# =========================
# GENRE ANALYSIS
# =========================

@app.get("/genre-analysis")
def genre_analysis():

    db = SessionLocal()

    try:

        channels = db.query(Channel).all()

        return {
            "total_channels": len(channels)
        }
    finally:
        db.close()