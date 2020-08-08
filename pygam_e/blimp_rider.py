import pygame
import time
import random

pygame.init()

#---Colors--_#

white = (255,255,255)
black = (0,0,0)


#--display variables--#

display_width = 800
display_height = 600


#--display---#

game_display = pygame.display.set_mode((display_width, display_height))
title = pygame.display.set_caption('A Game')

clock = pygame.time.Clock()



#--blimp width--#

blimp_width = 40

#--pause--#

paused = True

#--cloud dimension --#
cloud_height = 63
cloud_width = 85


#--blimp--#

image = 'pygam_e/res/blimp.png'

#--background--#

bg = 'pygam_e/res/background.png'

introbg = 'pygam_e/res/background.png'


#--start and quit --#

button = 'pygam_e/res/start.png'
q_button = 'pygam_e/res/quit.png'


#--messages--#

ms1 = 'pygam_e/res/strtmsg.png'
ms2 = 'pygam_e/res/stopmsg.png'


#--cloud obstacle --#

cloud = 'pygam_e/res/cloud1.png'


#--score--#
count = 0

def clouds_gone(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Clouds Gone : " +str(count), True, black)
    game_display.blit(text,(0,0))                   

#--cloud function --#

def disp_obstacles(posx, posy):
    global cloud
    cloud_display = pygame.image.load(cloud)
    game_display.blit(cloud_display,[posx,posy])

#--blit blimp--#

def display_blimp(x,y):
    global image
    blimp = pygame.image.load(image)
    game_display.blit(blimp,(x,y))

#--text--#

def text_objects(text,font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def disp_msg(text):
    global count
    large_text = pygame.font.Font('freesansbold.ttf',100)
    textsurf, textrect = text_objects(text, large_text)
    textrect.center = (round((display_width/2)),round((display_height/2)))
    game_display.blit(textsurf,textrect)

    pygame.display.update()

    x = 0
    
    time.sleep(2)

    count = 0

    mainloop()

#--crash--#

def blimp_crash():
    disp_msg('Blimp Crashed!!')

#-button function--#
def intro_buttons():
    #--capture mouse--#

    mouse = pygame.mouse.get_pos()

    #--click--#
    click = pygame.mouse.get_pressed()
    #print(click)
    #print(mouse)

    if 150 + 100 > mouse[0] > 150 and 450 + 75 > mouse[1] > 400:
        smsg = pygame.image.load(ms1)
        game_display.blit(smsg, (300,450))
        if click[0] == 1:
            mainloop()
    elif 500 + 100 > mouse[0] > 150 and 400 + 75 > mouse[1] >400:
        qmsg = pygame.image.load(ms2)
        game_display.blit(qmsg, (300,450))
        if click[0] == 1:
            pygame.quit()
  
    start = pygame.image.load(button)
    game_display.blit(start, (150,400))    

    quit = pygame.image.load(q_button)
    game_display.blit(quit, (500,400))

#--intro bg-- unnecessary function but why not?--#

def intro_bg():
    int_bg = pygame.image.load(introbg)
    game_display.blit(int_bg, (0,0))

#--pause buttons--#

def pause_buttons():
    global paused
     #--capture mouse--#

    mouse = pygame.mouse.get_pos()

    #--click--#
    click = pygame.mouse.get_pressed()
    #print(click)
    #print(mouse)

    if 150 + 100 > mouse[0] > 150 and 450 + 75 > mouse[1] > 400:
        smsg = pygame.image.load(ms1)
        game_display.blit(smsg, (300,450))
        if click[0] == 1:
            paused = False
    elif 500 + 100 > mouse[0] > 150 and 400 + 75 > mouse[1] >400:
        qmsg = pygame.image.load(ms2)
        game_display.blit(qmsg, (300,450))
        if click[0] == 1:
            pygame.quit()
  
    start = pygame.image.load(button)
    game_display.blit(start, (150,400))    

    quit = pygame.image.load(q_button)
    game_display.blit(quit, (500,400))   


#--pause--#

def is_pause():

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        intro_bg()
        large_text = pygame.font.Font('freesansbold.ttf',100)
        textsurf, textrect = text_objects("Paused!", large_text)
        textrect.center = (round((display_width/2)),round((display_height/2)))
        game_display.blit(textsurf,textrect)
        pause_buttons()
        pygame.display.update()

#--intro screen--#

def game_intro():
    global paused
    paused = False
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        intro_bg()
        large_text = pygame.font.Font('freesansbold.ttf',100)
        textsurf, textrect = text_objects("Blimp Rider", large_text)
        textrect.center = (round((display_width/2)),round((display_height/2)))
        game_display.blit(textsurf,textrect)

        intro_buttons()
        pygame.display.update()
        clock.tick(15)
#--bg variables --#
# bg_movement = 0
#--background--#
def background():
    # global bg_movement
    backg = pygame.image.load(bg)
    game_display.blit(backg, (0,0))

#---main_gameloop---#

def mainloop():
    global paused
    global count

    paused = False

    #-- cloud variables--#

    startx = random.randrange(0, display_width)
    starty = -600
    obs_speed = 7

    #--display--#

    x = round(display_width * 0.4)
    y = round(display_height * 0.75 )

    game_exit = False

    #--blimp speed--#

    x_change = 0
    speed = 7
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= speed
                if event.key == pygame.K_RIGHT:
                    x_change += speed
                if event.key == pygame.K_p:
                    paused = True
                    is_pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 

        x += x_change
        # game_display.fill(white)
        background()
        disp_obstacles(startx, starty)
        starty += obs_speed
        display_blimp(x,y)
        clouds_gone(count)



        #--random clouds--#

        if starty > display_height:
            starty = 0
            startx = random.randrange(0,display_width)
            count += 1
            obs_speed += 1
        #--collision--#

        if x < -10 or x > display_width - blimp_width:
            blimp_crash()

        if y < starty + cloud_height:
            # print('y cross over')
            if x > startx and x < startx + cloud_width or x + blimp_width > startx and x + blimp_width < startx + cloud_width:
                print('x crossover')
                blimp_crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
mainloop()
pygame.quit()
quit()


#main loop
#blimp
#clouds
#colission
#score
#fail menu
