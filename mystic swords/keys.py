import pygame
import keyboard
import client

ipcode = ""

playercontrols=["100","97","115","119"]

def ip(ip):
    global ipcode
    ipcode = ip
    
def movement(l,event):
    if event.type == pygame.KEYDOWN and event.key not in l:
        l.append(str(event.key))   
    if event.type == pygame.KEYUP:
        l.remove(str(event.key))
    print(l)
    retur = ipcode
    if l == []:
        retur += ".steady"
    else:
        for i in l:
            if i == '100':
                retur += ".right"
            elif i == '97':
                retur += ".left"
            elif i == '115':
                retur += ".up"
            elif i == '119':
                retur += ".down"
        
        



    client.post(retur)

