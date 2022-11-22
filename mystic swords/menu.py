import cv2
import pygame
import highscoredisplay
import settingsdisplay
import time
import pickle

screen = pygame.display.set_mode((1366,768),pygame.RESIZABLE)

def menu_music():
    pygame.mixer.init()
    pygame.mixer.music.load("menu\menu.mp3")
    pygame.mixer.music.play(1)
    
def loadingmenu():
    vidcap = cv2.VideoCapture('menu\menu frame.mkv')
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
            break

def menu(keylist):
    
    screen_x,screen_y=screen.get_size()
    pygame.mouse.set_pos(screen_x/2,screen_y/2)

    next = pygame.image.load(r'menu\next.png')

    back = pygame.image.load(r'menu\back.png')

    play = pygame.image.load('menu\play.png')

    how_to_play = pygame.image.load('menu\how to play.png')

    settings = pygame.image.load('menu\settings.png')
    
    highscore = pygame.image.load('menu\highscore.png')
    
    clearscore = pygame.image.load('menu\clear.png')
    
    singleplayer = pygame.image.load('menu\singleplayer.png')

    multiplayer = pygame.image.load('menu\multiplayer.png')

    create_game = pygame.image.load('menu\create game.png')

    join_game = pygame.image.load('menu\join game.png')

    htp = [pygame.image.load('menu\htp1.png'),pygame.image.load('menu\htp2.png')]
    
    
    sword_left = pygame.image.load('menu\sword left.png')
    sword_right = pygame.image.load('menu\sword right.png')

    nextno = 0

    menu_dict={"play":True,"settings":True,"how to play":True,"highscore":True,"singleplayer":False,"multiplayer":False,"create":False,"join":False,"back":False,"highmenu":False,"settmenu":False,"htpmenu":False,"next":False,"clearscore":False}

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 

        mouse_x,mouse_y = pygame.mouse.get_pos()
        menu_bg(mouse_x,mouse_y)
        screen_x,screen_y=screen.get_size()

        play_rect = pygame.Rect(screen_x/2-115,screen_y/2-49-270,230,98)
        how_to_play_rect = pygame.Rect(screen_x/2-287,screen_y/2-49-85,574,98)
        settings_rect = pygame.Rect(screen_x/2-231,screen_y/2-49+85,463,98)
        highscore_rect = pygame.Rect(screen_x/2-258,screen_y/2-49+270,504,98)

        back_rect = pygame.Rect(screen_x-240,screen_y-140,217,98)
        clear_rect = pygame.Rect(screen_x-240,screen_y-140-150,217,98)
        next_rect = pygame.Rect(screen_x-240,screen_y-140,217,98)

        singleplayer_rect = pygame.Rect(screen_x/2-337,screen_y/2-149,674,98)
        multiplayer_rect = pygame.Rect(screen_x/2-325,screen_y/2+49,650,98)

        create_rect = pygame.Rect(screen_x/2-315,screen_y/2-149,631,98)
        join_rect = pygame.Rect(screen_x/2-232,screen_y/2+49,464,98)
        
        
        if menu_dict["back"]==True:
            screen.blit(back,(screen_x-240,screen_y-140))
            
        if menu_dict["back"]==True and back_rect.collidepoint(mouse_x,mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["back"] = False
                menu_dict["play"] = True
                menu_dict["settings"] = True
                menu_dict["highscore"] = True
                menu_dict["how to play"] = True
                menu_dict["highmenu"] = False
                menu_dict["settmenu"] = False
                menu_dict["singleplayer"] = False
                menu_dict["multiplayer"] = False 
                menu_dict["next"] = False     
                menu_dict["htpmenu"] = False
                menu_dict["clearscore"] = False
                menu_dict["create"] = False
                menu_dict["join"] = False
                nextno = 0 

        if menu_dict["htpmenu"]==True:
            screen.blit(htp[nextno-1],(10,10))
            pygame.display.update()

        if menu_dict["next"]==True:
            screen.blit(next,(screen_x-240,screen_y-140))

        if menu_dict["next"]==True and next_rect.collidepoint(mouse_x,mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if nextno == 1:
                    menu_dict["back"] = True
                    menu_dict["next"] = False
                    nextno +=1
                else:
                    nextno +=1
                time.sleep(0.1)

        if menu_dict["settmenu"]==True:
            keylist = settingsdisplay.display(event,keylist)

        if menu_dict["highmenu"]==True:
            highscoredisplay.display()

        if menu_dict["clearscore"] == True:
            screen.blit(clearscore,(screen_x-240,screen_y-140-150))


        if menu_dict["clearscore"] == True and clear_rect.collidepoint(mouse_x,mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN:            
                fh = open("highscore.dat","wb")
                pickle.dump([0,0,"--/--/--"],fh)
                fh.flush()
        
        if menu_dict["play"]==True:
            screen.blit(play,(screen_x/2-115,screen_y/2-49-270))


        if menu_dict["play"] == True and play_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(sword_left,(screen_x/2-115-169,screen_y/2-42-270))
            screen.blit(sword_right,(screen_x/2+115,screen_y/2-42-270))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #return ["singleplayer"],keylist          
                menu_dict["play"]=False
                menu_dict["singleplayer"]=True
                menu_dict["multiplayer"]=True
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
                menu_dict["back"] = True

        if menu_dict["settings"]==True:
            screen.blit(settings,(screen_x/2-231,screen_y/2-49+85))

        if menu_dict["settings"] == True and settings_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(sword_left,(screen_x/2-231-169,screen_y/2-42+85))
            screen.blit(sword_right,(screen_x/2+231,screen_y/2-42+85))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
                menu_dict["back"] = True
                menu_dict["settmenu"] = True

        if menu_dict["how to play"]==True:
            screen.blit(how_to_play,(screen_x/2-287,screen_y/2-49-85))

        if menu_dict["how to play"] == True and how_to_play_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(sword_left,(screen_x/2-287-169,screen_y/2-42-85))
            screen.blit(sword_right,(screen_x/2+287,screen_y/2-42-85))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
                menu_dict["htpmenu"] = True
                menu_dict["next"] = True
                nextno += 1

        
        if menu_dict["highscore"]==True:
            screen.blit(highscore,(screen_x/2-252,screen_y/2-49+270))

        if menu_dict["highscore"] == True and highscore_rect.collidepoint(mouse_x,mouse_y):
            screen.blit(sword_left,(screen_x/2-252-169,screen_y/2-42+270))
            screen.blit(sword_right,(screen_x/2+252,screen_y/2-42+270))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_dict["play"] = False
                menu_dict["settings"] = False
                menu_dict["highscore"] = False
                menu_dict["how to play"] = False
                menu_dict["highmenu"] = True
                menu_dict["back"] = True
                menu_dict["clearscore"] = True

        #---------------------------------\/multiplayer\/---------------------------------#
        if menu_dict["singleplayer"]==True:
            screen.blit(singleplayer,(screen_x/2-337,screen_y/2-149))
        
        if singleplayer_rect.collidepoint(mouse_x,mouse_y) and menu_dict["singleplayer"] == True:
            screen.blit(sword_left,(screen_x/2-337-169,screen_y/2-142))
            screen.blit(sword_right,(screen_x/2+337,screen_y/2-142))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                return ["singleplayer"],keylist
            
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
                return ["create"],keylist
            
        if menu_dict["join"]==True:
            screen.blit(join_game,(screen_x/2-232,screen_y/2+49))
        
        if join_rect.collidepoint(mouse_x,mouse_y) and menu_dict["join"] == True and menu_dict["multiplayer"] == False:
            screen.blit(sword_left,(screen_x/2-232-169,screen_y/2+52))
            screen.blit(sword_right,(screen_x/2+232,screen_y/2+52))
            pygame.display.update()
            if event !=None and event.type == pygame.MOUSEBUTTONDOWN:
                return ["join"],keylist
        #---------------------------------^multiplayer^---------------------------------#
        


        pygame.display.update()
        screen.fill((0,0,0))

def menu_bg(mouse_x,mouse_y):

    move_menu_frame = pygame.image.load('menu\menu main2.png')


    screen_x,screen_y=screen.get_size()
    move_x,move_y=(1920-680-mouse_x,1080-mouse_y-400)
    screen.blit(move_menu_frame,(screen_x-680-mouse_x,screen_y-mouse_y-400))