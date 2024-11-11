import pygame

class Pit:
    COLOR = (50, 50, 50)


    def __init__(self, window, pos_x, pos_y, radius):
        self.window = window
        pygame.draw.circle(window, self.COLOR, (pos_x, pos_y), radius)
