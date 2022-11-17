import pygame

screen = pygame.display.set_mode((1366,768))
map = pygame.image.load('map/map.png')


right = pygame.image.load('player/right 1.png')

sright1 = pygame.image.load('player/sright 1.png')
sright2 = pygame.image.load('player/sright 2.png')
sright3 = pygame.image.load('player/sright 3.png')

x=10
y=50


increasex,increasey = 84,66 

right = pygame.transform.scale(right, (50,50))

sright1 = pygame.transform.scale(sright1, (66,66))
sright2 = pygame.transform.scale(sright2, (78,60))
sright3 = pygame.transform.scale(sright3, (84,50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                increasex += 2
            if event.key == pygame.K_s:
                increasey += 2
            if event.key == pygame.K_z:
                increasex -= 2
            if event.key == pygame.K_x:
                increasey -= 2
            sright3 = pygame.transform.scale(sright3, (increasex,increasey))
            
            if event.key == pygame.K_l:
                x += 1
            if event.key == pygame.K_k:
                y += 1
            if event.key == pygame.K_j:
                x -= 1
            if event.key == pygame.K_i:
                y -= 1
                
            if event.key == pygame.K_h:
                x += 10
            if event.key == pygame.K_g:
                y += 10
            if event.key == pygame.K_f:
                x -= 10
            if event.key == pygame.K_t:
                y -= 10


        
    print(increasex,increasey)
    #print(x,y)

    screen.blit(map,(0,0))

    screen.blit(right,(10,50))
    screen.blit(sright1,(120-18,50-18))
    screen.blit(sright2,(300,300))
    screen.blit(sright3,(x,y))



    pygame.display.update()
