#!/usr/bin/env python3
"""Build the Hub-based SOP worksheet. No PDF dependency is needed to serve it.

uv run --with reportlab==5.1.0 python build_sop_worksheet.py
"""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output/pdf/sop-worksheet.pdf"
NAVY, INK, GRAY, LINE = map(HexColor, ("#000080", "#202020", "#555555", "#999999"))
W, H = letter


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUTPUT), pagesize=letter, invariant=1)
    c.setTitle("SOP Worksheet | Victoria Chamber Workshop")
    c.setAuthor("Zenith")
    c.setSubject("A plain-language planning worksheet based on the Hub Markdown process contract.")

    def text(x, y, value, size=11, font="Times-Roman", color=INK):
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(x, H-y, value)

    def para(x, y, value, width=504, size=11, leading=14):
        for line in simpleSplit(value, "Times-Roman", size, width):
            text(x, y, line, size)
            y += leading

    def field(name, label, x, y, w, h, multiline=True, maxlen=400, border=True):
        c.acroForm.textfield(
            name=name, tooltip=label, x=x, y=H-y-h, width=w, height=h,
            fontName="Helvetica", fontSize=10, textColor=INK, fillColor=white,
            borderColor=LINE, borderWidth=0.65 if border else 0,
            forceBorder=border, borderStyle="solid", value="", maxlen=maxlen,
            fieldFlags="multiline doNotScroll" if multiline else "doNotScroll",
        )

    def header(kicker, title, subtitle):
        text(48, 38, "ZENITH", 12, "Times-Bold", NAVY)
        text(353, 38, "VICTORIA CHAMBER WORKSHOP", 9, color=GRAY)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.6)
        c.line(48, H-49, 564, H-49)
        text(48, 71, kicker, 9, color=GRAY)
        text(48, 101, title, 25, "Times-Bold", NAVY)
        para(48, 123, subtitle, width=516)

    def footer(n):
        c.setStrokeColor(LINE)
        c.line(48, 49, 564, 49)
        text(48, 760, "SOP worksheet  /  Hub process format", 9, color=GRAY)
        text(291, 760, "Hub schema reference", 9, color=NAVY)
        c.linkURL("https://github.com/ZenithResearch/hub/blob/17796093f6bbf766d0a642709d553ae121eb7181/base/ops/processes/index.md", (291, 27, 385, 40), relative=0)
        text(523, 760, f"{n} of 4", 9, color=GRAY)

    header("01  /  DEFINE THE PROCESS", "Standard operating procedure",
           "Describe one recurring task so another person can follow it. Use brief, specific answers.")
    text(48, 161, "Process name", 12, "Times-Bold")
    field("process_title", "Process title: name the recurring task", 48, 171, 516, 28, False, 80)
    text(48, 222, "What does this process do?", 12, "Times-Bold")
    text(48, 239, "State when it is used and the result it should produce.", 10)
    field("process_description", "What this process does", 48, 250, 516, 59, maxlen=330)
    text(48, 335, "Information used or created", 15, "Times-Bold", NAVY)
    para(48, 353, "Give each item one short name and use that same name in the steps. Include every input and output. Record systems, workspace access, and tools on the step pages instead.", width=516)
    text(48, 391, "Types: text, number, yes/no, list, or a record with several details.", 10, color=GRAY)
    xs = [48, 158, 235, 444, 564]
    for x, a, b in [(48, "Item name", "e.g., request_details"), (158, "Type", "e.g., text"), (235, "Meaning", "What does this item contain?"), (444, "Source", "At start, or step no.")]:
        text(x+6, 416, a, 10, "Times-Bold")
        text(x+6, 430, b, 9)
    for row in range(6):
        top=440+row*39
        for col, (key, label, limit) in enumerate([
            ("name", "Variable name", 44), ("type", "Variable type", 32),
            ("description", "Variable description", 105), ("source", "Available at start or produced by which step", 40),
        ]):
            field(f"variable_{row+1}_{key}", f"Information item {row+1}: {label}", xs[col]+3, top+3,
                  xs[col+1]-xs[col]-6, 33, maxlen=limit, border=False)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.65)
    for x in xs:
        c.line(x, H-402, x, H-674)
    for top in [402, 440, 479, 518, 557, 596, 635, 674]:
        c.line(48, H-top, 564, H-top)
    text(48, 696, "Use the next three pages for steps. Add sheets if needed; keep names and numbers unique.", 10)
    text(48, 713, "Type in the boxes and save a copy, or print and write by hand.", 10, color=GRAY)
    footer(1)
    c.showPage()

    for step in range(1, 4):
        header(f"0{step+1}  /  DESCRIBE THE WORK", f"Step {step}",
               "Describe one clear action. Use the information names from the first page.")
        prefix=f"step_{step}_"
        text(48, 154, "Step name", 12, "Times-Bold")
        field(prefix+"title", f"Step {step}: title", 48, 164, 516, 25, False, 80)

        text(48, 211, "Who does the work?", 12, "Times-Bold")
        text(48, 227, "Person or role assigned to this step.", 10)
        field(prefix+"assignee", f"Step {step}: Assignee", 48, 237, 245, 31, maxlen=90)
        text(309, 211, "Skill needed", 12, "Times-Bold")
        text(309, 227, "Name the skill, or describe the ability needed.", 10)
        field(prefix+"skills", f"Step {step}: Skills", 309, 237, 255, 31, maxlen=100)

        text(48, 291, "Inputs", 12, "Times-Bold")
        text(48, 307, "Which named information items must be ready before this step begins?", 10)
        field(prefix+"inputs", f"Step {step}: Input variable names", 48, 317, 516, 35, maxlen=210)

        text(48, 375, "What happens in this step?", 12, "Times-Bold")
        text(48, 391, "Include decisions, checks, approvals, and what to do if something is missing or goes wrong.", 10)
        field(prefix+"processing", f"Step {step}: Processing instructions", 48, 401, 516, 83, maxlen=620)

        text(48, 507, "Outputs", 12, "Times-Bold")
        text(48, 523, "Name each new information item this step produces and what it contains, or write none.", 10)
        field(prefix+"outputs", f"Step {step}: Output (process state), variable names and values", 48, 533, 516, 35, maxlen=210)

        text(48, 591, "Required resources", 12, "Times-Bold")
        text(48, 607, "Systems or workspaces this step needs access to.", 10)
        field(prefix+"required_resources", f"Step {step}: Required Resources", 48, 617, 245, 32, maxlen=110)
        text(309, 591, "Suggested resources", 12, "Times-Bold")
        text(309, 607, "Helpful, but the step can run without them.", 10)
        field(prefix+"suggested_resources", f"Step {step}: Suggested Resources (optional)", 309, 617, 255, 32, maxlen=110)

        text(48, 672, "Hub setup, if known: use registered names. Otherwise leave these for the facilitator.", 9, color=GRAY)
        for x, key, label in [(48, "executor", "Executor (runs the step)"), (223, "tools", "Tools (registered actions)"), (398, "toolsets", "Toolsets (tool groups)")]:
            text(x, 689, label, 10)
            field(prefix+key, f"Step {step}: {key.title()} (optional Hub setup)", x, 698, 166, 23, False, 28)
        footer(step+1)
        c.showPage()
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
