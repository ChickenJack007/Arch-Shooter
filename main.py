import pygame as py
from scripts.screen import game, game_start, game_over

py.init()
running = True

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
highscore = 0

game_start(screen)
while running:
    highscore = game(screen, highscore)
    running = game_over(screen, highscore)


'''
Resources
pygame-ce:    https://pyga.me/docs/
Referance:    https://pyga.me/docs/
Referance:    https://www.w3schools.com/python/default.asp
Player laser: Made in krita: https://krita.org/en/
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
Power Up image: see Enemy link, modified with krita
'''
