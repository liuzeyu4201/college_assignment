# game_functions.py
# 包含游戏功能的函数

import pygame
import random
from settings import *

def draw_snake(screen, snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], block_size, block_size])

def draw_fruit(screen, fruit_position):
    pygame.draw.rect(screen, red, [fruit_position[0], fruit_position[1], block_size, block_size])

def check_collision(x1, y1):
    return x1 >= width or x1 < 0 or y1 >= height or y1 < 0

def generate_fruit():
    fruit_x = random.randrange(0, width - block_size, block_size)
    fruit_y = random.randrange(0, height - block_size, block_size)
    return [fruit_x, fruit_y]

def show_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render('Score: ' + str(score), True, white)
    screen.blit(text, (0, 0))
