import http.server
import functools
import os
import sys
import webbrowser

DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

    def translate_path(self, path):
        # Clean URL rewrite for extensionless html routes
        translated = super().translate_path(path)
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
    print("  Nothin' Local Web Server", flush=True)
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
