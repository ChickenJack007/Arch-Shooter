import sys
import pygame as py
from scripts.utility import gen_background
from scripts.sprites import Player

py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = py.sprite.Group()
player = Player(all_sprites)

stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)

can_shoot = True
dt = 0
clock = py.time.Clock()
score = 0

font = py.font.SysFont(None, 32)

timer = py.event.custom_type()
py.time.set_timer(timer, 1000)
while True:
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)

    all_sprites.update(dt)

    all_sprites.draw(screen)

    text = font.render(f"Score: {score}", False, 'white')
    screen.blit(text, (20, 20))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == timer:
            score += 1
    dt = clock.tick() / 1000

    py.display.update()

'''
Resources
pygame-ce:    https://pyga.me/docs/
Referance:    https://pyga.me/docs/
Referance:    https://www.w3schools.com/python/default.asp
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
'''
