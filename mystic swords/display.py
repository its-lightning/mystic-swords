import pygame
pygame.init()

stable = pygame.image.load('player\stable 1.png')
pygame.init()

def display(data,screen):
    data = data.split("+")
    tempdata = []
    for i in data:
        tempdata.append(i.split("."))

    data=tempdata

    for i in data:
        if i[0] != '-1' and i[0] != "":
            print(int(i[1]),int(i[2]))
            screen.blit(stable,(int(i[1]),int(i[2])))
            pygame.display.update()

    print(data)

