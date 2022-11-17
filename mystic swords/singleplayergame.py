from types import MappingProxyType
import pygame
import time

screen = pygame.display.set_mode((1366,768))

keylist=[]
playerdata=[1000,600,"down",10]

map = pygame.image.load('map/map.png')


up1 = pygame.image.load('player/up 1.png')
up2 = pygame.image.load('player/up 2.png')
up3 = pygame.image.load('player/up 3.png')

down1 = pygame.image.load('player/down 1.png')
down2 = pygame.image.load('player/down 2.png')
down3 = pygame.image.load('player/down 3.png')

right1 = pygame.image.load('player/right 1.png')
right2 = pygame.image.load('player/right 2.png')
right3 = pygame.image.load('player/right 3.png')

left1 = pygame.image.load('player/left 1.png')
left2 = pygame.image.load('player/left 2.png')
left3 = pygame.image.load('player/left 3.png')

rightlist = [right1,right2,right3]
leftlist = [left1,left2,left3]
uplist = [up1,up2,up3]
downlist = [down1,down2,down3]

increase = 56

for i in range(0,3):
    
    rightlist[i] = pygame.transform.scale(rightlist[i], (increase,increase))
    rightlist[i].set_colorkey((255,255,255))
    uplist[i] = pygame.transform.scale(uplist[i], (increase,increase))
    uplist[i].set_colorkey((255,255,255))
    downlist[i] = pygame.transform.scale(downlist[i], (increase,increase))
    downlist[i].set_colorkey((255,255,255))
    leftlist[i] = pygame.transform.scale(leftlist[i], (increase,increase))
    leftlist[i].set_colorkey((255,255,255))
    
moveno = [0,0,0,0]

sup1 = pygame.image.load('player/sup 1.png')
sup2 = pygame.image.load('player/sup 2.png')
sup3 = pygame.image.load('player/sup 3.png')

sdown1 = pygame.image.load('player/sdown 1.png')
sdown2 = pygame.image.load('player/sdown 2.png')
sdown3 = pygame.image.load('player/sdown 3.png')

sright1 = pygame.image.load('player/sright 1.png')
sright2 = pygame.image.load('player/sright 2.png')
sright3 = pygame.image.load('player/sright 3.png')

sleft1 = pygame.image.load('player/sleft 1.png')
sleft2 = pygame.image.load('player/sleft 2.png')
sleft3 = pygame.image.load('player/sleft 3.png')

sup1 = pygame.transform.scale(sup1, (increase,increase))
sup2 = pygame.transform.scale(sup2, (increase,increase))
sup3 = pygame.transform.scale(sup3, (increase,increase))

sdown1 = pygame.transform.scale(sdown1, (54,68))
sdown2 = pygame.transform.scale(sdown2, (66,68))
sdown3 = pygame.transform.scale(sdown3, (88,92))

sright1 = pygame.transform.scale(sright1, (66,66))
sright2 = pygame.transform.scale(sright2, (78,60))
sright3 = pygame.transform.scale(sright3, (84,50))

sleft1 = pygame.transform.scale(sleft1, (66,66))
sleft2 = pygame.transform.scale(sleft2, (78,60))
sleft3 = pygame.transform.scale(sleft3, (84,50))



swordno = [0,0,0,0]

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

def swordframe():
    pygame.display.update()
    time.sleep(0.04)

def mapdis():
    screen.blit(map,(0,0))

def sword():
    if playerdata[2] == "down":
        mapdis()
        screen.blit(sdown1,(playerdata[0]-4,playerdata[1]-14))
        swordframe()
        mapdis()
        screen.blit(sdown2,(playerdata[0],playerdata[1]))
        swordframe()
        mapdis()
        screen.blit(sdown3,(playerdata[0]-19,playerdata[1]-12))
        swordframe()

    elif playerdata[2] == "right":
        mapdis()
        screen.blit(sright1,(playerdata[0]-14,playerdata[1]-18))
        swordframe()
        mapdis()
        screen.blit(sright2,(playerdata[0],playerdata[1]))
        swordframe()
        mapdis()
        screen.blit(sright3,(playerdata[0],playerdata[1]))
        swordframe()

    elif playerdata[2] == "left":
        mapdis()
        screen.blit(sleft1,(playerdata[0],playerdata[1]-18))
        swordframe()
        mapdis()
        screen.blit(sleft2,(playerdata[0]-20,playerdata[1]))
        swordframe()
        mapdis()
        screen.blit(sleft3,(playerdata[0]-14,playerdata[1]))
        swordframe()

    elif playerdata[2] == "up":
        mapdis()
        screen.blit(sup1,(playerdata[0],playerdata[1]))
        swordframe()
        mapdis()
        screen.blit(sup2,(playerdata[0],playerdata[1]))
        swordframe()
        mapdis()
        screen.blit(sup3,(playerdata[0]-10,playerdata[1]-10))
        swordframe()

def movement(pressedlist):
    directionlist = []
    xyposreturn = [playerdata[0],playerdata[1]]

    #print(moveno)

    for i in pressedlist:
        if i in keylist[0:4]:
            directionlist.append(i)
        if i in keylist[4:5]:
            sword()
            return playerdata[0],playerdata[1]

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
        
        if directionlist[-1] == keylist[3] and directionlist[-2] == keylist[3]:   #down and up
            if moveno[3] == 2:
                moveno[3] = 0
            else:
                moveno[3] +=1
            playerdata[2] = "down"
            xyposreturn = playerdata[0],playerdata[1]-playerdata[3]

        if directionlist[-1] == keylist[3] and directionlist[-2] == keylist[3]:   #up and down
            if moveno[3] == 2:
                moveno[3] = 0
            else:
                moveno[3] +=1
            playerdata[2] = "up"
            xyposreturn = playerdata[0],playerdata[1]+playerdata[3]
        
    def emptret():
        return playerdata[0],playerdata[1]

    print(playerdata)
    
    if xyposreturn[0] > 1310 and xyposreturn[1] > 694:
        return emptret()
    elif xyposreturn[0] < 4 and xyposreturn[1] < 40:
        return emptret()
    elif xyposreturn[0] > 1310 and xyposreturn[1] < 40:
        return emptret()
    elif xyposreturn[0] < 4 and xyposreturn[1] > 694:
        return emptret()
    elif xyposreturn[0] > 1310:
        return playerdata[0],xyposreturn[1]
    elif xyposreturn[0] < 4:
        return playerdata[0],xyposreturn[1]
    elif xyposreturn[1] > 694:
        return xyposreturn[0],playerdata[1]
    elif xyposreturn[1] < 40:
        return xyposreturn[0],playerdata[1]
    elif xyposreturn == playerdata[0:2]:
        moveno[0],moveno[1],moveno[2],moveno[3] = 0,0,0,0
        return playerdata[0],playerdata[1]
    else:
        return xyposreturn

def main():
    pressedlist = []
    while True:
        for event in pygame.event.get():
            pressedlist = keysheld(pressedlist,event)
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
        time.sleep(0.04)

        pygame.display.update()