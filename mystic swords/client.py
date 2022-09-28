import requests

def get():
    response = requests.get('http://192.168.1.12:8000')
    print(response.text)

def post(data):
    url = "http://192.168.1.12:7777"

    send={"keys":data}
    
    x = requests.post(url,data = send)



