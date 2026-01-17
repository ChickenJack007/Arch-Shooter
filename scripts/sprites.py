import pygame as py
class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = py.image.load("./player.png").convert()
        self.width, self.height = py.display.get_window_size()
        self.rect = self.image.get_frect(center = (self.width // 2, self.height // 2))
        self.can_shoot = True

    def update(self, dt):

        #input
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
        if keys[py.K_SPACE] or keys[py.K_z]:
            Laser(self.rect.midtop, all_sprites)



class Laser(py.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = py.image.load("./laser.png").convert()
        self.rect = self.image.get_frect()

    def update(self, dt):
        self.rect.y -= 900 * dt
        if self.rect.bottom < 0:
            self.kill()
