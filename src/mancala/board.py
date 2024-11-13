import pygame
import time
from . import pit

class Board:
    BROWN_BOARD = (255, 225, 150)
    SOWING_DELAY = 0.5
    pit_list = []
    #seed_sound = pygame.mixer.Sound("\media\plop-fancade.mp3")

    
    def __init__(self, window, pos_x, pos_y, scale, columns): #TODO:make columns and pit_spacing optional with default being 6
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scale = scale
        self.pit_radius = scale * 5
        self.pit_spacing = scale * 1
        self.columns = columns

    def draw_board(self):
        ANIMATE_TIME_STEP = 0.25
        window_w = self.window.get_width()
        window_h = self.window.get_height()


        #Draw board surface
        rect_x = window_w/2 + self.pos_x - (self.pit_spacing * 1.5) - (self.pit_radius * 4) - (self.pit_radius * self.columns) - + (self.pit_spacing * self.columns * 0.5)
        rect_y = window_h/2 - (self.pit_spacing * 1.5) - (self.pit_radius * 2) - self.pos_y
        rect_w = (self.pit_spacing * 3) + (self.pit_radius * 8) + (self.pit_radius * 2 * self.columns) + (self.pit_spacing * self.columns)
        rect_h = (self.pit_radius * 4) + (self.pit_spacing * 3)
        rect = (rect_x, rect_y, rect_w, rect_h)
        pygame.draw.rect(self.window, self.BROWN_BOARD, rect, 0, 125)

        #Draw Pits
        _pit_x = (window_w/2) + (self.pit_radius * (self.columns - 1)) + (self.pit_spacing * (self.columns * 0.5 - 0.5))
        _pit_y = (window_h/2) - self.pos_y
        _bank_spacing = window_w/2 - ((self.pit_radius * (self.columns - 1)) + (((self.columns -1)/2) * self.pit_spacing))

        #Draw top row
        for pit_count in range(0, self.columns): 
            #time.sleep(ANIMATE_TIME_STEP)

            _pit_temp = pit.Pit(self.window, _pit_x, (_pit_y - self.pit_radius - (self.pit_spacing/2)), self.pit_radius)
            _pit_temp.draw_pit()
            self.pit_list.append(_pit_temp)
            _pit_x = _pit_x - ((self.pit_radius * 2) + self.pit_spacing)

            #pygame.display.flip()

        #Draw Bank Right
        _bank_radius = self.pit_radius * 2
        _bank_1 = pit.Pit(self.window, _pit_x - self.pit_radius, _pit_y, _bank_radius)
        _bank_1.draw_pit()
        self.pit_list.append(_bank_1)

        #Draw bottom row
        _pit_x = _pit_x + ((self.pit_radius * 2) + self.pit_spacing)
        for pit_count in range(0, self.columns):
            #time.sleep(ANIMATE_TIME_STEP)

            _pit_temp = pit.Pit(self.window, _pit_x, (_pit_y + self.pit_radius + (self.pit_spacing/2)), self.pit_radius)
            _pit_temp.draw_pit()
            self.pit_list.append(_pit_temp)
            _pit_x = _pit_x + ((self.pit_radius * 2) + self.pit_spacing)

            #pygame.display.flip()     

        #Draw Bank Right
        _bank_radius = self.pit_radius * 2
        _bank_2 = pit.Pit(self.window, _pit_x + self.pit_radius, _pit_y, _bank_radius)
        _bank_2.draw_pit()
        self.pit_list.insert(0, _bank_2)



    def fill_board(self, seeds_per_pit, animation):
        _bank_1 = 0
        _bank_2 = self.columns + 1

        for index, Pit in enumerate(self.pit_list):
            if index == _bank_1 or index == _bank_2:
                continue
            if animation:
                pygame.display.flip()   
                time.sleep(self.SOWING_DELAY)
            
            Pit.add_seed()

  




        


