import pygame
import os
import random
pygame.init()
width,height = 750,600
win = pygame.display.set_mode((width,height))
fps = 75

bg = pygame.image.load(os.path.join('Assets','4.5.jpg'))
bg2 = pygame.image.load(os.path.join('Assets','4.3.jpg'))
bigbg = pygame.transform.scale(bg,(width,height-100))
bigbg2 = pygame.transform.scale(bg2,(width,103))

black = (0,0,0)
red = (255,0,0)
darkgreen = (50,100,50)
border_color = (20,150,10)
fruit_color = (230,40,0)

snake_color = (0,200,0)
snake_head_color = (0,155,30)
snake_height,snake_width= 30,30
snake_vel = 3

def snake_movement(snake,gameover = [],key = []):
    if key[-1] == 'up' and snake.y > 155:
        snake.y -= snake_vel 
    elif snake.y <= 155:
        gameover.append(True)
    if key[-1] == 'down' and snake.y < height - snake_height - 45:
        snake.y += snake_vel
    elif snake.y >= height - snake_height - 45:
        gameover.append(True)
    if key[-1] == 'right' and snake.x < width - snake_width - 20:
        snake.x += snake_vel
    elif snake.x >= width - snake_width - 20:
        gameover.append(True)
    if key[-1] == 'left' and snake.x > 15:
        snake.x -= snake_vel  
    elif snake.x <= 15:
        gameover.append(True)

def fruit_placement(snake,score = [],fruitpos = []):
    if snake.x - snake_width < fruitpos[-1].x < snake.x + snake_width and snake.y - snake_height < fruitpos[-1].y < snake.y + snake_height:
        new_fruit = pygame.Rect(random.randint(20,width - snake_width - 25),random.randint(155,height - snake_height - 40),snake_height,snake_width)
        fruitpos.append(new_fruit)
        pygame.draw.rect(win,fruit_color,fruitpos[-1])
        new_score = score[-1] + 1
        score.append(new_score)
    else:
        pygame.draw.rect(win,fruit_color,fruitpos[-1])

def snake_body_movement(gameover=[],pos = [],fruit = [],bodypos = []):
    if gameover[-1] == False:
        for i in range(1,len(fruit)):
            x,y = pos[-(11*i)]
            snake_x, snake_y = pos[-1]
            bodypart = pygame.Rect(x,y,snake_height,snake_width)
            pygame.draw.rect(win,snake_color,bodypart) 
            bodypos.append((x,y)) 
            if i > 1:
                for j in range(2,11*i):
                    if (snake_x, snake_y) == pos[-j]:
                        gameover.append(True)
                        break
    else:
        for i in range(1,len(fruit)):
            x,y = pos[-(11*i)]
            bodypart = pygame.Rect(x,y,snake_height,snake_width)
            pygame.draw.rect(win,snake_color,bodypart)     
  
def title_score(font,titlefont,score,highscore):
    display_score = font.render(f'Score : {score[-1]}', True, darkgreen)
    display_high_score = font.render(f'High Score : {highscore}', True, darkgreen)
    title = titlefont.render('SNAKE', True, darkgreen)
    win.blit(display_score,(600,60))
    win.blit(display_high_score,(50,60))
    win.blit(title,(320,50))
    if score[-1] > int(highscore):
        file = open("Highscore for snake game.txt",'w+')
        file.write(str(score[-1]))
        file.close()

def over_screen(font,font2,snake):
    display_go = font.render(f'GAME OVER', True, darkgreen)
    rerun = font2.render(f'Press enter to play again!', True, darkgreen)
    win.blit(display_go,(width/2-150,height/2 - 80))
    win.blit(rerun,(width/2 - 100,height/2))
    pygame.draw.rect(win,red,snake)

file = open("Highscore for snake game.txt",'r')
high_score = file.read()
file.close()
def main_loop():
    snake = pygame.Rect(width/2-20,height/2+30,snake_height,snake_width)
    fruit = pygame.Rect(random.randint(20,width - snake_width - 25),random.randint(155,height - snake_height - 40),snake_height,snake_width)
    # border = pygame.Rect(0,0,width,99)
    fruit_pos = [fruit]
    snake_pos = []
    body_pos = []
    key_list = [None]
    score = [0]
    font = pygame.font.SysFont('arial',25)
    title_font = pygame.font.SysFont('arial',40, True,True)
    gameover_font = pygame.font.SysFont('arial',60,True)
    rerun_font = pygame.font.SysFont('arial',20,False,True)
    clock = pygame.time.Clock()
    run = True
    game_over = [False]
    while run: 
        key = key_list[-1]
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and key_list[-1] != 'up' and key_list[-1] != 'down':
                    key = 'up'
                    key_list.append(key)
                elif event.key == pygame.K_DOWN and key_list[-1] != 'up' and key_list[-1] != 'down':
                    key = 'down'
                    key_list.append(key)
                elif event.key == pygame.K_RIGHT and key_list[-1] != 'left' and key_list[-1] != 'right':
                    key = 'right'
                    key_list.append(key)
                elif event.key == pygame.K_LEFT and key_list[-1] != 'left' and key_list[-1] != 'right':
                    key = 'left' 
                    key_list.append(key)
                elif event.key == pygame.K_RETURN:
                    key = 'enter'
                    key_list.append(key)
        win.blit(bigbg,(0,100))
        # pygame.draw.rect(win,border_color,border)
        win.blit(bigbg2,(0,0))
        pygame.draw.rect(win,snake_head_color,snake)
        fruit_placement(snake,score,fruit_pos)
        snake_body_movement(game_over,snake_pos,fruit_pos,body_pos)
        if game_over[-1] == False:
            snake_pos.append((snake.x,snake.y))
            snake_movement(snake,game_over,key_list)
        else:
            over_screen(gameover_font,rerun_font,snake)
            if key == 'enter':
                game_over.append(False)
                snake_pos.clear()
                fruit_pos.clear()
                body_pos.clear()
                score.clear()
                score.append(0)
                fruit_pos.append(fruit)
                snake = pygame.Rect(width/2-20,height/2+30,snake_height,snake_width)
        title_score(font,title_font,score,high_score)
        pygame.display.update()
    pygame.quit()
main_loop()
