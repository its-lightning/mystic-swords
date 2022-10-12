from http import server
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import pickle

playerlist=[]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        serverfile=open("serverfile.dat","rb")
        listdata = pickle.load(serverfile)
        output = ""
        
        for i in listdata:
            for j in  i:
                output += j

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

        serverfile=open("serverfile.dat","wb")
        

        if data[0:1] not in playerlist and len(playerlist) <= 4:
            playerlist.append(data[0:1])
        
        if len(playerlist) == 1 and data[0:1] == playerlist[0]:
            player1list=[data]
        else:
            player1list=[]

        if len(playerlist) == 2 and data == playerlist[1]:
            player2list=[data]
        else:
            player2list=[]
        
        if len(playerlist) == 3 and data[0:1] == playerlist[2]:
            player3list=[data]
        else:
            player3list=[]
        
        if len(playerlist) == 4 and data[0:1] == playerlist[3]:
            player4list=[data]
        else:
            player4list=[]
        
        
        
        datalist=[player1list,player2list,player3list,player4list]
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
