#!/usr/bin/env python3
"""Render the two site guides using their small Markdown authoring subset."""
from html import escape
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
INLINE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|\x60([^\x60]+)\x60")


def inline(text):
    parts = []
    position = 0
    for match in INLINE.finditer(text):
        parts.append(escape(text[position:match.start()]))
        label, href, bold, code = match.groups()
        if href is not None:
            external = urlsplit(href).scheme in {"http", "https"}
            attrs = ' target="_blank" rel="noopener noreferrer" title="Opens in a new tab"' if external else ""
            parts.append(f'<a href="{escape(href, quote=True)}"{attrs}>{escape(label)}</a>')
        elif bold is not None:
            parts.append(f"<b>{escape(bold)}</b>")
        else:
            parts.append(f"<code>{escape(code)}</code>")
        position = match.end()
    parts.append(escape(text[position:]))
    return "".join(parts)


def render(source):
    parts = []
    paragraph = []
    in_list = False
    in_section = False
    code = []

    def flush_paragraph():
        if paragraph:
            parts.append("<p>" + inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    def flush_code():
        if code:
            parts.append("<pre><code>" + escape("\n".join(code)) + "</code></pre>")
            code.clear()

    for line in (ROOT / source).read_text().splitlines() + [""]:
        if line.startswith("    "):
            flush_paragraph()
            if in_list:
                parts.append("</ul>")
                in_list = False
            code.append(line[4:])
            continue
        flush_code()
        if line.startswith("- "):
            flush_paragraph()
            if not in_list:
                parts.append("<ul>")
                in_list = True
            parts.append("<li>" + inline(line[2:]) + "</li>")
            continue
        if in_list:
            parts.append("</ul>")
            in_list = False
        if line.startswith("# "):
            flush_paragraph()
            parts.append('<header><p class="wordmark">ZENITH</p><h1>' + escape(line[2:]) + "</h1></header>")
        elif line.startswith("## "):
            flush_paragraph()
            if in_section:
                parts.append("</section>")
            parts.append("<section><h2>" + escape(line[3:]) + "</h2>")
            in_section = True
        elif not line.strip():
            flush_paragraph()
        else:
            paragraph.append(line)
    if in_section:
        parts.append("</section>")
    title = escape(source + " — Workshop guide")
    return (
        '<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<title>{title}</title><link rel="stylesheet" href="styles.css"></head>\n'
        '<body class="document guide-page"><main>\n'
        '<nav class="agenda-navigation" aria-label="Workshop navigation"><a href="index.html#agenda">Back to agenda</a></nav>\n'
        + "\n".join(parts)
        + f'\n<p><a href="{source}">Plain-text {source}</a></p>\n</main></body></html>\n'
    )


def main():
    for source, target in (("README.md", "readme.html"), ("AGENTS.md", "agents.html")):
        (ROOT / target).write_text(render(source))
    print("Rendered README.md and AGENTS.md guides.")


if __name__ == "__main__":
    main()
