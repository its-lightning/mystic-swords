import requests
import multiplayerdisplay

ipcode = ""

def ip(ip):
    global ipcode
    ipcode = ip

def get(screen):
    response = requests.get('http://'+ipcode+':6665')
    multiplayerdisplay.display(response.text,screen)

def post(data):
    url = "http://"+ipcode+":6665"
    
    send={"keys":data}
    
    x = requests.post(url,data = send)



