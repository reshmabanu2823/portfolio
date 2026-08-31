import http.server
import functools
import os
import sys
import mimetypes

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Ensure common mime types are registered
mimetypes.add_type('text/html', '')
mimetypes.add_type('text/html', '.html')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('video/mp4', '.mp4')
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        # Prevent octet-stream downloads for extensionless routes
        base, ext = os.path.splitext(path)
        if not ext or ext == '.html':
            return 'text/html; charset=utf-8'
        return super().guess_type(path)

    def translate_path(self, path):
        translated = super().translate_path(path)
        
        # If path is a directory and has index.html
        if os.path.isdir(translated):
            index = os.path.join(translated, 'index.html')
            if os.path.exists(index):
                return index

        # If direct path does not exist, check for .html extension
        if not os.path.exists(translated):
            if os.path.exists(translated + '.html'):
                return translated + '.html'
            # Also check inside www.noth.in subdirectory
            rel = os.path.relpath(translated, DIRECTORY)
            alt = os.path.join(DIRECTORY, 'www.noth.in', rel)
            if os.path.exists(alt):
                return alt
            if os.path.exists(alt + '.html'):
                return alt + '.html'
        return translated

def run_server():
    os.chdir(DIRECTORY)
    handler = functools.partial(CustomHandler, directory=DIRECTORY)
    candidate_ports = [5234, 8899, 8092, 5173, 9000, 3001, 8081]
    httpd = None
    selected_port = None

    for port in candidate_ports:
        try:
            httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port), handler)
            selected_port = port
            break
        except OSError:
            continue

    if not httpd:
        httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        selected_port = httpd.server_address[1]

    url = f"http://localhost:{selected_port}/"
    print("=" * 60, flush=True)
    print("  Nothin' Local Web Server (MIME / Clean Routing Fixed)", flush=True)
    print(f"  Status  : Running", flush=True)
    print(f"  URL     : {url}", flush=True)
    print(f"  Path    : {DIRECTORY}", flush=True)
    print("=" * 60, flush=True)
    print("Press Ctrl+C to stop the server.\n", flush=True)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...", flush=True)
        httpd.server_close()

if __name__ == '__main__':
    run_server()
