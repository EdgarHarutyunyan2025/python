import pygame
import sys
from random import randint
#clock=pygame.time.Clock()

pygame.init()

screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('My Pygame')

rect_color=pygame.Color((randint(0,200),randint(0,200),randint(0,200)))


fighter_image=pygame.image.load('images/fighter.png')
fighter_width,fighter_huight=fighter_image.get_size()
fighter_x,fighter_y=(screen_width/2)-(fighter_width/2),(screen_height/2)-(fighter_huight/2)

STAP=0.5

figther_is_moving_K_UP=False
figther_is_moving_K_DOWN=False
figther_is_moving_left=False
figther_is_moving_right=False

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP :
                figther_is_moving_K_UP=True
                
            if event.key==pygame.K_DOWN :
                figther_is_moving_K_DOWN=True
                
            if event.key==pygame.K_LEFT:
                figther_is_moving_left=True
                
            if event.key==pygame.K_RIGHT :
                figther_is_moving_right=True
               

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                figther_is_moving_K_UP=False
            if event.key==pygame.K_DOWN :
                figther_is_moving_K_DOWN= False
            if event.key==pygame.K_LEFT:
                figther_is_moving_left=False
            if event.key==pygame.K_RIGHT:
                figther_is_moving_right=False

    if figther_is_moving_K_UP and fighter_y>=STAP:
        fighter_y-=STAP
    if figther_is_moving_K_DOWN and fighter_y <= screen_height-fighter_huight-STAP:
        fighter_y+=STAP
    if figther_is_moving_left  and fighter_x>=STAP:
        fighter_x-=STAP
    if figther_is_moving_right and fighter_x <= screen_width-fighter_width-STAP:
        fighter_x+=STAP
           
    screen.fill((250,250,250))
    screen.blit(fighter_image,(fighter_x,fighter_y))
    pygame.display.update()

    #clock.tick(1)