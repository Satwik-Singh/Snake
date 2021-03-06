# made by Satwik Singh

import pygame as pg
import time
import random
pg.init()   #initializing pygame
width = 500
height = 500
snake_width = 10
scr = pg.display.set_mode((width, height))  # screen of width and height of 500 pixels
scr.fill([247, 155, 155])              # fill the background with a color
clock = pg.time.Clock()
pg.display.set_caption("Snake")
font = pg.font.Font('freesansbold.ttf', 32)
text_gameover = font.render("Game Over", True, (155, 155, 155), (255, 255, 255))

def update():
    pg.display.update()

def display():
    pg.display.flip()

def snake(Snake):
    for i in Snake:
        pg.draw.rect(scr, (255,255,255), [i[0], i[1], snake_width, snake_width])

def food(x, y):
    pg.draw.rect(scr, (165,120,167), [x, y, snake_width, snake_width])


def collide():  #collision detection between food and snake with margin m
    margin = 3
    if(right and x+snake_width<=xfood+snake_width and x+snake_width>=xfood and y>=yfood-(snake_width-margin) and y<=yfood+(snake_width-margin)):
        return True
    if(left and x<=xfood+snake_width and x>=xfood and y>=yfood-(snake_width+margin) and y<=yfood+(snake_width-margin)):
        return True
    if(up and x>=xfood-(snake_width)+margin and x<=xfood+snake_width-margin and y>=yfood and y<=yfood+snake_width):
        return True
    if(down and x>=xfood-(snake_width)+margin and x<=xfood+snake_width-margin and y+snake_width>=yfood and y+snake_width<=yfood+snake_width):
        return True
    if(x==xfood and y==yfood):
        return True

# display text
def disp_text(text, pos, italic = False):
    if(not italic):
        font.set_italic(False)
        scr.blit(text, pos)
    if(italic):
        font.set_italic(True)
        scr.blit(text, pos)



x = 200
y = 200
left = False
right = False
up = False
down = False
xspeed = 0
yspeed = 0
xfood = 0
yfood = 0
fps = 150
food_eaten = True
snake_len = 1
score = snake_len - 1
start_timer = False
timer_started = False
Snake = []
update()
run = True
while( run ):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        # keypress events and direction of motion
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                xspeed = -1
                yspeed = 0
                left = True
                right = False
                up = False
                down = False
            elif event.key == pg.K_UP:
                xspeed = 0
                yspeed = -1
                left = False
                right = False
                up = True
                down = False
            elif event.key == pg.K_RIGHT:
                xspeed = 1
                yspeed = 0
                left = False
                right = True
                up = False
                down = False
            elif event.key == pg.K_DOWN:
                xspeed = 0
                yspeed = 1
                left = False
                right = False
                up = False
                down = True

    # to return sanke back in screen if goes out of it
    x+=xspeed
    y+=yspeed
    if(x>=width and xspeed>0):
        x=0-snake_width
    if(y>=height and yspeed>0):
        y=0-snake_width
    if(x<=0 and xspeed<0):
        x=width-snake_width
    if(y<=0 and yspeed<0):
        y=height-snake_width


    # randomize next food location if food eaten
    if(food_eaten):
        xfood = random.randint(0, width-snake_width)
        yfood = random.randint(0, height-snake_width)
        food_eaten = False
    food(xfood, yfood)
    food_eaten = collide()
    if(food_eaten):
        snake_len+=5

    # increase snake length and quit the game if snake eates itself
    head = []
    head.append(x)
    head.append(y)
    for i in Snake[:-1]:
        if(head==i):
            start_timer = True
    Snake.append(head)
    if(len(Snake)>snake_len):
        del Snake[0]
    snake(Snake)

    if (start_timer):
        xspeed=0
        yspeed=0
        if(not timer_started):
            timer = pg.time.get_ticks()
            timer_started = True
        seconds = (pg.time.get_ticks() - timer) / 1000
        disp_text(text_gameover, (200, 200))
        if(seconds>2):
            run = False

    update()
    clock.tick(fps)
    scr.fill([247, 155, 155])

