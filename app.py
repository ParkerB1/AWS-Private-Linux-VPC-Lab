#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 8080

class HelloHandler(BaseHTTPRequestHandler):
        def do_GET(self):
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Hello, World!\nTesting CI/CD")

if __name__ == "__main__":
        server = HTTPServer((HOST, PORT), HelloHandler)
        print(f"Server running on http://{HOST}:{PORT}")
        server.serve_forever()
