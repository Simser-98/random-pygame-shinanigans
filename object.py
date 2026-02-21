import pygame
import utils
from math import cos, sin


class Object:

    def __init__(self, size, color, pos, vel, func_list):
        self.SIZE = size
        self.COLOR = color
        self.pos = pos
        self.vel = vel
        self.func_list = func_list

    # method is for to be applied to all objects

    # getter method
    def get_obj_velocity(self):
        return self.vel

    def draw_obj(self, screen):
        pygame.draw.circle(screen, self.COLOR, self.pos , self.SIZE)

    def velocity_rotation(self, theta):

        rotation_matrix = [[cos(theta), sin(theta)],
                           [-sin(theta), cos(theta)]]

        self.vel = [self.vel[0] * cos(theta) - self.vel[1] * sin(theta), self.vel[0] * sin(theta) + self.vel[1] * cos(theta)]


# functions are to be applied to only specific objects


def velocity_movement(object, _dt, _kys):

    # converting velocity to pixel movement
    object.pos = (object.pos[0] + object.vel[0], object.pos[1] + object.vel[1])
    
    
def move_player_obj(object, dt, keys):

    acceleration = 1.5
    resistance = 3
    max_spd = 0.5

    #velocity dampening
    object.vel[0] += object.vel[0] * -resistance * dt
    object.vel[1] += object.vel[1] * -resistance * dt


    # changing velocity on input
    if keys[pygame.K_w]:
        object.vel[1] -= acceleration * dt
    if keys[pygame.K_s]:
        object.vel[1] += acceleration * dt
    if keys[pygame.K_a]:
        object.vel[0] -= acceleration * dt
    if keys[pygame.K_d]:
        object.vel[0] += acceleration * dt

    #setting boundary of velocity
    object.vel[0] = utils.clamp_f(object.vel[0], -max_spd, max_spd)
    object.vel[1] = utils.clamp_f(object.vel[1], -max_spd, max_spd)


def update_objects(object, _dt, _keys):

    # deletes bullets that are out of bounds of the window
    if 0 > object.pos[0] or object.pos[0] > 1280 or 0 > object.pos[1] or object.pos[1] > 720:
        del object




