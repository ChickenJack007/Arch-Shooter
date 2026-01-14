import sys
import pygame as py
from scripts.utility import gen_background

py.init()
#player img source: 

SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 850
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_img = py.image.load("./arch-linux-normal-56.png").convert()
player_rect = player_img.get_frect(center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
stars = gen_background(500, SCREEN_WIDTH, SCREEN_HEIGHT)
#player_pos = py.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

#can_shoot = True
dt = 0
clock = py.time.Clock()

while True:
    screen.fill('black')
    for i in stars:
        py.draw.circle(screen, "white", i, 1)
    #py.draw.circle(screen, "white", player_pos, 20)

    keys = py.key.get_pressed()
    if keys[py.K_w] or keys[py.K_UP]: 
        if player_rect.y > 0:
            player_rect.y -= 500 * dt
            #player_pos.y -= 500 * dt
    if keys[py.K_s] or keys[py.K_DOWN]:
        if player_rect.bottom < SCREEN_HEIGHT:
            player_rect.y += 500 * dt
            #player_pos.y += 500 * dt
    if keys[py.K_a] or keys[py.K_LEFT]:
        if player_rect.left > 0:
            player_rect.x -= 500 * dt
            #player_pos.x -= 500 * dt
    if keys[py.K_d] or keys[py.K_RIGHT]:
        if player_rect.right < SCREEN_WIDTH:
            player_rect.x += 500 * dt
            #player_pos.x += 500 * dt
    key = py.key.get_just_pressed()
    #if key[py.K_SPACE] and can_shoot:
    if key[py.K_SPACE]:
        #can_shoot = False
        print("works")

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
