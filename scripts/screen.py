import pygame as py
from scripts.utility import gen_background
from scripts.sprites import Player, Enemy
import sys

def game(screen):
    player_sprites = py.sprite.Group()
    enemy_sprites = py.sprite.Group()
    player = Player(player_sprites)

    dt = 0
    clock = py.time.Clock()
    global score
    score = 0
    timer = 1500
    width, height = py.display.get_window_size()
    stars = gen_background(500, width, height)
    spawn_timer = py.event.custom_type()
    py.time.set_timer(spawn_timer, timer)
    
    font = py.font.SysFont(None, 32)
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
            break
    
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

def game_start(screen):
    clock = py.time.Clock()
    font = py.font.SysFont(None, 50)
    width, height = py.display.get_window_size()
    startup = True
    while startup:
        clock.tick(60)
        screen.fill('black')
        text = font.render('Press space to start', True, 'white')
        screen.blit(text, (width // 2 - 150, height // 2))
        keys = py.key.get_just_pressed()
        if keys[py.K_SPACE]:
            startup = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        py.display.update()

def game_over(screen):
    clock = py.time.Clock()
    running = True
    font = py.font.SysFont(None, 70)
    width, height = py.display.get_window_size()

    while running:
        clock.tick(60)
        screen.fill('black')
        text = font.render(f'Game Over\n  Score: {score}', True, 'white')
        screen.blit(text, (width // 2 - 150, 20))
        text = font.render('Press Space to try again', True, 'white')
        screen.blit(text, (width //2 - 300, height // 2))
        keys = py.key.get_just_pressed()
        if keys[py.K_SPACE]:
            return True
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        py.display.update()


