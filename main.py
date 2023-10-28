import pygame
from constants import *
from character import Character

pygame.init()

# clock for maintaining frame rate
clock = pygame.time.Clock()

# Window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cursed Catacombs")

# define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False


# Helper function to scale image
def scale_img(image, scale):
    w = image.get_width()
    h = image.get_height()

    return pygame.transform.scale(image, (w * scale, h * scale))

# load sprites
animation_types = ["idle", "run"]
animation_list = []
for animation in animation_types:
    # reset temporary list of images
    temp_list = []
    for i in range(4):
        img = pygame.image.load(f"assets/assets/images/characters/elf/{animation}/{i}.png").convert_alpha()
        img = scale_img(img, SCALE)
        temp_list.append(img)
    animation_list.append(temp_list)

# Create Player
player = Character(100, 100, animation_list)

# main game Loop
run = True
while run:
    # Frame rate control
    clock.tick(FPS)

    # window color to remove last player position
    win.fill(BG)

    # Calculate player movement
    dx, dy = 0, 0
    if moving_right:
        dx = VELOCITY
    if moving_left:
        dx = -VELOCITY
    if moving_up:
        dy = -VELOCITY
    if moving_down:
        dy = VELOCITY

    # Move player
    player.move(dx, dy)

    # Update player
    player.update()

    # Draw player on screen
    player.draw(win)

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Take keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True

        # Keyboard button released logic
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()


pygame.quit()

