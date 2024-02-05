# main.py

import pygame
from snake import Snake
from utils import white, blue


def main():
    pygame.init()

    dis_width = 800
    dis_height = 400
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Jogo da Cobrinha')

    snake_block = 10
    snake = Snake(snake_block, dis)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                snake.handle_keys(event)

        snake.update_snake_position()

        if snake.check_boundaries() or snake.check_collision():
            snake.display_game_over()
            pygame.display.update()
            pygame.time.wait(2000)
            main()

        snake.check_food_collision()
        snake.grow_snake()
        snake.draw_snake_and_food()
        snake.display_score()
        snake.tick_clock()
        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
