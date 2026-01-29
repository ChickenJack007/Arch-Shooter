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

def game_over(screen):
    print(score)
