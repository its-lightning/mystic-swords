from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import pickle


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        serverfile=open("serverfile.dat","rb")
        listdata = pickle.load(serverfile)
        output = ""
        for i in listdata:
            try:
                output+=i[0]
            except:
                output=""

        self.wfile.write(output.encode())
        
    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        data=form["keys"].value

        serverfile=open("serverfile.dat","wb")
        if data[0:1]=="1":
            player1list=[data]
        else:
            player1list=[]

        if data[0:1]=="2":
            player2list=[data]
        else:
            player2list=[]
        
        datalist=[player1list,player2list]
        print(datalist)
        pickle.dump(datalist,serverfile)
        serverfile.flush()
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

def start():
    with HTTPServer(('192.168.1.6', 6665), handler) as server:
        server.serve_forever()

start()
