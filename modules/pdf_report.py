from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os


def generate_pdf(topic, transcript, score, overall, speech):

    os.makedirs("reports", exist_ok=True)

    pdf_path = "reports/VBCUA_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Voice-Based Concept Understanding Analyser</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Topic:</b> {topic}", styles["Normal"]))

    story.append(Paragraph(f"<b>Concept Similarity:</b> {score:.2f}%", styles["Normal"]))

    story.append(Paragraph(f"<b>Overall Score:</b> {overall:.2f}/100", styles["Normal"]))

    story.append(Paragraph(f"<b>Total Words:</b> {speech['word_count']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Filler Words:</b> {speech['fillers']}", styles["Normal"]))

    story.append(Paragraph(f"<b>Words Per Minute:</b> {speech['wpm']}", styles["Normal"]))

    story.append(Paragraph("<br/><b>Transcript</b>", styles["Heading2"]))

    story.append(Paragraph(transcript, styles["BodyText"]))

    doc.build(story)

    return pdf_path
