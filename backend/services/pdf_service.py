from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_pdf_report(
    channel_name,
    review,
    strategy
):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"TubeInsight AI Report - {channel_name}",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "AI Review",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            review,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Growth Strategy",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            strategy,
            styles["BodyText"]
        )
    )

    doc.build(content)

    buffer.seek(0)

    return buffer