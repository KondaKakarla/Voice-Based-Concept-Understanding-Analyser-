from fpdf import FPDF
import os


def generate_pdf(topic, transcript, speech, score, overall, feedback):

    os.makedirs("reports", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Voice Based Concept Understanding Report", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "", 12)

    pdf.cell(0, 10, f"Topic: {topic}", ln=True)
    pdf.cell(0, 10, f"Concept Score: {score:.2f}%", ln=True)
    pdf.cell(0, 10, f"Overall Score: {overall:.2f}/100", ln=True)

    pdf.ln(5)

    pdf.cell(0, 10, f"Words: {speech['word_count']}", ln=True)
    pdf.cell(0, 10, f"Fillers: {speech['fillers']}", ln=True)
    pdf.cell(0, 10, f"WPM: {speech['wpm']}", ln=True)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Transcript", ln=True)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 8, transcript)

    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Feedback", ln=True)

    pdf.set_font("Arial", "", 11)

    for item in feedback:
        pdf.multi_cell(0, 8, item)

    filename = "reports/report.pdf"

    pdf.output(filename)

    return filename
