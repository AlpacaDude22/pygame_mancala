import pygame
import sys
import time
import mancala




pygame.init()
pygame.mixer.init()

WINDOW_W, WINDOW_H = 1200, 800
WHITE = (255, 255, 255)
SCALE = 10
PIT_SPACING = 1 * SCALE
PIT_RADIUS = 5 * SCALE
NUM_OF_COLUMNS = 6 #TODO MIN 1 
NUM_OF_START_SEEDS = 4 #TODO MIN 1 

window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("LAN Mancala")

window.fill(WHITE)

board = mancala.board.Board(window, 0, 200, SCALE, NUM_OF_COLUMNS) #(0, 0) is the center of the screen
board.draw_board()
board.fill_board(NUM_OF_START_SEEDS, True)

pygame.display.flip()


for Pit in board.pit_list:
    print(Pit.radius)


#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False