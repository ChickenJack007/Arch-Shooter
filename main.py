import sys
import pygame as py
from scripts.utility import gen_background

py.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 850
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = py.image.load("./arch-linux-normal-56.png").convert()
player_rect = player_img.get_frect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)
laser = py.FRect((0, -50), (50, 20)) 

can_shoot = True
dt = 0
clock = py.time.Clock()

while True:
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)

    if laser.bottom > 0: 
        py.draw.line(screen, "red", laser.midbottom, laser.midtop, 3)
        laser.y -= 700 * dt
    else:
        can_shoot = True

    keys = py.key.get_pressed()
    if keys[py.K_w] or keys[py.K_UP]: 
        if player_rect.y > 0:
            if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                player_rect.y -= 250 * dt
            else:
                player_rect.y -= 500 * dt


    if keys[py.K_s] or keys[py.K_DOWN]:
        if player_rect.bottom < SCREEN_HEIGHT:
            if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                player_rect.y += 250 * dt
            else:
                player_rect.y += 500 * dt


    if keys[py.K_a] or keys[py.K_LEFT]:
        if player_rect.left > 0:
            if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                player_rect.x -= 400 * dt
            else:
                player_rect.x -= 500 * dt

    if keys[py.K_d] or keys[py.K_RIGHT]:
        if player_rect.right < SCREEN_WIDTH:
            if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                player_rect.x += 400 * dt
            else:
                player_rect.x += 500 * dt


    key = py.key.get_just_pressed()
    if key[py.K_SPACE] and can_shoot:
        can_shoot = False
        laser.midtop = player_rect.midtop

    screen.blit(player_img, player_rect.topleft)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    dt = clock.tick(60) / 1000
    py.display.flip()

'''
Resources
pygame-ce: https://pyga.me/docs/
Player image https://github.com/joaofranciscoguarda/arch-pixel-icons?tab=readme-ov-file
'''
