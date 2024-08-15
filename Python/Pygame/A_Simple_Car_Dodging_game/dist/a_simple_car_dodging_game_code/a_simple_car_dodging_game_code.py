
#! Credits: https://coderslegacy.com/python/pygame-tutorial-part-3/

import pygame, sys
from pygame.locals import *
import random, time

#! Initialize the game
pygame.init()

#! Initialize constants
#* Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#* Colors
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
green_color = (0, 255, 0)
black_color = (0, 0, 0)
white_color = (255, 255, 255)

#* Other variables
width = 400
height = 600
speed = 5
score = 0

#* Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black_color)

background = pygame.image.load("AnimatedStreet.png")

#* Setting up sounds
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

#! Create a white screen
display_surface = pygame.display.set_mode((width, height))
display_surface.fill(white_color)
pygame.display.set_caption("A simple car dodging game")

#! Classes and Sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score

        self.rect.move_ip(0, speed)
        if (self.rect.bottom > height):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < width:
            self.rect.move_ip(5, 0)

#! Creating sprites
player_1 = Player()
enemy_1 = Enemy()

#! Creating sprite groups --> enemies and all_sprites
enemies = pygame.sprite.Group()
enemies.add(enemy_1)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_1)
all_sprites.add(enemy_1)

#! Adding user event
increased_speed = pygame.USEREVENT + 1
pygame.time.set_timer(increased_speed, 1000) #! enemy speed is increased every 1000 milliseconds --> very slow speeding process --> to make the game a little easier

#! Game Loop
while True:

    for event in pygame.event.get():

        if event.type == increased_speed:
            speed += 1.5

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.blit(background, (0, 0))
    scores = font_small.render(str(score), True, black_color)
    display_surface.blit(scores, (10, 10))

    #* Moves and re-draws all sprites
    for entity in all_sprites:
        display_surface.blit(entity.image, entity.rect)
        entity.move()

    #* Game over --> executes when the game detect player's and enemy's collision
    if pygame.sprite.spritecollideany(player_1, enemies):

        pygame.mixer.Sound("crash.wav").play()

        display_surface.fill(red_color)
        display_surface.blit(game_over, (30, 250))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(0.5)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)