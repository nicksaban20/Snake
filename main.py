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
blockSize = 20
direction = 0
point = 0
tail_length = 0
red = (255, 0, 0)
snake_color = (57, 255, 20)
apple_color = (238, 75, 43)
apple_posW = random.randint(0, WINDOW_WIDTH/blockSize - blockSize/10)
apple_posH = random.randint(0, WINDOW_HEIGHT/blockSize - blockSize/10)
x_value , y_value = (apple_posW * blockSize, apple_posH * blockSize)
pygame.draw.rect(SCREEN, snake_color, pygame.Rect(x_value, y_value, blockSize, blockSize))
snake_location = [x_value, y_value]
font_style = pygame.font.SysFont(None, 50)


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    SCREEN.blit(mesg, [WINDOW_WIDTH/5, WINDOW_HEIGHT/2])

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


while True:
    drawGrid()
    pygame.display.set_caption(f"Snake Game | Points: {point}")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_value > 0:
            direction = 1
    if keys[pygame.K_DOWN] and y_value < WINDOW_HEIGHT - blockSize:
            direction = 2
    if keys[pygame.K_LEFT] and x_value > 0:
            direction = 3  
    if keys[pygame.K_RIGHT] and x_value < WINDOW_WIDTH - blockSize:
            direction = 4  
            

    if direction == 1 and y_value > 0 - blockSize:
        snake_location.append(x_value)
        snake_location.append(y_value + blockSize)
        y_value -= blockSize
    if direction == 2 and y_value < WINDOW_HEIGHT:
        snake_location.append(x_value)
        snake_location.append(y_value - blockSize)
        y_value += blockSize
    if direction == 3 and x_value > 0 - blockSize:
        snake_location.append(x_value + blockSize)
        snake_location.append(y_value)
        x_value -= blockSize
    if direction == 4 and x_value < WINDOW_WIDTH:
        snake_location.append(x_value - blockSize)
        snake_location.append(y_value)
        x_value += blockSize

    if direction == 1 and y_value == 0 - blockSize:
        SCREEN.fill(WHITE)
        message(f"You lost and got {point} points!",red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    if direction == 2 and y_value == WINDOW_HEIGHT:
        SCREEN.fill(WHITE)
        message(f"You lost and got {point} points!",red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    if direction == 3 and x_value == 0 - blockSize:
        SCREEN.fill(WHITE)
        message(f"You lost and got {point} points!",red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    if direction == 4 and x_value == WINDOW_WIDTH:
        SCREEN.fill(WHITE)
        message(f"You lost and got {point} points!",red)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()

    time.sleep(0.075)
    SCREEN.fill(BLACK)
    drawGrid()
    pygame.draw.rect(SCREEN, snake_color, pygame.Rect(x_value, y_value, blockSize, blockSize))
    pygame.display.flip()

    pygame.draw.rect(SCREEN, apple_color, pygame.Rect(apple_posW * blockSize, apple_posH * blockSize, blockSize, blockSize))
    pygame.display.flip()

    number = 0

    for i in range(0, tail_length):
        pygame.draw.rect(SCREEN, snake_color, pygame.Rect(snake_location[number], snake_location[number + 1], blockSize, blockSize))
        pygame.display.flip()
        number += 2
        print(i)

    snake_location.clear()
    snake_location = [0, 0]

    if x_value == apple_posW * blockSize and y_value == apple_posH * blockSize:
        apple_posW = random.randint(0, WINDOW_WIDTH/blockSize - blockSize/10)
        apple_posH = random.randint(0, WINDOW_HEIGHT/blockSize - blockSize/10)
        pygame.draw.rect(SCREEN, apple_color, pygame.Rect(apple_posW * blockSize, apple_posH * blockSize, blockSize, blockSize))
        pygame.display.flip()
        point += 1
        tail_length += 1

