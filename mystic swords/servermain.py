from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

apple=["left","power1"]

def getport(x):
    return x

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        output = apple[1]
        self.wfile.write(output.encode())
        
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        print(form["keys"].value)
        
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

def start():
    with HTTPServer(('', 6666), handler) as server:
        server.serve_forever()
