from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.database.connection import SessionLocal
from backend.database.models import Channel

from backend.services.ai_service import (
    generate_channel_review,
    generate_growth_strategy
)

from backend.services.pdf_service import (
    generate_pdf_report
)

router = APIRouter(
    prefix="/report",
    tags=["PDF Reports"]
)


@router.get("/{channel_name}")
def export_report(channel_name: str):

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
            return {
                "error": "Channel not found"
            }

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

        strategy = generate_growth_strategy(
            channel_data
        )

        pdf_buffer = generate_pdf_report(
            channel_name,
            review,
            strategy
        )

        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={
                "Content-Disposition":
                f"attachment; filename={channel_name}_report.pdf"
            },
        )

    finally:
        db.close()