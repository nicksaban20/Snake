import pygame
import time
import random
import logging
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_y,
    K_n,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

logging.basicConfig(level=logging.DEBUG)

black = (0, 0, 0) # Black
white = (255, 255, 255) # White
apple_color = (238, 75, 43) # Red
snake_color = (57, 255, 20) # Green
snake_head_color = (128, 128, 128) # Gray
window_height = 800
window_width = 800
fps = 10
block_size = 20


pygame.init()
SCREEN = pygame.display.set_mode((window_width, window_height))
CLOCK = pygame.time.Clock()
SCREEN.fill(black)

direction = 0
points = 0
apple_posW = random.randint(0, window_width//block_size - 1)
apple_posH = random.randint(0, window_height//block_size - 1)
snake_x, snake_y = 0, 0
while True:
    snake_x, snake_y = (random.randint(0, window_width//block_size - 1) * block_size, random.randint(0, window_width//block_size - 1) * block_size)
    if snake_x != apple_posW * block_size or snake_y != apple_posH * block_size:
        wait = True
        break
snake_location = [snake_x, snake_y]
font_style = pygame.font.SysFont(None, 50)
snake_body = [[140, 60], [120, 60], [100, 60], [80, 60]]


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [window_width/5, window_height/2])

def drawGrid():
    for x in range(0, window_width, block_size):
        for y in range(0, window_height, block_size):
            rect = pygame.Rect(x, y, block_size, block_size)
            pygame.draw.rect(SCREEN, white, rect, 1)

def drawSnake():
    for index, segment in enumerate(snake_body):
        if index == len(snake_body) - 1:  # Head of the snake
            pygame.draw.rect(SCREEN, snake_head_color, pygame.Rect(segment[0], segment[1], block_size, block_size))
        else:
            pygame.draw.rect(SCREEN, snake_color, pygame.Rect(segment[0], segment[1], block_size, block_size))

def debug():
    logging.debug(f"Snake body: {snake_body}")
    logging.debug(f"Apple position: {apple_posW * block_size}, {apple_posH * block_size}")
    logging.debug(f"Snake x and y: {snake_x}, {snake_y}")
    logging.debug(f"Direction: {direction}")

def endGame():
    SCREEN.fill(white)
    message(f"You lost and got {points} points!", apple_color)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

def restartGame():
    global direction, points, apple_posW, apple_posH, snake_x, snake_y, snake_location, snake_body, fps
    SCREEN.fill(white)
    message("Would you like to restart the game? (y/n)", black)
    pygame.display.update()
    time.sleep(5)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_y:
                direction = 0
                points = 0
                apple_posW = random.randint(0, window_width//block_size - 1)
                apple_posH = random.randint(0, window_height//block_size - 1)
                snake_x, snake_y = 0, 0
                while True:
                    snake_x, snake_y = (random.randint(0, window_width//block_size - 1) * block_size, random.randint(0, window_width//block_size - 1) * block_size)
                    if snake_x != apple_posW * block_size or snake_y != apple_posH * block_size:
                        break
                snake_location = [snake_x, snake_y]
                snake_body = [[140, 60], [120, 60], [100, 60], [80, 60]]
                fps = 10
                break
            if event.key == K_n:
                endGame()
                break
    message("Restarting the game...", black)
    pygame.display.update()
    time.sleep(1)

def pauseGame():
    SCREEN.fill(white)
    message("Game paused", black)
    pygame.display.update()
    time.sleep(1)

def resumeGame():
    SCREEN.fill(white)
    message("Game resumed", black)
    pygame.display.update()
    time.sleep(1)

wait = True
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pauseGame()
                while wait:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                exit()
                            if event.key == pygame.K_SPACE:
                                resumeGame()
                                wait = False
                                break
                    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    drawGrid()
    pygame.display.set_caption(f"Snake Game | points: {points}")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != 2:
        direction = 1
    if keys[pygame.K_DOWN] and direction != 1:
        direction = 2
    if keys[pygame.K_LEFT] and direction != 4:
        direction = 3  
    if keys[pygame.K_RIGHT] and direction != 3:
        direction = 4  

    if snake_x == 0 and direction == 3 or snake_x == window_width - block_size and direction == 4 or snake_y == 0 and direction == 1 or snake_y == window_height - block_size and direction == 2:
        restartGame()
        continue

    if direction == 1 and snake_y > 0:
        snake_y -= block_size
    if direction == 2 and snake_y < window_height - block_size:
        snake_y += block_size
    if direction == 3 and snake_x > 0:
        snake_x -= block_size
    if direction == 4 and snake_x < window_width - block_size:
        snake_x += block_size

    snake_body.append([snake_x, snake_y])
    del snake_body[0]

    if snake_x == (apple_posW * block_size) and snake_y == (apple_posH * block_size):
        apple_posW = random.randint(0, window_width//block_size - 1)
        apple_posH = random.randint(0, window_height//block_size - 1)
        snake_body.insert(0, snake_body[0])
        points += 1
        fps += 1

    SCREEN.fill(black)
    drawGrid()
    drawSnake()
    pygame.draw.rect(SCREEN, apple_color, pygame.Rect(apple_posW * block_size, apple_posH * block_size, block_size, block_size))
    pygame.display.flip()

    debug()

    if [snake_x, snake_y] in snake_body[:-1] and direction != 0:
        restartGame()
        continue

    CLOCK.tick(fps)  # Set the frame rate to 10 FPS
