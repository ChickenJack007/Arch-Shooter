import pygame as py
from scripts.utility import load_img, gen_enemy_img
import random as rand

class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = load_img('player')
        self.width, self.height = py.display.get_window_size()
        self.rect = self.image.get_frect(center = (self.width // 2, self.height // 2))
        self.group = groups
        self.can_shoot = True
        self.time_shot = 0
        self.shoot_timer = 700
        self.has_powerup = False

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

        if (keys[py.K_SPACE] or keys[py.K_z]) and self.can_shoot and not self.has_powerup: 
            Laser(self.rect.midtop, self.group)
            self.can_shoot = False
            self.time_shot = py.time.get_ticks()
        elif (keys[py.K_SPACE] or keys[py.K_z]) and self.can_shoot and self.has_powerup:
            Laser(self.rect.midleft, self.group)
            Laser(self.rect.midtop, self.group)
            Laser(self.rect.midright, self.group)
            self.can_shoot = False
            self.time_shot = py.time.get_ticks()

        if self.has_powerup:
            if py.time.get_ticks() - self.powerup_time >= 5000:
                self.has_powerup = False
                self.shoot_timer = 700

        if not self.can_shoot:
            if py.time.get_ticks() - self.time_shot >= self.shoot_timer:
                self.can_shoot = True

    def powerup(self):
        self.has_powerup = True
        self.shoot_timer = 400
        self.powerup_time = py.time.get_ticks()


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
        self.image = load_img(gen_enemy_img())
        self.rect = self.image.get_frect(midbottom = (rand.randint(0, self.width), 60))


    def update(self, dt):
        if self.rect.top < self.height:
            self.rect.center += self.direction * dt
        else:
            self.kill()
        if (self.rect.right >= self.width) or (self.rect.left <= 0):
            self.direction.x *= -1
            if self.direction.x > 0:
                self.direction.x += 50 * dt
            else:
                self.direction.x -= 50 * dt

            if self.direction.y > 0:
                self.direction.y += 50 * dt
            else:
                self.direction.y -= 50 * dt
        if self.rect.bottom >= self.height or self.rect.top <= 0:
            self.direction.y *= -1
        

class Power_up(py.sprite.Sprite):
    def __init__(self, groups, seconds=3):
        super().__init__(groups)
        self.width, self.height = py.display.get_window_size()
        self.image = load_img('power-up')
        self.rect = self.image.get_frect(center = (rand.randint(40, self.width - 40), rand.randint(40, self.height - 40)))
        self.timer = seconds * 1000
        self.spawn_time = py.time.get_ticks()

    def update(self):
        if (py.time.get_ticks() - self.spawn_time)  >= self.timer:
            self.kill()
