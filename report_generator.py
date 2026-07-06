from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(
    filename,
    transcript,
    semantic_score,
    fluency_score,
    final_score,
    feedback
):

    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, 760, "VBCUA Evaluation Report")

    c.setFont("Helvetica", 12)

    c.drawString(50, 710, f"Transcript:")
    c.drawString(50, 690, transcript)

    c.drawString(50, 650, f"Semantic Score: {semantic_score}%")

    c.drawString(50, 630, f"Fluency Score: {fluency_score}%")

    c.drawString(50, 610, f"Final Score: {final_score}%")

    c.drawString(50, 590, f"Feedback: {feedback}")

    c.save()