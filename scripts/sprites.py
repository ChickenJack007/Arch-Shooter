import pygame as py
from scripts.utility import load_img, gen_player_img
#from scripts.screen import hit_bottom
import random as rand

class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = load_img('player')
        self.width, self.height = py.display.get_window_size()
        self.rect = self.image.get_frect(center = (self.width // 2, self.height // 2))
        self.laser_rect = py.FRect((0, -40), (20, 25))
        self.group = groups

    def update(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_w] or keys[py.K_UP]:
            if self.rect.y > 0:
                if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                    self.rect.y -= 250 * dt
                else:
                    self.rect.y -= 500 * dt
        if keys[py.K_s] or keys[py.K_DOWN]:
            if self.rect.bottom < self.height:
                if keys[py.K_d] or keys[py.K_a] or keys[py.K_LEFT] or keys[py.K_RIGHT]:
                    self.rect.y += 250 * dt
                else:
                    self.rect.y += 500 * dt
        if keys[py.K_a] or keys[py.K_LEFT]:
            if self.rect.left > 0:
                if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x -= 400 * dt
                else:
                    self.rect.x -= 500 * dt
        if keys[py.K_d] or keys[py.K_RIGHT]:
            if self.rect.right < self.width:
                if keys[py.K_w] or keys[py.K_s] or keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x += 400 * dt
                else:
                    self.rect.x += 500 * dt
        key = py.key.get_just_pressed()
        if (key[py.K_SPACE] or key[py.K_z]): 
            Laser(self.rect.midtop, self.group)

class Laser(py.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = load_img('laser')
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 900 * dt
        if self.rect.bottom < 0:
            self.kill()


class Enemy(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.group = groups
        self.width, self.height = py.display.get_window_size()
        self.direction = py.Vector2((rand.randint(-300, 300), rand.randint(75, 175)))
        self.image = load_img(gen_player_img())
        self.rect = self.image.get_frect(midbottom = (rand.randint(0, self.width),0))


    def update(self, dt):
        if self.rect.top < self.height:
            #hit_bottom()
            self.rect.center += self.direction * dt
        else:
            #loss += 1
            self.kill()
        if (self.rect.right >= self.width) or (self.rect.left <= 0):
            self.direction.x *= -1
