import pygame
import time
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)



number = 0
BLOCK_SIZE = 20
DIRECTION = 0
POINT = 0
TAIL_LENGTH = 1
red = (255, 0, 0)
snake_color = (57, 255, 20)
apple_color = (238, 75, 43)
apple_posW = random.randint(0, WINDOW_WIDTH//BLOCK_SIZE - 1)
apple_posH = random.randint(0, WINDOW_HEIGHT//BLOCK_SIZE - 1)
x_value, y_value = (100, 60)
snake_location = [x_value, y_value]

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [WINDOW_WIDTH/5, WINDOW_HEIGHT/2])

def drawGrid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def drawSnake():
    for segment in snake_body:
        pygame.draw.rect(SCREEN, snake_color, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

snake_body = [[140, 60], [120, 60], [100, 60], [80, 60]]

while True:
    drawGrid()
    pygame.display.set_caption(f"Snake Game | Points: {POINT}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and DIRECTION != 2:
        DIRECTION = 1
    if keys[pygame.K_DOWN] and DIRECTION != 1:
        DIRECTION = 2
    if keys[pygame.K_LEFT] and DIRECTION != 4:
        DIRECTION = 3  
    if keys[pygame.K_RIGHT] and DIRECTION != 3:
        DIRECTION = 4  

    if DIRECTION == 1 and y_value > 0:
        y_value -= BLOCK_SIZE
    if DIRECTION == 2 and y_value < WINDOW_HEIGHT - BLOCK_SIZE:
        y_value += BLOCK_SIZE
    if DIRECTION == 3 and x_value > 0:
        x_value -= BLOCK_SIZE
    if DIRECTION == 4 and x_value < WINDOW_WIDTH - BLOCK_SIZE:
        x_value += BLOCK_SIZE

    snake_body.append([x_value, y_value])
    if len(snake_body) > TAIL_LENGTH:
        del snake_body[0]

    if x_value == (apple_posW * BLOCK_SIZE) and y_value == (apple_posH * BLOCK_SIZE):
        apple_posW = random.randint(0, WINDOW_WIDTH//BLOCK_SIZE - 1)
        apple_posH = random.randint(0, WINDOW_HEIGHT//BLOCK_SIZE - 1)
        snake_body.append([x_value, y_value])
        POINT += 1
        TAIL_LENGTH += 1

    SCREEN.fill(BLACK)
    drawGrid()
    drawSnake()
    pygame.draw.rect(SCREEN, apple_color, pygame.Rect(apple_posW * BLOCK_SIZE, apple_posH * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

    print(snake_body)
    print()
    print(f"Apple: {apple_posW * BLOCK_SIZE}, {apple_posH * BLOCK_SIZE}")
    print()
    print(f"Snake: {x_value}, {y_value}")
    print()
    print(f"Tails: {TAIL_LENGTH}")

    if x_value <= 0 or x_value >= WINDOW_WIDTH - (TAIL_LENGTH * BLOCK_SIZE) or y_value <= 0 or y_value >= WINDOW_HEIGHT - (TAIL_LENGTH * BLOCK_SIZE):
        SCREEN.fill(WHITE)
        message(f"You lost and got {POINT} points!", red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()

    time.sleep(0.1)
