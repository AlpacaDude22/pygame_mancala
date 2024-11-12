import pygame
import sys
import time
import mancala




pygame.init()

WINDOW_W, WINDOW_H = 1000, 700
WHITE = (255, 255, 255)
PIT_SPACING = 10
PIT_RADIUS = 15
NUM_OF_COLUMNS = 20 #TODO MIN 1 

window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("LAN Mancala")

window.fill(WHITE)
pygame.display.flip()

mancala.board.Board(window, 0, 0, PIT_RADIUS, PIT_SPACING, NUM_OF_COLUMNS)















#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False