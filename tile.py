import pygame


# base static tile draw, can assign groups based on function, obstacle, visible, collectible etc
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, name):
        super().__init__(group)
        self.name = name
        self.dir = pygame.math.Vector2()

        # different images as tiles
        if self.name == 'tile':
            self.image = pygame.image.load('graphics/testtile.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, 0)
        if self.name == 'honey':
            self.image = pygame.image.load('graphics/honey.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, 0)
        if self.name == 'bee':
            self.image = pygame.image.load('graphics/beemo.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, -20)
        if self.name == 'text':
            self.image = pygame.image.load('graphics/beemotext.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)


# same as Tile but instead makes it movable, implement collision later so you can move it and jump on it, eg boxes
class MovableTiles(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites, name):
        super().__init__(group)
        self.name = name
        self.dir = pygame.math.Vector2()
        self.obstacle_sprites = obstacle_sprites
        self.gravity = 0.8
        if self.name == 'bear':
            self.image = pygame.image.load('graphics/whitebear.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)

    def collision(self):
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.dir.x < 0:
                    self.rect.left = sprite.rect.right
                if self.dir.x > 0:
                    self.rect.right = sprite.rect.left
                if self.dir.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.dir.y = 0
                if self.dir.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.dir.y = 0

    def update(self):
        self.collision()