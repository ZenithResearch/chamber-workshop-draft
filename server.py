#!/usr/bin/env python3
"""Serve only the fresh workshop draft on a selected local interface."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
FILES = {
    '/': ('index.html', 'text/html; charset=utf-8'),
    '/index.html': ('index.html', 'text/html; charset=utf-8'),
    '/resources.html': ('resources.html', 'text/html; charset=utf-8'),
    '/styles.css': ('styles.css', 'text/css; charset=utf-8'),
}

for activity in range(1, 7):
    for folder in ('plans', 'slides', 'notes'):
        filename = f'{folder}/activity-{activity:02d}.html'
        FILES[f'/{filename}'] = (filename, 'text/html; charset=utf-8')


for activity, slide_count in ((1, 7), (2, 7), (4, 6), (5, 6), (6, 5)):
    for slide in range(2, slide_count + 1):
        filename = f'slides/activity-{activity:02d}-slide-{slide:02d}.html'
        FILES[f'/{filename}'] = (filename, 'text/html; charset=utf-8')


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        allowed_hosts = {'127.0.0.1', 'localhost', self.server.server_address[0]}
        if self.headers.get('Host', '').split(':', 1)[0] not in allowed_hosts:
            self.send_error(403)
            return
        path = urlsplit(self.path).path
        if path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return
        if path not in FILES:
            self.send_error(404)
            return
        filename, media = FILES[path]
        data = (ROOT / filename).read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', media)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Content-Security-Policy', "default-src 'none'; style-src 'self'; script-src 'none'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1', help='Local interface address (default: 127.0.0.1)')
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, 8767), Handler)
    print(f'Fresh workshop draft: http://{args.host}:8767', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
