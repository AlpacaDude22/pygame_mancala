import pygame

class Pit:

    RADIUS = 50
    COLOR = (0, 0, 0)


    def __init__(self, window, pos_x, pos_y):
        self.window = window
        pygame.draw.circle(window, self.COLOR, (pos_x, pos_y), self.RADIUS)
