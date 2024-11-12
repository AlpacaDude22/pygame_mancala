import pygame
import time
from . import pit

class Board:
    BROWN_BOARD = (255, 225, 150)
    
    def __init__(self, window, pos_x, pos_y, scale, columns): #TODO:make columns and pit_spacing optional with default being 6
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scale = scale
        self.pit_radius = scale * 5
        self.pit_spacing = scale * 1
        self.columns = columns

    def draw_board(self):
        ANIMATE_TIME_STEP = 0.03
        window_w = self.window.get_width()
        window_h = self.window.get_height()


        #Draw board surface
        rect = (window_w/2 - self.pos_x - (self.pit_radius * self.columns), window_h/2 - self.pos_y, self.pit_radius * self.columns * 2, 200)
        pygame.draw.rect(self.window, self.BROWN_BOARD, rect)

        #Draw Pits
        _pit_x = (window_w/2 - ((self.pit_radius * (self.columns - 1)) + (((self.columns -1)/2) * self.pit_spacing)))
        _pit_y = (window_h/2) - self.pos_y
        _bank_spacing = window_w/2 - ((self.pit_radius * (self.columns - 1)) + (((self.columns -1)/2) * self.pit_spacing))

        #Draw top row
        for pit_count in range(0, self.columns): 
            #time.sleep(ANIMATE_TIME_STEP)

            pit.Pit(self.window, _pit_x, (_pit_y - self.pit_radius - (self.pit_spacing/2)), self.pit_radius)
            _pit_x = _pit_x + (self.pit_radius * 2) + self.pit_spacing

            #pygame.display.flip()

        #Draw Bank Right
        _bank_radius = self.pit_radius * 2
        pit.Pit(self.window, _pit_x + self.pit_radius, _pit_y, _bank_radius)

        #Draw bottom row
        _pit_x = _pit_x - ((self.pit_radius * 2) + self.pit_spacing)
        for pit_count in range(0, self.columns):
            #time.sleep(ANIMATE_TIME_STEP)

            pit.Pit(self.window, _pit_x, (_pit_y + self.pit_radius + (self.pit_spacing/2)), self.pit_radius)
            _pit_x = _pit_x - ((self.pit_radius * 2) + self.pit_spacing)

            #pygame.display.flip()     

        #Draw Bank Right
        _bank_radius = self.pit_radius * 2
        pit.Pit(self.window, _pit_x - self.pit_radius, _pit_y, _bank_radius)

        #pygame.display.flip()     




        


