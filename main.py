import sys
import pygame as py
from scripts.utility import gen_background, spawn_enemy
from scripts.sprites import Player, Laser


py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
all_sprites = py.sprite.Group()
player = Player(all_sprites)

player_img = py.image.load("./player.png").convert()
player_rect = player_img.get_frect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)
laser = py.FRect((0, -50), (50, 25)) 
level = 0
enemy_amount = [1, 2, 3, 5, 7, 10, 15]
active_enemys = 0

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

    if laser.bottom > 0: 
        py.draw.line(screen, "red", laser.midbottom, laser.midtop, 3)
        laser.y -= 900 * dt
    else:
        if can_shoot == False:
            can_shoot = True
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
Player image: https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
Enemy images: https://icons8.com/icons/set/pixel-windows--style-color
'''
