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

def game_start(screen):
    font = py.font.SysFont(None, 50)
    width, height = py.display.get_window_size()
    startup = True
    while startup:
        screen.fill('black')
        text = font.render('Press space to start', False, 'white')
        screen.blit(text, (width // 2 - 150, height // 2))
        keys = py.key.get_pressed()
        if keys[py.K_SPACE]:
            startup = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        py.display.update()

