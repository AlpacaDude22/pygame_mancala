import pygame

class Pit:
    COLOR = (191, 171, 119)


    def __init__(self, window, pos_x, pos_y, radius):
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius

        pygame.draw.circle(window, self.COLOR, (pos_x, pos_y), radius)


