from turtle import width
import pygame
import os
WIDTH,HEIGHT = 1080,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption('First Game')

bg_color = (51,100,146) # RGB BACKGROUND COLOUR
border_color = (0,0,0) # Black color
spaceship_width,spaceship_height = 100,100

first_spaceship = pygame.image.load(os.path.join('Assets','first_spaceship.png'))
scaled_first_ship = pygame.transform.rotate(pygame.transform.scale(first_spaceship,(spaceship_width,spaceship_height)),270)
second_spaceship = pygame.image.load(os.path.join('Assets','second_spaceship.png'))
scaled_second_ship = pygame.transform.rotate(pygame.transform.scale(second_spaceship,(spaceship_width,spaceship_height)),90)

vel = 5 # Movement speed
bullet_vel = 8
border = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT) # A rectange for border

def FS_movement(first,keys_pressed):
    if keys_pressed[pygame.K_a] and first.x > 0 : # Here if 'a' key i.e. left key is pressed it will move first spaceship in -x direction
        first.x -= vel  
    if keys_pressed[pygame.K_d] and first.x < WIDTH/2 - 5 - spaceship_width : # right
        first.x += vel 
    if keys_pressed[pygame.K_w] and first.y > 0 : # up
        first.y -= vel 
    if keys_pressed[pygame.K_s] and first.y < HEIGHT - spaceship_height: # down
        first.y += vel 

def SS_movement(second,keys_pressed):
    if keys_pressed[pygame.K_LEFT] and second.x > WIDTH/2 - 5 : # Here if 'a' key i.e. left key is pressed it will move second spaceship in -x direction
        second.x -= vel  
    if keys_pressed[pygame.K_RIGHT] and second.x < WIDTH - spaceship_width : # right
        second.x += vel 
    if keys_pressed[pygame.K_UP] and second.y > 0 : # up
        second.y -= vel 
    if keys_pressed[pygame.K_DOWN] and second.y < HEIGHT - spaceship_height: # down
        second.y += vel 

def draw_window(first,second):
    WIN.fill(bg_color)
    pygame.draw.rect(WIN,border_color,border)
    WIN.blit(scaled_first_ship,(first.x,first.y))
    WIN.blit(scaled_second_ship,(second.x,second.y))
    pygame.display.update()


def main_loop(): 
    first = pygame.Rect(100,100,spaceship_width,spaceship_height) # To move spaceships in every frame 
    second = pygame.Rect(700,100,spaceship_width,spaceship_height) # To move spaceships in every frame
    clock = pygame.time.Clock()
    run = True 
    first_bullets = []
    second_bullets = []
    while run: 
        clock.tick(FPS) # Limits FPS
        for event in pygame.event.get(): # 3 lines here mean if user were to quit the programe it will close
            if event.type == pygame.QUIT: 
                run = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LCTRL: 
                    bullet = pygame.Rect(first.x,first.y,10,5)
                    first_bullets.append(bullet)
                if event.key == pygame.K_RCTRL: 
                    bullet = pygame.Rect(second.x,second.y,10,5)
                    second_bullets.append(bullet)
        keys_pressed = pygame.key.get_pressed() # List for keys being pressed
        FS_movement(first,keys_pressed)
        SS_movement(second,keys_pressed)
        draw_window(first,second)
    pygame.quit()

main_loop()
