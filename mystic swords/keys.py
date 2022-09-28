import pygame
import keyboard

    
def movement(l,event):
    if event.type == pygame.KEYDOWN and event.key not in l:
        l.append(str(event.key))   

    if event.type == pygame.KEYUP:
        l.remove(str(event.key))

    return l