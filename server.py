#Creating Http server
#python -m http.server --cgi 8000

#Sending Hello World message
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()


#Adding Post request
from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()


#Creating TCP Server
from socketserver import BaseRequestHandler, TCPServer

class handler(BaseRequestHandler):
    def handle(self):
        while True:
            msg = self.request.recv(1024)
            if msg == b'quit\n':
                break
            self.request.send(b'Message received: ' + msg)

with TCPServer(('', 8000), handler) as server:
    server.serve_forever()