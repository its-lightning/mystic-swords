import cv2
import pygame


screen = pygame.display.set_mode((1366,768),pygame.RESIZABLE)

def menu_music():
    pygame.mixer.init()
    pygame.mixer.music.load("menu\menu.mp3")
    pygame.mixer.music.play(1)
    
def menu():
    '''vidcap = cv2.VideoCapture('menu\menu frame.mkv')
    menu_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        frame_loaded,menu_frame = vidcap.read()
        if frame_loaded == True:
            menu_frame = cv2.cvtColor(menu_frame, cv2.COLOR_RGB2BGR)
            menu_frame = cv2.rotate(menu_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
            menu_frame = cv2.flip(menu_frame, 0)
            menu_frame = pygame.pixelcopy.make_surface(menu_frame)

            frame_x,frame_y=menu_frame.get_size() 
            screen_x,screen_y=screen.get_size()

            screen_ratio=screen_x/screen_y
            img_ratio=frame_x/frame_y

            if screen_ratio < img_ratio:
                frame_x=screen_x
                frame_y=int(frame_x/img_ratio)
                image_x=0
                image_y=(screen_y-frame_y)//2
            
            elif screen_ratio > img_ratio:
                frame_y=screen_y
                frame_x=int(frame_y*img_ratio)
                image_x=(screen_x-frame_x)//2
                image_y=0

            menu_frame = pygame.transform.scale(menu_frame, (frame_x, frame_y))
            
            screen.blit(menu_frame,((screen_x-frame_x)//2,(screen_y-frame_y)//2))
            pygame.display.update()
        else:
            break'''
    
    screen_x,screen_y=screen.get_size()
    pygame.mouse.set_pos(screen_x/2,screen_y/2)

    play = pygame.image.load('menu\play.png')

    how_to_play = pygame.image.load('menu\how to play.png')

    settings = pygame.image.load('menu\settings.png')
    
    highscore = pygame.image.load('menu\highscore.png')
    
    singleplayer = pygame.image.load('menu\singleplayer.png')

    multiplayer = pygame.image.load('menu\multiplayer.png')

    create_game = pygame.image.load('menu\create game.png')

    join_game = pygame.image.load('menu\join game.png')

    sword_left = pygame.image.load('menu\sword left.png')
    sword_right = pygame.image.load('menu\sword right.png')
    menu_dict={"play":True,"settings":True,"how to play":True,"highscore":True,"singleplayer":False,"multiplayer":False,"create":False,"join":False}

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 

        mouse_x,mouse_y = pygame.mouse.get_pos()
        menu_bg(mouse_x,mouse_y)
        screen_x,screen_y=screen.get_size()
        
        play_rect = pygame.Rect(screen_x/2-115,screen_y/2-49-270,230,98)
        how_to_play_rect = pygame.Rect(screen_x/2-115,screen_y/2-49-85,230,98)
        settings_rect = pygame.Rect(screen_x/2-115,screen_y/2-49+85,230,98)
        highscore_rect = pygame.Rect(screen_x/2-115,screen_y/2-49+270,230,98)

        singleplayer_rect = pygame.Rect(screen_x/2-337,screen_y/2-149,674,98)
        multiplayer_rect = pygame.Rect(screen_x/2-325,screen_y/2+49,650,98)

        create_rect = pygame.Rect(screen_x/2-315,screen_y/2-149,631,98)
        join_rect = pygame.Rect(screen_x/2-232,screen_y/2+49,464,98)
        
        if menu_dict["play"]==True:
            screen.blit(play,(screen_x/2-115,screen_y/2-49-270))

        if play_rect.collidepoint(mouse_x,mouse_y) and menu_dict["play"] == True:
            screen.blit(sword_left,(screen_x/2-115-169,screen_y/2-42-270))
            screen.blit(sword_right,(screen_x/2+115,screen_y/2-42-270))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return ["singleplayer"]
                '''menu_dict["play"]=False
                menu_dict["singleplayer"]=True
                menu_dict["multiplayer"]=True'''
        if menu_dict["settings"]==True:
            screen.blit(settings,(screen_x/2-231,screen_y/2-49+85))

        if settings_rect.collidepoint(mouse_x,mouse_y) and menu_dict["settings"] == True:
            screen.blit(sword_left,(screen_x/2-231-169,screen_y/2-42+85))
            screen.blit(sword_right,(screen_x/2+231,screen_y/2-42+85))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
        
        if menu_dict["how to play"]==True:
            screen.blit(how_to_play,(screen_x/2-287,screen_y/2-49-85))

        if how_to_play_rect.collidepoint(mouse_x,mouse_y) and menu_dict["how to play"] == True:
            screen.blit(sword_left,(screen_x/2-287-169,screen_y/2-42-85))
            screen.blit(sword_right,(screen_x/2+287,screen_y/2-42-85))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
        
        if menu_dict["highscore"]==True:
            screen.blit(highscore,(screen_x/2-252,screen_y/2-49+270))

        if highscore_rect.collidepoint(mouse_x,mouse_y) and menu_dict["highscore"] == True:
            screen.blit(sword_left,(screen_x/2-252-169,screen_y/2-42+270))
            screen.blit(sword_right,(screen_x/2+252,screen_y/2-42+270))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False

        

        '''if menu_dict["singleplayer"]==True:
            screen.blit(singleplayer,(screen_x/2-337,screen_y/2-149))
        
        if singleplayer_rect.collidepoint(mouse_x,mouse_y) and menu_dict["singleplayer"] == True:
            screen.blit(sword_left,(screen_x/2-337-169,screen_y/2-142))
            screen.blit(sword_right,(screen_x/2+337,screen_y/2-142))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return ["singleplayer"]
            
        if menu_dict["multiplayer"]==True:
            screen.blit(multiplayer,(screen_x/2-325,screen_y/2+49))
        
        if multiplayer_rect.collidepoint(mouse_x,mouse_y) and menu_dict["multiplayer"] == True:
            screen.blit(sword_left,(screen_x/2-325-169,screen_y/2+52))
            screen.blit(sword_right,(screen_x/2+325,screen_y/2+52))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["multiplayer"]=False
                menu_dict["singleplayer"]=False
                menu_dict["create"]=True
                menu_dict["join"]=True
                event=None
        
        if menu_dict["create"]==True:
            screen.blit(create_game,(screen_x/2-315,screen_y/2-149))
        
        if create_rect.collidepoint(mouse_x,mouse_y) and menu_dict["create"] == True and menu_dict["singleplayer"] == False:
            screen.blit(sword_left,(screen_x/2-315-169,screen_y/2-142))
            screen.blit(sword_right,(screen_x/2+315,screen_y/2-142))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return ["create"]
            
        if menu_dict["join"]==True:
            screen.blit(join_game,(screen_x/2-232,screen_y/2+49))
        
        if join_rect.collidepoint(mouse_x,mouse_y) and menu_dict["join"] == True and menu_dict["multiplayer"] == False:
            screen.blit(sword_left,(screen_x/2-232-169,screen_y/2+52))
            screen.blit(sword_right,(screen_x/2+232,screen_y/2+52))
            pygame.display.update()
            if event !=None and event.type == pygame.MOUSEBUTTONDOWN:
                return ["join"]'''
        


        pygame.display.update()
        screen.fill((0,0,0))

def menu_bg(mouse_x,mouse_y):

    move_menu_frame = pygame.image.load('menu\menu main2.png')


    screen_x,screen_y=screen.get_size()
    move_x,move_y=(1920-680-mouse_x,1080-mouse_y-400)
    screen_rect=pygame.Rect(0,0,screen_x,screen_y)
    move_rect=pygame.Rect(move_x,move_y,1380,800)
    screen.blit(move_menu_frame,(screen_x-680-mouse_x,screen_y-mouse_y-400))