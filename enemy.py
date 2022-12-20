# basically early player one with some changes
import pygame


# implement game over once finished in level
# base enemy, auto moving till collision
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites,):
        super().__init__(group)
        self.image = pygame.image.load('graphics/fire.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.dir = pygame.math.Vector2()
        self.speed = 3
        self.obstacle_sprites = obstacle_sprites
        self.shift = -1

    def collision(self):
        self.rect.x += self.shift * self.speed
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.dir.x < 0:
                    self.rect.left = sprite.rect.right
                if self.dir.x > 0:
                    self.rect.right = sprite.rect.left
                self.shift *= -1

    def update(self):
        self.collision()




