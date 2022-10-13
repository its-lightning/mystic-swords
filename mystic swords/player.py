import client

ipcode = ""

def ip(ip):
    global ipcode
    ipcode = ip

def move(movelist,p2):
    print(movelist)
    if movelist!=[]:
            if movelist[-1]==p2[0]:
                client.post(ipcode+".right")
            if movelist[-1]==p2[1]:
                client.post(ipcode+".left")
            if movelist[-1]==p2[2]:
                client.post(ipcode+".down")
            if movelist[-1]==p2[3]:
                client.post(ipcode+".up")
    else:
        client.post(ipcode+".steady")