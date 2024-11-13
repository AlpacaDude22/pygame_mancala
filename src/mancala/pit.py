import pygame
import random
from . import seed

class Pit:
    COLOR = (191, 171, 119)


    def __init__(self, window, pos_x, pos_y, radius):
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius


    def draw_pit(self):
        pygame.draw.circle(self.window, self.COLOR, (self.pos_x, self.pos_y), self.radius)

    def add_seed(self):
        random_lbound = round(self.radius * -0.5)
        random_ubound = round(self.radius * 0.5)
        random_offset_x = random.randint(random_lbound, random_ubound)
        random_offset_y = random.randint(random_lbound, random_ubound)
        seed_1 = seed.Seed(self, self.pos_x + random_offset_x, self.pos_y + random_offset_y)
        seed_1.draw_seed()
        


