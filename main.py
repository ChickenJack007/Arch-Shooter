import sys
import pygame as py
from scripts.utility import gen_background
from scripts.sprites import Player, Enemy

py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 900
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_sprites = py.sprite.Group()
enemy_sprites = py.sprite.Group()
player = Player(player_sprites)

#enemy = []
#for i in range(3):
#    enemy.append(Enemy(all_sprites))

stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)

can_shoot = True
dt = 0
clock = py.time.Clock()
score = 0
timer = 2000
startup = True

font = py.font.SysFont(None, 32)
while startup:
    screen.fill('black')
    text = font.render('Press space to start', False, 'white')
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    keys = py.key.get_pressed()
    if keys[py.K_SPACE]:
        startup = False
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    py.display.update()

spawn_timer = py.event.custom_type()
py.time.set_timer(spawn_timer, timer)
while True:
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)

    player_sprites.update(dt)
    enemy_sprites.update(dt)

    player_sprites.draw(screen)
    enemy_sprites.draw(screen)

    if py.sprite.spritecollideany(player, enemy_sprites):
        player_sprites.remove(player)

    if py.sprite.groupcollide(player_sprites, enemy_sprites, True, True):
        score += 1

    text = font.render(f"Score: {score}", False, 'white')
    screen.blit(text, (20, 20))

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == spawn_timer:
            Enemy(enemy_sprites)
            timer -= 50

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
