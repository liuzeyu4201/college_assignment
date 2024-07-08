# main.py
# 主程序

import pygame
import sys
from settings import *
from game_functions import draw_snake, draw_fruit, check_collision, generate_fruit, show_score

def game_intro(screen, clock):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_SPACE:
                    intro = False
        
        screen.fill(black)
        font = pygame.font.Font(None, 36)
        text = font.render('press anything start Game ,Rmathematics 24 liuzeyu', True, white)
        screen.blit(text, (200, 200))
        pygame.display.update()
        clock.tick(15)

def game_loop(screen, clock):
    game_over = False
    game_close = False
    
    x1 = width / 2
    y1 = height / 2
    
    x1_change = 0
    y1_change = 0
    
    snake_body = []
    snake_length = 1
    score = 0  # 初始分数
    
    fruit_position = generate_fruit()
    
    while not game_over:
        
        while game_close:
            screen.fill(black)
            font = pygame.font.Font(None, 35)
            text = font.render("Game over press Q quit and C re-play", True, white)
            screen.blit(text, (100, 200))
            show_score(screen, score)  # 显示最终分数
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(screen, clock)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = block_size
        
        if check_collision(x1, y1):
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        screen.fill(black)
        draw_fruit(screen, fruit_position)
        snake_head = [x1, y1]
        snake_body.append(snake_head)
        
        if len(snake_body) > snake_length:
            del snake_body[0]
        
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(screen, snake_body)
        show_score(screen, score)  # 实时显示分数
        pygame.display.update()
        
        if x1 == fruit_position[0] and y1 == fruit_position[1]:
            fruit_position = generate_fruit()
            snake_length += 1
            score += 1  # 每吃一个果实，分数加1
        
        clock.tick(snake_speed)  # 使用设置中定义的蛇速度

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    game_intro(screen, clock)
    game_loop(screen, clock)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
