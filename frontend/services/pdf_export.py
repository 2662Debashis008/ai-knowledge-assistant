from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os

EXPORT_DIR = "exports"

os.makedirs(
    EXPORT_DIR,
    exist_ok=True
)

def export_to_pdf(
        question,
        answer
):

    filename = f"{EXPORT_DIR}/answer.pdf"

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            f"<b>Question:</b> {question}",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            f"<b>Answer:</b> {answer}",
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename