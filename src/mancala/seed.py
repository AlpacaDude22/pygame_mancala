
from . import pit
import pygame

class Seed:

    COLOR = (0, 0, 255)
    BLACK = (0, 0, 0)

    def __init__(self, Pit, pos_x, pos_y):
        self.Pit = Pit
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = self.Pit.radius * 0.3
        self.outline_w = 4
        pass

    def draw_seed(self):
        pygame.draw.circle(self.Pit.window, self.COLOR, (self.pos_x, self.pos_y), self.radius)
        pygame.draw.circle(self.Pit.window, self.BLACK, (self.pos_x, self.pos_y), self.radius, self.outline_w)