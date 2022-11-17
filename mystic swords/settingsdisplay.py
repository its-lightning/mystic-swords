import pygame

pygame.init()

screen = pygame.display.set_mode((1366,768),pygame.RESIZABLE)
font = pygame.font.Font('AngelRhapsoy.ttf',64)

spacefont = pygame.font.Font('AngelRhapsoy.ttf',48)

tile = pygame.image.load(r'menu\tile.png')

colltile = [pygame.Rect(362,242,100,100),pygame.Rect(122,242,100,100),pygame.Rect(242,122,100,100),pygame.Rect(242,242,100,100),pygame.Rect(552,242,100,100)]


def display(event,keylist):
    screen.blit(tile,(240,120))
    screen.blit(tile,(120,240))
    screen.blit(tile,(240,240))
    screen.blit(tile,(360,240))
    screen.blit(tile,(550,240))
    
    

    if keylist[0] == "32":
        right = spacefont.render(chr(int(keylist[0])),True,(255,0,0))
        screen.blit(up,(275-30,146))
    else:
        right = font.render(chr(int(keylist[0])),True,(255,0,0))
        screen.blit(right,(395,266))

    if keylist[1] == "32":
        left =  spacefont.render(chr(int(keylist[1])),True,(255,0,0))
        screen.blit(left,(155-30,266))
    else:
        left =  font.render(chr(int(keylist[1])),True,(255,0,0))
        screen.blit(left,(155,266))
    
    if keylist[2] == "32":
        up = spacefont.render(chr(int(keylist[2])),True,(255,0,0))
        screen.blit(down,(275-30,266))
    else:
        up = font.render(chr(int(keylist[2])),True,(255,0,0))    
        screen.blit(up,(275,146))
    
    if keylist[3] == "32":
        down = spacefont.render(chr(int(keylist[3])),True,(255,0,0))
        screen.blit(down,(275-30,266))
    else:
        down = font.render(chr(int(keylist[3])),True,(255,0,0))
        screen.blit(down,(275,266))    
    
    if keylist[4] == "32":
        attack = spacefont.render("space",True,(255,0,0))
        screen.blit(attack,(585-30,266))
    else: 
        attack = font.render(chr(int(keylist[4])),True,(255,0,0))
        screen.blit(attack,(585,266))

    colltileno = 0
    
    for i in colltile:
        print(i)
        if i.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
            loop = True
            while loop:
                screen.blit(font.render("enter a control other than space",True,(255,0,0)),(630,20))
                for event2 in pygame.event.get():
                    pygame.display.update()
                    if event2.type == pygame.QUIT:
                        pygame.quit()
                    if event2.type == pygame.KEYDOWN:
                        if str(event2.key) not in keylist:
                            keylist[colltileno] = str(event2.key)
                        loop = False
                        break
                        

        
        colltileno += 1
              
            


    return keylist
    pygame.display.update()