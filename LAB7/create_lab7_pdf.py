
import os
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image,
    PageBreak, Table, TableStyle
)

OUTPUT = "AM070_JYOTHIKA_LAB7.pdf"
SCREENSHOT_DIR = "screenshots"

screenshots = [
    ("SS1 - Original Application", "01_original_application.png",
     "Execution of the original Bowling Alley Parser application using valid inputs."),
    ("SS2 - Hypothesis Failure Results", "02_hypothesis_failures.png",
     "Hypothesis discovered input validation bugs in all three functions."),
    ("SS3 - Fixed Application", "04_fixed_application.png",
     "Execution of the corrected application after implementing defensive input validation."),
    ("SS4 - Final Hypothesis Test Results", "03_final_hypothesis_tests.png",
     "All three Hypothesis tests passed after the application was fixed.")
]

for _, filename, _ in screenshots:
    if not os.path.exists(os.path.join(SCREENSHOT_DIR, filename)):
        raise FileNotFoundError(f"Missing screenshot: {filename}")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "LabTitle", parent=styles["Title"],
    fontSize=22, leading=28, alignment=TA_CENTER,
    textColor=colors.HexColor("#17365D"), spaceAfter=18
)

heading_style = ParagraphStyle(
    "SectionHeading", parent=styles["Heading2"],
    textColor=colors.HexColor("#17365D"),
    fontSize=15, leading=20, spaceAfter=12
)

body_style = ParagraphStyle(
    "BodyCustom", parent=styles["BodyText"],
    fontSize=10.5, leading=16, spaceAfter=9
)

caption_style = ParagraphStyle(
    "CaptionCustom", parent=styles["BodyText"],
    fontSize=10, leading=15, alignment=TA_CENTER,
    textColor=colors.HexColor("#444444")
)

story = []

# Cover and summary
story.append(Spacer(1, 0.6 * inch))
story.append(Paragraph("LAB 7", title_style))
story.append(Paragraph(
    "Fuzzing for Input Validation Bugs",
    ParagraphStyle("Subtitle", parent=styles["Heading2"],
                   alignment=TA_CENTER, fontSize=16)
))
story.append(Spacer(1, 0.35 * inch))

details = [
    ["Student Name", "Jyothika"],
    ["SRN", "AM070"],
    ["Project", "Bowling Alley Parser"],
    ["Testing Library", "Hypothesis"],
    ["Test Framework", "Pytest"]
]

table = Table(details, colWidths=[1.8 * inch, 3.8 * inch])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#DCE6F1")),
    ("TEXTCOLOR", (0, 0), (-1, -1), colors.HexColor("#222222")),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("PADDING", (0, 0), (-1, -1), 9),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
]))
story.append(table)
story.append(Spacer(1, 0.35 * inch))

story.append(Paragraph("Objective", heading_style))
story.append(Paragraph(
    "To explore fuzz testing as a security and quality assurance technique "
    "by identifying and fixing input validation bugs in a Python application "
    "using the Hypothesis fuzzing library.",
    body_style
))

story.append(Paragraph("Functions Tested", heading_style))
for item in [
    "format_player_name() - formats player names safely.",
    "parse_frame() - parses bowling frame notation.",
    "parse_scoreboard() - parses player names and scores."
]:
    story.append(Paragraph("• " + item, body_style))

story.append(Paragraph("Bugs Identified and Fixes", heading_style))
for item in [
    "format_player_name(): Added type validation to handle None and invalid input.",
    "parse_frame(): Added checks for input type, frame length, valid symbols and pin count.",
    "parse_scoreboard(): Added type validation and safe handling of malformed entries."
]:
    story.append(Paragraph("• " + item, body_style))

story.append(Paragraph("Final Testing Result", heading_style))
story.append(Paragraph(
    "<b>3 tests passed in 1.35 seconds.</b> All three Hypothesis tests "
    "passed after the application was corrected.",
    body_style
))

# Screenshot pages
for title, filename, description in screenshots:
    story.append(PageBreak())
    story.append(Paragraph(title, heading_style))
    story.append(Spacer(1, 0.15 * inch))

    image_path = os.path.join(SCREENSHOT_DIR, filename)
    img = Image(image_path)

    max_width = 7.1 * inch
    max_height = 8.4 * inch
    scale = min(max_width / img.imageWidth, max_height / img.imageHeight)

    img.drawWidth = img.imageWidth * scale
    img.drawHeight = img.imageHeight * scale

    story.append(img)
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(description, caption_style))

story.append(PageBreak())
story.append(Paragraph("Conclusion", heading_style))
story.append(Paragraph(
    "Hypothesis fuzz testing identified input validation bugs in all three "
    "functions of the Bowling Alley Parser. Defensive input validation and "
    "safe handling of malformed data were implemented. The application was "
    "successfully executed with valid inputs, and all three property-based "
    "tests passed after the fixes.",
    body_style
))

def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawCentredString(
        A4[0] / 2, 25,
        f"Lab 7 - Jyothika | Page {document.page}"
    )
    canvas.restoreState()

doc.build(story, onFirstPage=add_page_number,
          onLaterPages=add_page_number)

print(f"\nPDF created successfully: {OUTPUT}")
