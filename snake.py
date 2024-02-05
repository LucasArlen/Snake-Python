# snake.py

import pygame
from utils import get_random_position
from utils import white, blue, green, red

class Snake:
    def __init__(self, snake_block, surface):
        self.snake_block = snake_block
        self.surface = surface
        self.snake_list = []
        self.length_of_snake = 1
        self.font_style = pygame.font.SysFont(None, 30)
        self.snake_speed = 12
        self.x1_change = self.snake_block
        self.y1_change = 0
        self.x1 = self.surface.get_width() / 2
        self.y1 = self.surface.get_height() / 2
        self.foodx, self.foody = get_random_position(surface, snake_block)

    def handle_keys(self, event):
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.x1_change = -self.snake_block
            self.y1_change = 0
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.x1_change = self.snake_block
            self.y1_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            self.y1_change = -self.snake_block
            self.x1_change = 0
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.y1_change = self.snake_block
            self.x1_change = 0

    def check_boundaries(self):
        if self.x1 >= self.surface.get_width() or self.x1 < 0 or self.y1 >= self.surface.get_height() or self.y1 < 0:
            return True
        return False

    def check_collision(self):
        head = [self.x1, self.y1]
        for segment in self.snake_list[:-1]:
            if segment == head:
                return True
        return False

    def grow_snake(self):
        snake_head = [self.x1, self.y1]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length_of_snake:
            del self.snake_list[0]

    def check_food_collision(self):
        if self.x1 == self.foodx and self.y1 == self.foody:
            self.foodx, self.foody = get_random_position(self.surface, self.snake_block)
            self.length_of_snake += 1

    def update_snake_position(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change

    def draw_snake_and_food(self):
        self.surface.fill(blue)
        pygame.draw.rect(self.surface, red, [self.foodx, self.foody, self.snake_block, self.snake_block])
        for segment in self.snake_list:
            pygame.draw.rect(self.surface, green, [segment[0], segment[1], self.snake_block, self.snake_block])

    def display_score(self):
        score_font = pygame.font.SysFont(None, 35)
        value = score_font.render("Pontuação: " + str(self.length_of_snake - 1), True, white)
        self.surface.blit(value, [0, 0])

    def display_game_over(self):
        self.surface.fill(blue)
        self.message("Voce perdeu! Q para sair ou C para jogar de novo", red, self.font_style, self.surface,
                     self.surface.get_width() / 6, self.surface.get_height() / 3)

    def message(self, msg, color, font, surface, x, y):
        mesg = font.render(msg, True, color)
        surface.blit(mesg, [x, y])

    def tick_clock(self):
        pygame.time.Clock().tick(self.snake_speed)
