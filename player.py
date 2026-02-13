import pygame
import utils

class Player:

    def __init__(self, size, color, pos):
        self.SIZE = size
        self.COLOR = color
        self.pos = pos
        self.vel_x = 0
        self.vel_y = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, self.pos , self.SIZE)


    def move(self, dt):

        acceleration = 25
        resistance = 0.05
        max_spd = 3

        #velocity dampening
        self.vel_y += self.vel_y * -resistance
        self.vel_x += self.vel_x * -resistance

        # changing velocity on input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vel_y -= acceleration * dt
        if keys[pygame.K_s]:
            self.vel_y += acceleration * dt
        if keys[pygame.K_a]:
            self.vel_x -= acceleration * dt
        if keys[pygame.K_d]:
            self.vel_x += acceleration * dt

        #setting boundary of velocity
        self.vel_x = utils.clamp_f(self.vel_x, -max_spd, max_spd)
        self.vel_y = utils.clamp_f(self.vel_y, -max_spd, max_spd)

        # converting velocity to pixel movement
        self.pos = (self.pos[0] + self.vel_x, self.pos[1] + self.vel_y)


