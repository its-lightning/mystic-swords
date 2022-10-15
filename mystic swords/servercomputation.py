from turtle import right


p=["","","",""]
playerdata=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
playerlist=[]

def getplayerlist(plist):
    global playerlist
    playerlist = plist

def movemntreturn(direction,xylist,rightbool,direction2="empty"):
    print(direction)
    if direction2 == "empty":
        if direction == "right":
            rightbool = True
            return xylist[0]+10,xylist[1],rightbool
            
        if direction == "left":
            rightbool = False
            return xylist[0]-10,xylist[1],rightbool
        
        if direction == "up":
            rightbool = False
            return xylist[0],xylist[1]-10,rightbool
        
        if direction == "down":
            rightbool = False
            return xylist[0],xylist[1]+10,rightbool

    else:
        if direction == "right" and direction2 == "up" or direction == "up" and direction2 == "right":
            rightbool = True
            return xylist[0]+10,xylist[1]-10,rightbool
        if direction == "right" and direction2 == "down" or direction == "down" and direction2 == "right":
            rightbool = True
            return xylist[0]+10,xylist[1]+10,rightbool
        
        if direction == "left" and direction2 == "up" or direction == "up" and direction2 == "left":
            rightbool = False
            return xylist[0]-10,xylist[1]-10,rightbool
        if direction == "left" and direction2 == "down" or direction == "down" and direction2 == "left":
            rightbool = False
            return xylist[0]-10,xylist[1]+10,rightbool

        if direction == "left" and direction2 == "right":
            rightbool = True
            return xylist[0]+10,xylist[1],rightbool
        
        if direction == "right" and direction2 == "left":
            rightbool = True
            return xylist[0]-10,xylist[1],rightbool
        
        if direction == "down" and direction2 == "up":
            rightbool = False
            return xylist[0],xylist[1]-10,rightbool
        
        if direction == "up" and direction2 == "down":
            rightbool = False
            return xylist[0],xylist[1]+10,rightbool
        

    
def computedata(data):
    playernoofdata = data.split(".")[0]
    datalist = data.split(".")
    for i in range(0,4):
        rightbool=0
        if p[i] != datalist[0] and playerlist[i] == playernoofdata:
            p[i] = data
            if datalist[1] in "rightleftdownup":
                print(datalist)
                if len(datalist) == 2:
                    px,py,rightbool = movemntreturn(datalist[1],playerdata[i],rightbool)
                else:
                    px,py,rightbool = movemntreturn(datalist[1],playerdata[i],rightbool,datalist[2])
                
                playerdata[i][0],playerdata[i][1],playerdata[i][2] = px,py,rightbool

    return playerdata