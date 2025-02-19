import http.server
import socketserver
import json

PORT = 8000

class run(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)



with socketserver.TCPServer(("", PORT),run ) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()