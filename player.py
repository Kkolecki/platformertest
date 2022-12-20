import pygame
from config import *


# our player, implemented functions that make it interact with other tiles, self explained by function names
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites, collectible_sprites, movable_sprites, enemy_sprites):
        super().__init__(group)
        self.image = pygame.image.load('graphics/lildude.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0) # enlarge or shrink hitbox for player
        self.dir = pygame.math.Vector2()
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
        self.collectible_sprites = collectible_sprites
        self.movable_sprites = movable_sprites
        self.gravity = 0.9
        self.jump_speed = 20
        self.isJumping = True
        self.score = 0
        self.enemy_sprites = enemy_sprites

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.dir.x = +1
        elif key[pygame.K_LEFT]:
            self.dir.x = -1
        else:
            self.dir.x = 0
        if key[pygame.K_SPACE] and self.isJumping is False:
            self.dir.y = -self.jump_speed
            self.isJumping = True

    def move(self, speed):
        self.rect.x += self.dir.x * speed

    def collision(self): # also applies gravity
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.dir.x < 0:
                    self.rect.left = sprite.rect.right
                if self.dir.x > 0:
                    self.rect.right = sprite.rect.left
        self.dir.y += self.gravity
        self.rect.y += self.dir.y
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.dir.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.isJumping = False
                    self.dir.y = 0
                if self.dir.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.dir.y = 0

    def collectible(self):
        for sprite in self.collectible_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.score += 1
                sprite.kill()

    def movable(self, speed):
        for sprite, collision in zip(self.movable_sprites.sprites(), self.obstacle_sprites.sprites()):
            if sprite.rect.colliderect(self.rect):
                if self.dir.x < 0:
                    sprite.dir.x = -1
                if self.dir.x > 0:
                    sprite.dir.x = 1
                sprite.rect.x += sprite.dir.x * speed
                if collision.rect.colliderect(sprite.rect):
                    if sprite.dir.x < 0:
                        sprite.rect.left = collision.rect.right
                    if sprite.dir.x > 0:
                        sprite.rect.right = collision.rect.left

    # unstable for now, sometimes both die, sometimes enemy without touching from up, check for
    # multiple directions at once? or self.collide
    def enemy(self):
        for sprite in self.enemy_sprites:
            if self.rect.colliderect(sprite.rect):
                if self.dir.y > 0 and self.dir.x > 0 or self.dir.x < 0:
                    sprite.kill()
                if self.dir.y < 0 and self.dir.x < 0 or self.dir.x > 0:
                    self.kill()
                if self.dir.x > 0:
                    self.kill()
                if self.dir.x < 0:
                    self.kill()

    def update(self):
        self.input()
        self.move(self.speed)
        self.movable(self.speed)
        self.collision()
        self.collectible()
        self.enemy()
