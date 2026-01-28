import pygame as py
import random as rand

def gen_background(x, SCREEN_WIDTH, SCREEN_HEIGHT):
    stars = []
    for i in range(x):
        stars.append(py.Vector2(rand.randint(0, SCREEN_WIDTH), rand.randint(0, SCREEN_HEIGHT)))
    return stars

def load_img(name):
    return py.image.load(f'./images/{name}.png').convert_alpha()

def gen_player_img():
    return f'enemy{rand.randint(1, 8)}'

def game_over():
    pass
