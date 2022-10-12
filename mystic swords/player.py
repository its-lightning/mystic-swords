import pygame
import client

def move(movelist,p2):
    if movelist!=[]:
            if movelist[-1]==p2[0]:
                client.post("2right")
            if movelist[-1]==p2[1]:
                client.post("2left")
            if movelist[-1]==p2[2]:
                client.post("2down")
            if movelist[-1]==p2[3]:
                client.post("2up")
    else:
        client.post("steady")