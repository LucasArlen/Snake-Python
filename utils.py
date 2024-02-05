import pygame
import random

white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)


def message(text, color, font, surface, x, y):
    mesg = font.render(text, True, color)
    surface.blit(mesg, (x, y))


def draw_snake(snake_block, snake_list, surface):
    for block in snake_list:
        pygame.draw.rect(surface, green, [block[0], block[1], snake_block, snake_block])


def get_random_position(surface, snake_block):
    return round(random.randrange(0, surface.get_width() - snake_block) / snake_block) * snake_block, \
           round(random.randrange(0, surface.get_height() - snake_block) / snake_block) * snake_block
