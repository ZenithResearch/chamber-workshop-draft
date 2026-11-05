#!/usr/bin/env python3
"""Serve only the fresh workshop draft on loopback."""
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

for activity in range(1, 10):
    for folder in ('plans', 'slides'):
        filename = f'{folder}/activity-{activity:02d}.html'
        FILES[f'/{filename}'] = (filename, 'text/html; charset=utf-8')


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.headers.get('Host', '').split(':', 1)[0] not in {'127.0.0.1', 'localhost'}:
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
    server = ThreadingHTTPServer(('127.0.0.1', 8767), Handler)
    print('Fresh workshop draft: http://127.0.0.1:8767', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
