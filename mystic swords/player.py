import pygame
import client

def move(movelist,p2):
    if movelist!=[]:
            if movelist[-1]==p2[0]:
                client.post("right")
            if movelist[-1]==p2[1]:
                client.post("left")
            if movelist[-1]==p2[2]:
                client.post("down")
            if movelist[-1]==p2[3]:
                client.post("up")
    else:
        client.post("steady")