from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer
import servercomputation
import cgi
import pickle

playerlist=["-1","-1","-1","-1"]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        serverfile=open("serverfile.dat","rb")
        loaddata = pickle.load(serverfile)
        output=""
        loopno=0
        for i in loaddata:
            output += playerlist[loopno]+"."
            for j in i:
                output += str(j)+"."
            output += "+"
            loopno += 1

        self.wfile.write(output.encode())
        
    def do_POST(self):
        global playerlist
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        data=form["keys"].value

        datalist=data.split(".")

        serverfile=open("serverfile.dat","wb")

        if datalist[0] not in playerlist and len(playerlist) <= 4:
            emptyslot=playerlist.index("-1")
            playerlist[emptyslot]=datalist[0]
            servercomputation.getplayerlist(playerlist)

        dumpdata = servercomputation.computedata(data)

        pickle.dump(dumpdata,serverfile)
        serverfile.flush()
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

def start():
    with HTTPServer(('', 6665), handler) as server:
        server.serve_forever()

start()
