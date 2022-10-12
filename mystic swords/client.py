import requests

def get():
    response = requests.get('http://192.168.1.6:6665')
    print(response.text)

def post(data):
    url = "http://192.168.1.6:6665"

    send={"keys":data}
    
    x = requests.post(url,data = send)



