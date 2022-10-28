import pygame

screen = pygame.display.set_mode((1366,768))

img1 = pygame.image.load('player/down 1.png')
img2 = pygame.image.load('player/sdown 1.png')
map = pygame.image.load('map/map.png')

increase = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.transform.scale(sdown1, (increase,increase))
