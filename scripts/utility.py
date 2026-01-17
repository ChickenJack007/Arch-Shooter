import pygame as py
import random as rand

def gen_background(x, SCREEN_WIDTH, SCREEN_HEIGHT):
    stars = []
    for i in range(x):
        stars.append(py.Vector2(rand.randint(0, SCREEN_WIDTH), rand.randint(0, SCREEN_HEIGHT)))
    return stars

def spawn_enemy(SCREEN_WIDTH, SCREEN_HEIGHT, x, screen):
    enemy_img = []
    for i in range(x):
        enemy_img = py.image.load(f"./enemy{rand.randint(1, 8)}.png").convert()
        return screen.blit(enemy_img, (500, 500))
        enemy_img.append(enemy_img)


