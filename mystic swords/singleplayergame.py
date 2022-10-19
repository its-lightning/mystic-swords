import pygame
keylist=[]
playerdata=[0,0,""]

stable = pygame.image.load('player\stable 1.png')

pygame.init()

def keys(l):
    global keylist
    keylist=l

def keysheld(pressedlist,event):
    if event.type == pygame.KEYDOWN and event.key not in pressedlist:
        pressedlist.append(str(event.key))   
    if event.type == pygame.KEYUP:
        try:
            pressedlist.remove(str(event.key))
        except:
            pass
    return pressedlist

def movement(pressedlist):
    directionlist=[]
    for i in pressedlist:
        if i in "10097119115":
            directionlist.append(i)
    
    if len(directionlist) == 1:
        if directionlist[-1] == keylist[0]:
            return playerdata[0]+10,playerdata[1]
            
        if directionlist[-1] == keylist[1]:
            return playerdata[0]-10,playerdata[1]
        
        if directionlist[-1] == keylist[2]:
            return playerdata[0],playerdata[1]-10
        
        if directionlist[-1] == keylist[3]:
            return playerdata[0],playerdata[1]+10

    elif len(directionlist) == 2:
        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[2] or directionlist[-1] == keylist[2] and directionlist[-2] == keylist[0]:
            return playerdata[0]+10,playerdata[1]-10

        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[3] or directionlist[-1] == keylist[3] and directionlist[-2] == keylist[0]:
            return playerdata[0]+10,playerdata[1]+10
        
        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[2] or directionlist[-1] == keylist[2] and directionlist[-2] == keylist[1]:
            return playerdata[0]-10,playerdata[1]-10
            
        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[3] or directionlist[-1] == keylist[3] and directionlist[-2] == keylist[1]:
            return playerdata[0]-10,playerdata[1]+10

        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[0]:
            return playerdata[0]+10,playerdata[1]
        
        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[1]:
            return playerdata[0]-10,playerdata[1]
        
        if directionlist[-1] == keylist[3] and directionlist[-2] == keylist[2]:
            return playerdata[0],playerdata[1]-10
        
        if directionlist[-1] == keylist[2] and directionlist[-2] == keylist[3]:
            return playerdata[0],playerdata[1]+10
    
    return playerdata[0],playerdata[1]

def main(screen):
    pressedlist=[]
    while True:
        for event in pygame.event.get():
            pressedlist = keysheld(pressedlist,event)
        playerdata[0],playerdata[1]=movement(pressedlist)
        screen.fill((0,0,0))
        screen.blit(stable,(int(playerdata[0]),int(playerdata[1])))
        pygame.display.update()