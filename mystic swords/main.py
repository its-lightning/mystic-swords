import pygame
import menu
import multiplayerkeys
import os
import threading
import client
import singleplayergame


pygame.display.set_caption("Mystic Sword")


screen = pygame.display.set_mode((1366,768))

stable = pygame.image.load('player\stable 1.png')

#right left up down space \/
keylist=["100","97","119","115","32"]

menu.loadingmenu()

while True:
    menu_info,keylist = menu.menu(keylist)
    #menu_info=["singleplayer"]
    
    pygame.display.update()
    
    pygame.init()
    
    
    #---------------------------------\/multiplayer\/---------------------------------#
                
    def servermain():
        os.startfile("servermain.py")
    
    def clientfun(hostip,ip,screen):
        client.ip(hostip)
        multiplayerkeys.ip(ip)
        while True:
            for event in pygame.event.get():
                client.get(screen)
                movelist=multiplayerkeys.movement(["100","97","119","115"],event)
            else:
                client.get(screen)
    #---------------------------------^multiplayer^---------------------------------#
    
    
    if menu_info[0] == "singleplayer":
        singleplayergame.keys(keylist)
        singleplayergame.main()
    
    #---------------------------------\/multiplayer\/---------------------------------#
    elif menu_info[0] == "create":
        thread1=threading.Thread(target=servermain)
        thread1.start()
        import socket
    
        name = socket.gethostname()
        hostip = socket.gethostbyname(name)
    
        del socket
    
        ip=hostip.split(".")
        ip=ip[-1]
    
        font = pygame.font.SysFont(None, 24)
        ipcode=font.render(str(hostip),True,(0,0,0))
        screen.blit(ipcode,(22,0))
        
        clientfun(hostip,ip,screen)
    
    elif menu_info[0] == "join":  
        hostip = input("enter host ip ") 
        hostip = "192.168."+hostip
        import socket
    
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
        ip=ip.split(".")
        ip=ip[-1]
        del socket
        clientfun(hostip,ip,screen)
    #---------------------------------^multiplayer^---------------------------------#