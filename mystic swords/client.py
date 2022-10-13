import requests

ipcode = ""

def ip(ip):
    global ipcode
    ipcode = ip
    print(ipcode)


def get():
    print(ipcode)
    response = requests.get('http://192.168.1.'+ipcode+':6665')
    print(response.text)

def post(data):
    print(ipcode)
    url = "http://192.168.1."+ipcode+":6665"
    
    send={"keys":data}
    
    x = requests.post(url,data = send)



