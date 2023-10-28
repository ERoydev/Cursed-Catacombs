import pygame
from constants import *
from character import Character

clock = pygame.time.Clock()
pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cursed Catacombs")

# Create Player

player = Character(100, 100)

# main game Loop
run = True
while run:
    clock.tick(FPS)
    win.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

