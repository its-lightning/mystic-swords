from types import MappingProxyType
import pygame
import time

keylist=[]
playerdata=[100,100,"down",1]

map = pygame.image.load('map/map.png')


up1 = pygame.image.load('player/up 1.jpg')
up2 = pygame.image.load('player/up 2.jpg')
up3 = pygame.image.load('player/up 3.jpg')

down1 = pygame.image.load('player/down 1.jpg')
down2 = pygame.image.load('player/down 2.jpg')
down3 = pygame.image.load('player/down 3.jpg')

right1 = pygame.image.load('player/right 1.jpg')
right2 = pygame.image.load('player/right 2.jpg')
right3 = pygame.image.load('player/right 3.jpg')

left1 = pygame.image.load('player/left 1.jpg')
left2 = pygame.image.load('player/left 2.jpg')
left3 = pygame.image.load('player/left 3.jpg')

rightlist = [right1,right2,right3]
leftlist = [left1,left2,left3]
uplist = [up1,up2,up3]
downlist = [down1,down2,down3]

moveno = [0,0,0,0]

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
    directionlist = []
    xyposreturn = [playerdata[0],playerdata[1]]
    for i in pressedlist:
        if i in "10097119115":
            directionlist.append(i)
    
    if len(directionlist) == 1:
        if directionlist[-1] == keylist[0]:                   #right
            if moveno[0] == 2:
                moveno[0] = 0
            else:
                moveno[0] +=1
            playerdata[2] = "right"
            xyposreturn = playerdata[0]+playerdata[3],playerdata[1]
            
        if directionlist[-1] == keylist[1]:                   #left
            if moveno[1] == 2:
                moveno[1] = 0
            else:
                moveno[1] +=1
            playerdata[2] = "left"
            xyposreturn = playerdata[0]-playerdata[3],playerdata[1]
        
        if directionlist[-1] == keylist[2]:                   #up
            if moveno[2] == 2:
                moveno[2] = 0
            else:
                moveno[2] +=1
            playerdata[2] = "up"
            xyposreturn = playerdata[0],playerdata[1]-playerdata[3]
        
        if directionlist[-1] == keylist[3]:                   #down
            if moveno[3] == 2:
                moveno[3] = 0
            else:
                moveno[3] +=1
            playerdata[2] = "down"
            xyposreturn = playerdata[0],playerdata[1]+playerdata[3]

    elif len(directionlist) == 2:
        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[2] or directionlist[-1] == keylist[2] and directionlist[-2] == keylist[0]:   #righy and up
            if moveno[0] == 2:
                moveno[0] = 0
            else:
                moveno[0] +=1
            playerdata[2] = "right"
            xyposreturn = playerdata[0]+playerdata[3],playerdata[1]-playerdata[3]

        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[3] or directionlist[-1] == keylist[3] and directionlist[-2] == keylist[0]:   #right and down
            if moveno[0] == 2:
                moveno[0] = 0
            else:
                moveno[0] +=1
            playerdata[2] = "right"
            xyposreturn = playerdata[0]+playerdata[3],playerdata[1]+playerdata[3]
        
        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[2] or directionlist[-1] == keylist[2] and directionlist[-2] == keylist[1]:   #left and up
            if moveno[1] == 2:
                moveno[1] = 0
            else:
                moveno[1] +=1
            playerdata[2] = "left"
            xyposreturn = playerdata[0]-playerdata[3],playerdata[1]-playerdata[3]
            
        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[3] or directionlist[-1] == keylist[3] and directionlist[-2] == keylist[1]:   #left and down
            if moveno[1] == 2:
                moveno[1] = 0
            else:
                moveno[1] +=1
            playerdata[2] = "left"
            xyposreturn = playerdata[0]-playerdata[3],playerdata[1]+playerdata[3]

        if directionlist[-1] == keylist[1] and directionlist[-2] == keylist[0]:   #right and left
            if moveno[0] == 2:
                moveno[0] = 0
            else:
                moveno[0] +=1
            playerdata[2] = "right"
            xyposreturn = playerdata[0]+playerdata[3],playerdata[1]
        
        if directionlist[-1] == keylist[0] and directionlist[-2] == keylist[1]:   #left and right
            if moveno[1] == 2:
                moveno[1] = 0
            else:
                moveno[1] +=1
            playerdata[2] = "left"
            xyposreturn = playerdata[0]-playerdata[3],playerdata[1]
        
        if directionlist[-1] == keylist[3] and directionlist[-2] == keylist[2]:   #down and up
            if moveno[3] == 2:
                moveno[3] = 0
            else:
                moveno[3] +=1
            playerdata[2] = "down"
            xyposreturn = playerdata[0],playerdata[1]-playerdata[3]
        
        if directionlist[-1] == keylist[2] and directionlist[-2] == keylist[3]:   #up and down
            if moveno[2] == 2:
                moveno[2] = 0
            else:
                moveno[2] +=1
            playerdata[3] = "up"
            xyposreturn = playerdata[0],playerdata[1]+playerdata[3]
        
    def emptret():
        return playerdata[0],playerdata[1]

    
    if xyposreturn[0] > 1275 and xyposreturn[1] > 715:
        emptret()
    elif xyposreturn[0] < 10 and xyposreturn[1] < 30:
        emptret()
    elif xyposreturn[0] > 1275 and xyposreturn[1] < 30:
        emptret()
    elif xyposreturn[0] < 10 and xyposreturn[1] > 715:
        emptret()
    elif xyposreturn[0] > 1275:
        return playerdata[0],xyposreturn[1]
    elif xyposreturn[0] < 10:
        return playerdata[0],xyposreturn[1]
    elif xyposreturn[1] > 715:
        return xyposreturn[0],playerdata[1]
    elif xyposreturn[1] < 30:
        return xyposreturn[0],playerdata[1]
    elif xyposreturn == playerdata[0:2]:
        moveno[0],moveno[1],moveno[2],moveno[3] = 0,0,0,0
        return playerdata[0],playerdata[1]
    else:
        return xyposreturn

def main(screen):
    pressedlist=[]
    while True:
        for event in pygame.event.get():
            pressedlist = keysheld(pressedlist,event)
        print(playerdata)
        playerdata[0],playerdata[1] = movement(pressedlist)
        screen.blit(map,(0,0))
        if playerdata[2] == "right":
            screen.blit(rightlist[moveno[0]],(playerdata[0],playerdata[1]))
        if playerdata[2] == "left":
            screen.blit(leftlist[moveno[1]],(playerdata[0],playerdata[1]))
        if playerdata[2] == "up":
            screen.blit(uplist[moveno[2]],(playerdata[0],playerdata[1]))
        if playerdata[2] == "down":
            screen.blit(downlist[moveno[3]],(playerdata[0],playerdata[1]))
        time.sleep(0.02)

        pygame.display.update()