import sys
import pygame as py
from scripts.utility import gen_background, spawn_enemy
from scripts.sprites import Player, Laser


py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = py.sprite.Group()
player = Player(all_sprites)

stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)

can_shoot = True
dt = 0
clock = py.time.Clock()

enemy_timer = py.event.custom_type()
py.time.set_timer(enemy_timer, 700)
while True:
    dt = clock.tick() / 1000
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)

    all_sprites.update(dt)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

        if event.type == enemy_timer:
            #spawn_enemy(SCREEN_WIDTH, SCREEN_HEIGHT, 1, screen)
            pass

    all_sprites.draw(screen)
    py.display.update()

'''
Resources
pygame-ce:    https://pyga.me/docs/
Referance:    https://pyga.me/docs/
Referance:    https://www.w3schools.com/python/default.asp
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
'''
