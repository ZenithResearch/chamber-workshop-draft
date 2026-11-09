#!/usr/bin/env python3
"""Build a one-page, fillable classroom worksheet for Hub process planning.

uv run --with reportlab==5.1.0 python build_sop_worksheet.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/sop-worksheet.pdf"
NAVY, INK, GRAY, LINE = map(HexColor, ("#000080", "#202020", "#555555", "#929292"))
W, H = landscape(letter)


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), invariant=1)
    c.setTitle("SOP Worksheet | Workshop")
    c.setAuthor("Zenith")
    c.setSubject("A simple process worksheet with three connected steps, a result check, and a handoff.")

    def text(x, y, value, size=11, font="Times-Roman", color=INK):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, H-y, value)

    def line(x1, y1, x2, y2, color=LINE, width=0.7):
        c.setStrokeColor(color)
        c.setLineWidth(width)
        c.line(x1, H-y1, x2, H-y2)

    def field(name, label, x, y, w, h, maxlen=140, multiline=True):
        c.acroForm.textfield(
            name=name, tooltip=label, x=x, y=H-y-h, width=w, height=h,
            fontName="Helvetica", fontSize=11, textColor=INK, fillColor=white,
            borderColor=LINE, borderWidth=0.7, forceBorder=True,
            borderStyle="solid", value="", maxlen=maxlen,
            fieldFlags="multiline doNotScroll" if multiline else "doNotScroll",
        )

    def circle(x, y, number):
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.2)
        c.setFillColor(white)
        c.circle(x, H-y, 14, stroke=1, fill=1)
        c.setFillColor(NAVY)
        c.setFont("Times-Bold", 15)
        c.drawCentredString(x, H-y-5, str(number))

    def arrow(x1, x2, y):
        line(x1, y, x2, y, NAVY, 1.3)
        line(x2-6, y-4, x2, y, NAVY, 1.3)
        line(x2-6, y+4, x2, y, NAVY, 1.3)

    text(36, 28, "ZENITH", 11, "Times-Bold", NAVY)
    text(699, 28, "WORKSHOP", 10, color=GRAY)
    text(36, 61, "Make a task easy to repeat", 25, "Times-Bold", NAVY)
    text(36, 81, "Write a short set of instructions someone else could follow. This is your standard operating procedure (SOP).", 11)

    text(36, 108, "A task I do often:", 12, "Times-Bold")
    text(408, 108, "The result I want:", 12, "Times-Bold")
    field("process_title", "A task I do often", 36, 116, 348, 30, 65, False)
    field("process_result", "The result I want", 408, 116, 348, 30, 105)
    text(36, 168, "When do you start?", 12, "Times-Bold")
    text(153, 168, "For example: when a customer asks for a quote.", 11, color=GRAY)
    field("process_trigger", "When do you start this process?", 36, 176, 720, 27, 120, False)

    # The arrows show a simple handoff sequence. Facilitator guidance maps the
    # receiving step's needs to actual dependencies, in the opposite edge direction.
    for n, x, title in [(1, 36, "First"), (2, 288, "Next"), (3, 540, "Then")]:
        circle(x+14, 236, n)
        text(x+38, 241, title, 17, "Times-Bold", NAVY)
        if n < 3:
            arrow(x+123, x+236, 236)
        prefix = f"step_{n}_"
        text(x, 270, "Who does it?", 11, "Times-Bold")
        field(prefix+"who", f"Step {n}: who does it?", x, 278, 216, 25, 34, False)
        text(x, 322, "What do they do?", 11, "Times-Bold")
        field(prefix+"action", f"Step {n}: what do they do?", x, 330, 216, 48, 140)
        text(x, 397, "What do they need?", 11, "Times-Bold")
        field(prefix+"needs", f"Step {n}: information, tools, or help needed", x, 405, 216, 30, 65)
        text(x, 454, "What do they pass on?", 11, "Times-Bold")
        field(prefix+"result", f"Step {n}: what result do they pass on?", x, 462, 216, 30, 65)

    text(36, 518, "Check the result", 14, "Times-Bold", NAVY)
    text(288, 518, "If something goes wrong", 14, "Times-Bold", NAVY)
    text(540, 518, "Hand it over", 14, "Times-Bold", NAVY)
    text(36, 535, "How will you know it was done correctly?", 11)
    text(288, 535, "When should you stop and ask for help?", 11)
    text(540, 535, "Who checks it, and who gets the result?", 11)
    field("check", "How will you know the work was done correctly?", 36, 543, 216, 37, 90)
    field("help", "When should you stop and ask for help?", 288, 543, 216, 37, 90)
    field("handoff", "Who checks it, and who gets the result?", 540, 543, 216, 37, 90)

    text(36, 600, "Use short phrases. Leave unused steps blank. Type and save a copy, or print and write by hand.", 9, color=GRAY)
    text(716, 600, "1 page", 9, color=GRAY)
    c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
