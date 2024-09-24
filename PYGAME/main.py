import pygame
import sys
from random import randint

pygame.init()

game_font=pygame.font.Font(None,30)

screen_width=800
screen_height=600
screen_file_color=(32,52,71)
screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Awesome Game')

fighter_image=pygame.image.load('images/fighter.png')

fighter_width,fighter_huight=fighter_image.get_size()
fighter_x,fighter_y=(screen_width/2)-(fighter_width/2),(screen_height-fighter_huight)
STAP=0.3

figther_is_moving_left=False
figther_is_moving_right=False

rocket_image=pygame.image.load('images/rocket.png')
rocket_width,rocket_height=rocket_image.get_size()
rocket_x=0
rocket_y=0
rocket_was_fired=False
ROCKET_STAP=0.5

alien_image=pygame.image.load('images/alien.png')
alien_width,alien_height=alien_image.get_size()
alien_x=randint(0,screen_width-alien_width)
alien_y=0
ALIEN_STAP=0.05   

game_is_running=True

while game_is_running:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                figther_is_moving_left=True
                
            if event.key==pygame.K_RIGHT :
                figther_is_moving_right=True

            if event.key==pygame.K_SPACE:
                rocket_was_fired=True
                rocket_x=fighter_x+(fighter_width/2)-(rocket_width/2)
                rocket_y=fighter_y-rocket_height

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                figther_is_moving_left=False
            if event.key==pygame.K_RIGHT:
                figther_is_moving_right=False


    if event.type==pygame.QUIT:
            sys.exit()

    if figther_is_moving_left  and fighter_x>=STAP:
             fighter_x-=STAP

    if figther_is_moving_right and fighter_x <= screen_width-fighter_width-STAP:
             fighter_x+=STAP

    alien_y+=ALIEN_STAP
  
    if rocket_was_fired and rocket_y +rocket_height<0:
         rocket_was_fired=False 

    if rocket_was_fired:
         rocket_y-=ROCKET_STAP

    screen.fill(screen_file_color)
    screen.blit(fighter_image,(fighter_x,fighter_y))
    screen.blit(alien_image,(alien_x,alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image,(rocket_x,rocket_y))

    pygame.display.update()

    if alien_y+alien_height>fighter_y:
         game_is_running=False

    if rocket_was_fired and alien_x< rocket_x and rocket_x<alien_x+ alien_width-rocket_width and alien_y<rocket_y<alien_y+alien_height-rocket_height:
        rocket_was_fired=False
        alien_x=randint(0,screen_width-alien_width)
        alien_y=0




game_over_text=game_font.render('GAME OVER',True,'white')
game_over_rectangle=game_over_text.get_rect()
game_over_rectangle.center=(screen_width/2,screen_height/2)
screen.blit(game_over_text,game_over_rectangle)
pygame.display.update()
pygame.time.wait(5000)
pygame.quit()