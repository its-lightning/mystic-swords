p=["","","",""]
playerxy=[[0,0],[0,0],[0,0],[0,0]]
playerlist=[]

def getplayerlist(plist):
    global playerlist
    playerlist = plist

def movemntreturn(direction,xylist):
    if direction == "right":
        return xylist[0]+10,xylist[1]
    
    if direction == "left":
        return xylist[0]-10,xylist[1]
    
    if direction == "up":
        return xylist[0],xylist[1]-10
    
    if direction == "down":
        return xylist[0],xylist[1]+10
    
def computedata(data):
    playernoofdata = data.split(".")[0]
    datalist = data.split(".")

    print(data)
    for i in range(0,4):
        print(playerlist[i],playernoofdata)
        if p[i] != datalist[0] and playerlist[i] == playernoofdata:
            p[i] = data
            
            if datalist[1] in "rightleftdownup":
                px,py = movemntreturn(datalist[1],playerxy[i])
                playerxy[i][0],playerxy[i][1] = px,py

    return playerxy