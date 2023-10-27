import pygame
from constants import *
from character import Character
from weapon import Weapon

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

# Load Weapon Images
bow_image = scale_img(pygame.image.load("assets/assets/images/weapons/bow.png").convert_alpha(), WEAPON_SCALE)
arrow_image = scale_img(pygame.image.load("assets/assets/images/weapons/arrow.png").convert_alpha(), WEAPON_SCALE)

# Load Character Images
mob_animations = []
mob_types = ["elf", "imp", "skeleton", "goblin", "muddy", "tiny_zombie", "big_demon"]
animation_types = ["idle", "run"]

for mob in mob_types:
    animation_list = []
    for animation in animation_types:
        # reset temporary list of images
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f"assets/assets/images/characters/{mob}/{animation}/{i}.png").convert_alpha()
            img = scale_img(img, SCALE)
            temp_list.append(img)
        animation_list.append(temp_list)

    mob_animations.append(animation_list)

# Create Player
player = Character(100, 100, mob_animations, 0)

# Create Player Weapon
bow = Weapon(bow_image, arrow_image)

# Create sprite groups
arrow_group = pygame.sprite.Group()

# Main Game Loop
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
    arrow = bow.update(player)
    if arrow:
        arrow_group.add(arrow)

    # Draw player on screen
    player.draw(win)
    bow.draw(win)
    for arrow in arrow_group:
        arrow.draw(win)

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

