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
    lives = 3
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
            if lives > 0:
                print(lives)
                lives -= 1
            else:
                break
    
        if py.sprite.groupcollide(player_sprites, enemy_sprites, False, True):
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
    global width, height
    width, height = py.display.get_window_size()
    avalible = True
    startup = True
    while startup:
        clock.tick(60)
        screen.fill('black')
        text = font.render('Press space to start', True, 'white')
        screen.blit(text, (width // 2 - 150, height // 2 - 200))
        text = font.render('Press h for help', True, 'white')
        screen.blit(text, (width // 2 - 120, height // 2))
        keys = py.key.get_just_pressed()
        if (keys[py.K_SPACE] or keys[py.K_z]) and avalible:
            startup = False
        if keys[py.K_h]:
            avalible = False
        if not avalible:
            avalible = help_screen(screen, font, keys)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        py.display.update()

def help_screen(screen, font, keys):
    screen.fill('black')
    text = font.render('Move with WASD or arrow keys\n         Fire with Space or Z', True, 'white')
    screen.blit(text, (width // 2 - 250, height // 2 - 300))
    text = font.render('Destroy the Microsoft products \n          Before it\'s too late', True, 'white')
    screen.blit(text, (width // 2 - 260, height // 2 - 100))
    text = font.render('Press space to return to the title screen', True, 'white')
    screen.blit(text, (width // 2 - 320, height // 2 + 300))
    if keys[py.K_SPACE]:
        return True
    else:
        return False


def game_over(screen):
    clock = py.time.Clock()
    running = True
    font = py.font.SysFont(None, 70)

    while running:
        clock.tick(60)
        screen.fill('black')
        text = font.render(f'Game Over\n  Score: {score}', True, 'white')
        screen.blit(text, (width // 2 - 150, 20))
        text = font.render('Press Space to try again\n           or q to quit', True, 'white')
        screen.blit(text, (width //2 - 300, height // 2))
        keys = py.key.get_just_pressed()
        if keys[py.K_SPACE]:
            return True
        if keys[py.K_q]:
            return False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        py.display.update()
