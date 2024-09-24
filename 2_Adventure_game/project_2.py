"""
## Introduction
Welcome to Awesome Game, a simple arcade-style game built with Pygame.

## Features
- Control a spaceship with left and right arrow keys.
- Fire rockets to destroy descending alien ships.
- Increasing difficulty as you progress by destroying more aliens.
- Game over screen with final score display.

## Install Pygame
   ```
   pip install pygame
   ```"""

import sys
from random import randint

#This module implements a game using Pygame.
import pygame

pygame.init()

# Screen setup
bg=pygame.image.load('2_Adventure_game\\images\\pngtree-game.jpg')
game_font=pygame.font.Font(None,30)
SCREEN_WIDTH=1200
SCREEN_HEIGHT=650
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Awesome Game')

# Fighter parameters
fighter_image=pygame.image.load('2_Adventure_game\\images\\fighter.png')
fighter_width,fighter_huight=fighter_image.get_size()
fighter_x,fighter_y=(SCREEN_WIDTH/2)-(fighter_width/2),(SCREEN_HEIGHT-fighter_huight)
STAP=0.3

FIGHTER_IS_MOVING_LEFT=False
FIGHTER_IS_MOVING_RIGHT=False

# Parameters Rocket
rocket_image=pygame.image.load('2_Adventure_game\\images\\rocket.png')
rocket_width,rocket_height=rocket_image.get_size()
ROCKET_X=0
ROCKET_STAP_Y=0
ROCKET_WAS_FIRED=False
ROCKET_STAP=0.5

# Parameters alien
ALIEN_IMAGE=pygame.image.load('2_Adventure_game\\images\\alien.png')
ALIEN_WIDTH,ALIEN_HEIGHT=ALIEN_IMAGE.get_size()
ALIEN_X=randint(0,SCREEN_WIDTH-ALIEN_WIDTH)
ALIEN_Y=0
ALIEN_STAP=0.05
NUMBER_OF_ARROWS=0
GAME_IS_RUNNING=True
BACK_GROUND_X=0
# Creating sound
sound=pygame.mixer.Sound('2_Adventure_game\\mp3\\11_Stage.mp3')
sound.play()

# Creating sound Shots
Shots_sound=pygame.mixer.Sound('2_Adventure_game\\mp3\\vyistrel.mp3')

# Creating the sound of explosions
EXPLOSIONS_SOUND=pygame.mixer.Sound('2_Adventure_game\\mp3\\vzryiv.mp3')
EXPLOSIONS_COUNT=0

while GAME_IS_RUNNING:
    for event in pygame.event.get():
        if event.type==768:
            if event.key==1073741904: #pygame.K_LEFT
                # Handle left arrow key press
                FIGHTER_IS_MOVING_LEFT=True
            if event.key==1073741903: #pygame.K_RIGHT
                # Handle right arrow key press
                FIGHTER_IS_MOVING_RIGHT=True
            if event.key==32: #pygame.K_SPACE
                # Handle spacebar press
                Shots_sound.play()
                ROCKET_WAS_FIRED=True
                ROCKET_X=fighter_x+(fighter_width/2)-(rocket_width/2)
                ROCKET_STAP_Y=fighter_y-rocket_height

        if event.type==769: #pygame.KEYUP
            if event.key==1073741904: #pygame.K_LEFT
                # Handle left arrow key press
                FIGHTER_IS_MOVING_LEFT=False
            if event.key==1073741903: #pygame.K_RIGHT
                # Handle right arrow key release
                FIGHTER_IS_MOVING_RIGHT=False


    if event.type==256: #pygame.QUIT:
        sys.exit()

    if FIGHTER_IS_MOVING_LEFT  and fighter_x>=STAP:
        fighter_x-=STAP

    if FIGHTER_IS_MOVING_RIGHT and fighter_x <= SCREEN_WIDTH-fighter_width-STAP:
        fighter_x+=STAP

    ALIEN_Y+=ALIEN_STAP
    if ROCKET_WAS_FIRED and ROCKET_STAP_Y + rocket_height<0:
        ROCKET_WAS_FIRED=False

    if ROCKET_WAS_FIRED:
        ROCKET_STAP_Y-=ROCKET_STAP

    # Creating a background
    screen.blit(bg,(BACK_GROUND_X,0))
    screen.blit(bg,(BACK_GROUND_X+1200,0))
    BACK_GROUND_X-=0.05
    if int(BACK_GROUND_X)==-1200:
        BACK_GROUND_X=0

    # Creating figther
    screen.blit(fighter_image,(fighter_x,fighter_y))
    # Creation of alien
    screen.blit(ALIEN_IMAGE,(ALIEN_X,ALIEN_Y))
    # Creating Rocket
    if ROCKET_WAS_FIRED:
        screen.blit(rocket_image,(ROCKET_X,ROCKET_STAP_Y))

    pygame.display.update()

    if ALIEN_Y+ALIEN_HEIGHT>fighter_y:
        GAME_IS_RUNNING=False

    if (ROCKET_WAS_FIRED and ALIEN_X< ROCKET_X and ROCKET_X<ALIEN_X+ALIEN_WIDTH-rocket_width and ALIEN_Y<ROCKET_STAP_Y<ALIEN_Y+ALIEN_HEIGHT-rocket_height):
        ROCKET_WAS_FIRED=False
        EXPLOSIONS_SOUND.play()
        EXPLOSIONS_COUNT+=1
        ALIEN_X=randint(0,SCREEN_WIDTH-ALIEN_WIDTH)
        ALIEN_Y=0
        NUMBER_OF_ARROWS+=1
        if NUMBER_OF_ARROWS>1:
            ALIEN_STAP+=0.01


game_over_text=game_font.render('GAME OVER',True,'white')
game_over_rectangle=game_over_text.get_rect()
game_over_rectangle.center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
Explosions_text=game_font.render(f"{EXPLOSIONS_COUNT} POINTS",True,'white')
Explosions_rectangle=Explosions_text.get_rect()
Explosions_rectangle.center=(600,(SCREEN_HEIGHT/2)+50)
game_over_sound=pygame.mixer.Sound('2_Adventure_game\\mp3\\24_Game Over.mp3')
sound.stop()
game_over_sound.play()
screen.blit(game_over_text,game_over_rectangle)
screen.blit(Explosions_text,Explosions_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()
