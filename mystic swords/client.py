import requests
import display

ipcode = ""

def ip(ip):
    global ipcode
    ipcode = ip

def get(screen):
    response = requests.get('http://'+ipcode+':6665')
    display.display(response.text,screen)

def post(data):
    url = "http://"+ipcode+":6665"
    
    send={"keys":data}
    
    x = requests.post(url,data = send)



