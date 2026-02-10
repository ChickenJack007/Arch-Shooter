import pygame as py
from scripts.screen import game, game_start, game_over

py.init()
running = True

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


while running:
    game_start(screen)
    game(screen)
    running = game_over(screen)


'''
Resources
pygame-ce:    https://pyga.me/docs/
Referance:    https://pyga.me/docs/
Referance:    https://www.w3schools.com/python/default.asp
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
'''
