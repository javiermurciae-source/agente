import http.server
import socketserver
import os

PORT = 8089
DIRECTORY = "/tmp/tv_wallpapers"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Servidor sirviendo en http://0.0.0.0:{PORT}")
    httpd.serve_forever()
