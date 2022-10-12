import pygame
import menu
import keys
import player
import os
import threading
import client

pygame.display.set_caption("Mystic Sword")

screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)

stable = pygame.image.load('player\stable 1.png')

keylist=[]

p2=["100","97","115","119"]

menu_info=menu.menu()
pygame.display.update()

def servermain():
    os.startfile("servermain.py")

if menu_info[0] == "create":
    thread1=threading.Thread(target=servermain)
    thread1.start()

print("a")
def main():
    while True:
        for event in pygame.event.get():
            movelist=keys.movement(keylist,event)
            player.move(movelist,p2)
            client.get()
        
main()
        
            
