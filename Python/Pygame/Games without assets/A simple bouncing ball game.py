
#! Credit to the original code (link): https://www.freecodecamp.org/news/pygame-tutorial-build-a-bouncing-game/

#! Platform control:
    #* use arrow keys to move the platform left or right.
    #* the platform moves horizontally based on key input.
    #* ensure the platform stays within the screen's boundaries.
#! Bouncing ball dynamics:
    #* guide the bouncing ball across the screen.
    #* the ball move independently.
    #* the ball bounces off from walls and the platform.
    #* scores each time teh ball successfully bounces off the platform.
#! Scoring system:
    #* acculate points based on successful bounces.
    #* optimize the scoring mechanism for higher scores.
#! Level progression:
    #* advance through levels as your scores reaches milestones.
    #* with every 10 points, you progresses to the next level.
    #* increased difficulty and complexity with each level.
#! Dynamic platform color:
    #* platform colors changes with each level, adding a visual dynamic.
    #* colors are randomly generated uopn reaching a new level.
#! Lives and Game Over mechanism:
    #* avoid letting the ball fall off the screen to maintain lives.   
    #* lives decreases with missed bounces.
    #* Game Over occurs when lives run out, 3 live in total.
    #* after Game Over, restart with three lives and a reseted score (0)

import pygame
import sys
import random

#! Constants
width, height = 800, 600
ball_radius = 20
platform_width, platform_height = 100, 10
fps = 60
#* Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
light_blue = (173, 216, 230)

#! Pygame instances
#* Initialize pygame
pygame.init()

#* Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("A simple bouncing ball game")
font = pygame.font.Font(None, 36)

#* Clock --> to control the frame rate
clock = pygame.time.Clock()

#* Initialize variables for the game
ball_pos = [width // 2, height // 2]
ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]
platform_pos = [width // 2 - platform_width // 2, height - platform_height - 10]
platform_speed = 10
score = 0
lives = 3
current_level = 1
platform_color = orange

#! Creating game screens
def start_screen():
    screen.fill(black)
    show_text_on_screen("A simple bouncing ball game", 50, height // 4)
    show_text_on_screen("Press any key to start...", 30, height // 3)
    show_text_on_screen("You can move the platform with arrow keys.", 30, height // 2)
    pygame.display.flip()
    wait_for_key()

def game_over_screen():
    screen.fill(black)
    show_text_on_screen("Game Over", 50, height // 3)
    show_text_on_screen(f"Your final score: {score}", 30, height // 2)
    show_text_on_screen("Press any key to restart...", 20, height * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def victory_screen():
    screen.fill(black)
    show_text_on_screen("Congratulations!", 50, height // 3)
    show_text_on_screen(f"You've won the game with total score: {score}", 30, height // 2)
    show_text_on_screen("Press any key to exit...", 20, height * 2 // 3)
    pygame.display.flip()
    wait_for_key()

def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_text_on_screen(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, white)
    text_rect = text_render.get_rect(center = (width // 2, y_position))
    screen.blit(text_render, text_rect)

def change_platform_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#! Main game loop
start_screen()
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    keys = pygame.key.get_pressed()

#* Moving the platform
    platform_pos[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * platform_speed
    platform_pos[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * platform_speed

#* Making sure the platform stays within the screen boundaries
    platform_pos[0] = max(0, min(platform_pos[0], width - platform_width))
    platform_pos[1] = max(0, min(platform_pos[1], height - platform_height))

#* Moving the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

#* Bounce off the wall mechanism
    if ball_pos[0] <= 0 or ball_pos[0] >= width:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

#* Check if the ball hits the platform
    if (
        (platform_pos[0] <= ball_pos[0] <= platform_pos[0] + platform_width)
        and
        (platform_pos[1] <= ball_pos[1] <= platform_pos[1] + platform_height)
    ):
        ball_speed[1] = -ball_speed[1]
        score += 1

#* Check if the player advances to the next level
    if score >= current_level * 10:
        current_level += 1
        ball_pos = [width // 2, height // 2]
        ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]
        platform_color = change_platform_color()

#* Check if the ball falls off teh screen
    if ball_pos[1] >= height:
        lives -= 1
        if lives == 0:
            game_over_screen()
            start_screen()
            score = 0
            lives = 3
            current_level = 1
        else:
            ball_pos = [width // 2, height // 2]
            ball_speed = [random.uniform(2, 4), random.uniform(2, 4)]

#! Clear the screen
    screen.fill(black)

#! Drawing the sprites
#* Draw the ball
    pygame.draw.circle(screen, white, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
#* Draw the platform
    pygame.draw.rect(screen, platform_color, (int(platform_pos[0]), int(platform_pos[1]), platform_width, platform_height))

#! Diplaying information on the screen
#* Adjusting the vertical position
    info_line_y = 10
#* Adjusting the spacing
    info_spacing = 75

#* Drawing the score in an orange rectangle at the top left
    score_text = font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect(topleft = (10, info_line_y))
    pygame.draw.rect(screen, orange, score_rect.inflate(10, 5))
    screen.blit(score_text, score_rect)

#* Drawing the level indicator in light-blue rectangle at the top left (next to the score)
    level_text = font.render(f"Level: {current_level}", True, white)
    level_rect = level_text.get_rect(topleft = (score_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, light_blue, level_rect.inflate(10, 5))
    screen.blit(level_text, level_rect)

#* Drawing the lives in red rectangle at the top left (next to the level)
    lives_text = font.render(f"Lives: {lives}", True, white)
    lives_rect = lives_text.get_rect(topleft = (level_rect.topright[0] + info_spacing, info_line_y))
    pygame.draw.rect(screen, red, lives_rect.inflate(10, 5 ))
    screen.blit(lives_text, lives_rect)

#! Update the display
    pygame.display.flip()

#! Controlling the frame rate
    clock.tick(fps)

#! Quit pygame
pygame.quit()