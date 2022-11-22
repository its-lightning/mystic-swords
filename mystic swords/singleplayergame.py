from datetime import datetime
import pygame
import time
import threading
import random
import pickle
import settingsdisplay

screen = pygame.display.set_mode((1366,768))

pygame.init()


keylist=[]
playerdata=[1200,380,"down",10]

font = pygame.font.Font('AngelRhapsoy.ttf',64)

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

ghostmove = pygame.image.load('player\gmove.png')
ghostmove1 = pygame.image.load('player\gmove1.png')
ghostmove2 = pygame.image.load('player\gmove2.png')
ghoststeady = pygame.image.load('player\gsteady.png')

ghostspeed = 10
ghostlist = []
maxghostno = 1
waveno = 0
steadyno = 1
escapeloop = False

sword_rect = sword_rect = pygame.Rect(-100,-100,10,10)

swordno = [0,0,0,0]

pygame.init()

runtime = 1
running = True

def resetvalues():
    global runtime,ghostlist,waveno,maxghostno,playerdata,running
    runtime,ghostlist,waveno,maxghostno,playerdata,running = 1,[],0,1,[1200,380,"down",10],True


def gameover():
    global ghostlist,running
    ghostlist = []
    screen.blit(font.render("GAME OVER",True,(255,0,0)),(490,150))
    screen.blit(font.render("Time : "+str(runtime),True,(255,0,0)),(530,280))
    screen.blit(font.render("Return To Menu",True,(255,0,0)),(452,410))
    return_rect = pygame.Rect(452,410,830-452,460-100)
    pygame.display.update()
    addhighscore()    
    gameoverloop = True
    while gameoverloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if return_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    gameoverloop = False

def escape():
    global keylist,running,escapeloop
    screen.blit(font.render("GAME PAUSED!!!!!",True,(255,0,0)),(420,50))
    screen.blit(font.render("Resume",True,(255,0,0)),(540,150+100))
    screen.blit(font.render("Settings",True,(255,0,0)),(530,280+100))
    screen.blit(font.render("End game",True,(255,0,0)),(526,410+100))
    back_rect = pygame.Rect(1366-240,768-140,217,98)
    resume_rect = pygame.Rect(540,150+100,720-540,300-250)
    settings_rect = pygame.Rect(530,280+100,720-530,330-280)
    return_rect = pygame.Rect(526,410+100,830-452,460-100)
    back = pygame.image.load(r'menu\back.png')
    pygame.display.update()
    escapeloop = True
    while escapeloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if resume_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    escapeloop = False
            if return_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    escapeloop = False
            if settings_rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    setloop = True
                    while setloop:
                        for event2 in pygame.event.get():
                            screen.blit(map,(0,0))
                            keylist = settingsdisplay.display(event2,keylist)
                            screen.blit(back,(1366-240,768-140))
                            pygame.display.update()
                            if back_rect.collidepoint(pygame.mouse.get_pos()) and event2.type == pygame.MOUSEBUTTONDOWN:
                                setloop = False
                    escapeloop = False
    

def addhighscore():    
    fh = open("highscore.dat","rb")
    data = []
    while True:
        try:
            rec = pickle.load(fh)
            data.append([rec[1],rec[2]])
        except EOFError:
            fh.close()
            break
    data.append([runtime,datetime.now().strftime(r"%d/%m/%Y")])
    fh = open("highscore.dat","wb")
    pos = 1
    for i in sorted(data)[::-1]:
        pickle.dump([pos,i[0],i[1]],fh)
        pos += 1    
    fh.flush()

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

def timedis():
    if runtime == runtime//1:
        screen.blit(font.render(str(runtime)+"0",True,(255,0,0)),(1200,10))
    else:
        screen.blit(font.render(str(runtime)+str(random.randint(0,9)),True,(255,0,0)),(1200,10))

def ghostdis():
    for i in ghostlist:
        if steadyno > 10:
            x = random.randint(1,3)
            if x==1:
                screen.blit(ghostmove,(i[0],i[1]))
            elif x==2:
                screen.blit(ghostmove1,(i[0],i[1]))
            else:
                screen.blit(ghostmove2,(i[0],i[1]))

        else:
            screen.blit(ghoststeady,(i[0],i[1]))

def swordframe():
    timedis()
    ghostdis()
    pygame.display.update()
    time.sleep(0.04)
            


def mapdis():
    screen.blit(map,(0,0))

def sword():
    global sword_rect
    if playerdata[2] == "down":
        sword_rect = pygame.Rect(playerdata[0]-2,playerdata[1]-2,50,100)
        #pygame.draw.rect(screen, (255,0,0), sword_rect)
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
        sword_rect = pygame.Rect(playerdata[0]-2,playerdata[1]-2,100,50)
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
        sword_rect = pygame.Rect(playerdata[0]-52,playerdata[1]-2,100,50)
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
        sword_rect = pygame.Rect(playerdata[0]-2,playerdata[1]-52,50,100)
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

    for i in pressedlist:
        if pressedlist[0] == "27":
            escape()
            pressedlist.remove("27")
        if i in keylist[0:4]:
            directionlist.append(i)
        if i in keylist[4:5]:
            sword()
            sword_rect = pygame.Rect(-100,-100,10,10)
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
    
def ghost(i):
    global running
    try:
        disx = random.randint(ghostspeed-2,ghostspeed+2)
        disy = random.randint(8,11)
        ran = random.randint(1,3)

        ghostlist[i][0] -= disx #displacment
        if ran == 1 and 200 < ghostlist[i][1] + disy: #displacmenty
            ghostlist[i][1] -= disy
        if ran == 2 and 694 > ghostlist[i][1] + disy:
            ghostlist[i][1] += disy

        if ghostlist[i][0] < 250:
            running = False

        if sword_rect.collidepoint(ghostlist[i][0]+10,ghostlist[i][1]+15):
            ghostlist.remove(ghostlist[i])

        time.sleep(0.08)
    except IndexError:
        pass

                
def wave():
    global waveno,maxghostno
    waveno += 1
    maxghostno += random.randint(2,6)#noincrease

    for i in range(0,maxghostno):
        ghostlist.append([random.randint(1100,1310),random.randint(40,649),2])

    while ghostlist != []:
        if escapeloop == False:
            for i in range(len(ghostlist)):
                temp = len(ghostlist)
                ghostthread = threading.Thread(target = ghost(i))
                ghostthread.start()
    
                time.sleep(0.02)
            
def timer():
    global runtime
    while running:
        if not escapeloop:
            time.sleep(0.01)
            runtime = round(runtime + 0.01,2) 
        

def main():
    resetvalues()
    global steadyno
    pressedlist = []
    timethread = threading.Thread(target = timer)
    timethread.start()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            pressedlist = keysheld(pressedlist,event)
        playerdata[0],playerdata[1] = movement(pressedlist)
        screen.blit(map,(0,0))
        steadyno += 1
        timedis()
        ghostdis()
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

        if ghostlist == []:
            steadyno = 0
            playerdata[0],playerdata[1] = 200,380
            screen.blit(map,(0,0))
            screen.blit(rightlist[moveno[0]],(playerdata[0],playerdata[1]))
            screen.blit(font.render("WAVE "+str(waveno+1),True,(255,0,0)),(550,350))
            pygame.display.update()
            time.sleep(0.5)
            wavethread = threading.Thread(target = wave)
            wavethread.start()
            

        time.sleep(0.04)
    
    gameover()