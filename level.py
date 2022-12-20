import pygame
import sys
from config import *
from tile import Tile, MovableTiles
from player import Player
from enemy import Enemy


# generates level, collects all groups here
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = CameraGroupSortY()
        self.obstacle_sprites = pygame.sprite.Group()
        self.collectible_sprites = pygame.sprite.Group()
        self.movable_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.create_map()

    # go through array and generate world based on that, later replace by cvs reader to import form TILED maps
    def create_map(self):
        for row_i, row in enumerate(WORLD_MAP):
            for col_i, col in enumerate(row):
                x = col_i * TILE_SIZE
                y = row_i * TILE_SIZE
                # CLass((x,y), [list of groups sprite belongs to], groups to interact with
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'tile')
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites,
                                         self.collectible_sprites, self.movable_sprites, self.enemy_sprites)
                if col == 'h':
                    Tile((x, y), [self.visible_sprites, self.collectible_sprites], 'honey')
                if col == 'w':
                    MovableTiles((x, y), [self.visible_sprites, self.movable_sprites],
                                 self.obstacle_sprites, 'bear')
                if col == 'b':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'bee')
                if col == 'f':
                    Enemy((x, y), [self.visible_sprites, self.enemy_sprites], self.obstacle_sprites)
                if col == 't':
                    Tile((x, y), [self.visible_sprites], 'text')

    def game_over(self): # implement later, just restart to starting position maybe
        pass

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.camera_draw(self.player)
        self.collectible_sprites.update()


# center camera on player while sorting sprites ourselves instead of read order,
# replaces 1st draw function and displays surface here
class CameraGroupSortY(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2(100,300)
        # score text and init
        pygame.font.init()
        self.myFont = pygame.font.SysFont('Comic Sans MS', 30)

    def camera_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        self.texture_surface = self.myFont.render('Beemo honey:' + str(player.score), False, (0, 0, 0))

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.center):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
            self.display_surface.blit(self.texture_surface, (0,0))




