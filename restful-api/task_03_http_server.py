import http.server
import socketserver

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
class run(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")


with socketserver.TCPServer(("", PORT),handler ) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()