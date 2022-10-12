import pygame
import menu
import keys
import player
import os
import threading
import client
import player


pygame.display.set_caption("Mystic Sword")

screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)

stable = pygame.image.load('player\stable 1.png')

keylist=[]

p2=["100","97","115","119"]

menu_info=menu.menu()
pygame.display.update()

pygame.init()

def clientfun(ip):
    client.ip(ip)
    player.ip(ip)
    while True:
        for event in pygame.event.get():
            client.get()
            movelist=keys.movement(keylist,event)
            player.move(movelist,p2)
        
def servermain():
    os.startfile("servermain.py")

if menu_info[0] == "create":
    thread1=threading.Thread(target=servermain)
    thread1.start()
    import socket

    name = socket.gethostname()
    ip = socket.gethostbyname(name)

    del socket

    ip=ip.split(".")
    ip=ip[-1]

    font = pygame.font.SysFont(None, 24)
    ipcode=font.render(str(ip),True,(0,0,0))
    screen.blit(ipcode,(22,0))
    
    clientfun(ip)

elif menu_info[0] == "join":  
    ip = input("enter ip ") 
    clientfun(ip)            