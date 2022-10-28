import pygame
import pickle

pygame.init()

screen = pygame.display.set_mode((1366,768),pygame.RESIZABLE)
font = pygame.font.Font('AngelRhapsoy.ttf',64)

fh = open("highscore.dat","rb")
data = []
while True:
    try:
        rec = pickle.load(fh)
        data.append(rec)
    except EOFError:
        fh.close()
        break


def display():
    datay = 50
    tempdata = font.render("Position",True,(255,0,0))
    screen.blit(tempdata,(100,datay))
    tempdata = font.render("Time",True,(255,0,0))
    screen.blit(tempdata,(400,datay))
    tempdata = font.render("Date",True,(255,0,0))
    screen.blit(tempdata,(700,datay))
    datay += 100
    for i in data:
        tempdata = font.render(str(i[0]),True,(255,0,0))
        screen.blit(tempdata,(100,datay))
        tempdata = font.render(str(i[1]),True,(255,0,0))
        screen.blit(tempdata,(400,datay))
        tempdata = font.render(str(i[2]),True,(255,0,0))
        screen.blit(tempdata,(700,datay))
        datay += 60
    pygame.display.update()