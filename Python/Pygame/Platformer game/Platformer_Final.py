
#! Credits to the creator: https://coderslegacy.com/python/pygame-platformer-game-development/

import pygame, sys, random
from pygame.locals import *


pygame.init()

#! Initialize variables

vec = pygame.math.Vector2
#* This is the default setting
# height = 450
# width = 400
height = 950
width = 900
acceleration = 0.5
friction = -0.12
fps = 60
FramePerSec = pygame.time.Clock()

display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer game")

#! Creating classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("snowman.png")
        self.surf = pygame.Surface((30, 30)) #* creating a small block as the player
        self.surf.fill((128, 255, 40)) #* filling the block with green color
        self.rect = self.surf.get_rect(center = (10, 420)) #* getting the rect and the starting position of the player

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -acceleration
        if pressed_keys[K_RIGHT]:
            self.acc.x = acceleration

        self.acc.x += self.vel.x * friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)

        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if player_1.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self):
        hits = pygame.sprite.spritecollide(player_1, platforms, False)
        if hits:
            self.vel.y = -15

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50, 100), 12))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center = (random.randint(0, width - 10), 
                                                 random.randint(0, height - 30)))

    def move(self):
        pass

platform_1 = platform()
player_1 = Player()

#! Creating sprite groups
platform_1.surf = pygame.Surface((width, 20))
platform_1.surf.fill((255, 0, 0))
platform_1.rect = platform_1.surf.get_rect(center = (width / 2, height - 10))

all_sprites = pygame.sprite.Group()
all_sprites.add(platform_1)
all_sprites.add(player_1)

platforms = pygame.sprite.Group()
platforms.add(platform_1)

#! Level generation

for x in range(random.randint(5, 6)):
    pl = platform()
    platform.add(pl)
    all_sprites.add(pl)

#! Game loop here
while True:
    if player_1.rect.top <= height / 3:
        player_1.pos.y += abs(player_1.vel.y)
        for plat in platforms:
            plat.rect.y += abs(player_1)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_1.jump()

    display_surface.fill((0, 0, 0))
    player_1.update()

    for entity in all_sprites:
        display_surface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(fps)

