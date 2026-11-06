#!/usr/bin/env python3
"""Check served workshop pages, local navigation and agenda return links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import runpy

ROOT = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = []
        self.links = []
        self.agenda_navs = 0
        self.scripts = 0
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.append(values["id"])
        if tag in {"a", "link"} and "href" in values:
            self.links.append((tag, values))
        if tag in {"img", "source", "iframe"} and "src" in values:
            self.links.append((tag, {**values, "href": values["src"]}))
        if tag == "nav" and "agenda-navigation" in values.get("class", "").split():
            self.agenda_navs += 1
        if tag == "script":
            self.scripts += 1


def scan():
    files = runpy.run_path(str(ROOT / "server.py"))["FILES"]
    routes = set(files)
    paths = {ROOT / filename for filename, _ in files.values()}
    errors = []
    for path in sorted(paths):
        if not path.is_file():
            errors.append(f"Missing served file: {path.relative_to(ROOT)}")
    pages = {
        path: Page(path.read_text())
        for path in sorted(paths)
        if path.is_file() and path.suffix == ".html"
    }
    link_count = 0
    for path, page in pages.items():
        name = str(path.relative_to(ROOT))
        if len(page.ids) != len(set(page.ids)):
            errors.append(f"{name}: duplicate IDs")
        if page.scripts:
            errors.append(f"{name}: browser JavaScript is not allowed")
        agenda_links = 0
        for tag, values in page.links:
            link_count += 1
            href = values["href"]
            url = urlsplit(href)
            if url.scheme or url.netloc:
                if tag == "a" and url.scheme in {"http", "https"}:
                    if values.get("target") != "_blank" or "noopener" not in values.get("rel", "").split():
                        errors.append(f"{name}: external link must preserve the workshop tab: {href}")
                elif url.scheme not in {"http", "https", "mailto", "tel"}:
                    errors.append(f"{name}: unsupported link scheme: {href}")
                continue
            if url.path.startswith("/"):
                target = (ROOT / unquote(url.path).lstrip("/")).resolve()
            else:
                target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target == ROOT:
                target = ROOT / "index.html"
            try:
                relative = target.relative_to(ROOT)
            except ValueError:
                errors.append(f"{name}: link escapes the site: {href}")
                continue
            if tag == "a" and target == ROOT / "index.html":
                agenda_links += 1
            if not target.is_file():
                errors.append(f"{name}: missing target: {href}")
                continue
            if "/" + relative.as_posix() not in routes:
                errors.append(f"{name}: target is not served: {href}")
            if url.fragment and (target not in pages or unquote(url.fragment) not in pages[target].ids):
                errors.append(f"{name}: missing anchor: {href}")
        if path != ROOT / "index.html":
            if agenda_links != 1:
                errors.append(f"{name}: expected one direct agenda link, found {agenda_links}")
            if page.agenda_navs != 1:
                errors.append(f"{name}: expected one shared agenda navigation bar")
    return pages, link_count, errors


if __name__ == "__main__":
    pages, link_count, errors = scan()
    if errors:
        for error in errors:
            print("FAIL:", error)
        raise SystemExit(1)
    print(f"PASS: {len(pages)} pages, {link_count} links and assets; all {len(pages) - 1} detail pages return directly to the agenda.")
