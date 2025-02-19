from http.server import BaseHTTPRequestHandler, HTTPServer

class run(BaseHTTPRequestHandler):
    
    def do_GET(self):
        print("Hello, this is a simple API!")