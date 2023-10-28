import math

import constants
import pygame
import constants
import math


class Character:
    def __init__(self, x, y, animation_list):
        self.action = 0  # 0: idle, 1: running
        self.flip = False
        self.animation_list = animation_list
        self.frame_index = 0   # for animations
        self.update_time = pygame.time.get_ticks()    # for animations
        self.running = False
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.image = animation_list[self.action][self.frame_index]


    def move(self, dx, dy):
        self.running = False

        if dx != 0 or dy != 0:
            self.running = True

        # control flip side on player
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        # control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)

        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        #check what action the player is performing
        if self.running:
            self.update_action(1)
        else:
            self.update_action(0)

        animation_cooldown = 70

        #handle animation
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time passed since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        # check if animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if new action is different from current
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)


