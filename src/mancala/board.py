import pygame
import time
from . import pit

class Board:
    COLOR = (50, 50, 50)


    def __init__(self, window, pos_x, pos_y, pit_radius, pit_spacing, columns): #TODO:make columns and pit_spacing optional with default being 6
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pit_radius = pit_radius
        self.columns = columns

        ANIMATE_TIME_STEP = 0.03
        #Draw Pits
        window_w = window.get_width()
        window_h = window.get_height()
        
        _pit_spacing = window_w/2 - ((pit_radius * (columns - 1)) + (((columns -1)/2) * pit_spacing))
        _bank_spacing = window_w/2 - ((pit_radius * (columns - 1)) + (((columns -1)/2) * pit_spacing))
        for pit_count in range(0, columns):
            time.sleep(ANIMATE_TIME_STEP)

            pit.Pit(window, _pit_spacing, pit_radius , pit_radius)
            _pit_spacing = _pit_spacing + (pit_radius * 2) + pit_spacing

            pygame.display.flip()

        _pit_spacing = _pit_spacing - ((pit_radius * 2) + pit_spacing)
        for pit_count in range(0, columns):
            time.sleep(ANIMATE_TIME_STEP)

            pit.Pit(window, _pit_spacing, pit_radius + (pit_radius * 2) + pit_spacing, pit_radius)
            _pit_spacing = _pit_spacing - ((pit_radius * 2) + pit_spacing)

            pygame.display.flip()       



        


