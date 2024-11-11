import pygame
import sys
from mancala import pit




pygame.init()

WINDOW_W, WINDOW_H = 1000, 800
WHITE = (255, 255, 255)
PIT_SPACING = 110
PITS_START_LOC = 200

window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("LAN Mancala")

window.fill(WHITE)

#Draw top
_pit_spacing = PITS_START_LOC
for pit_count in range(0, 6):

    pit.Pit(window, _pit_spacing, 100)
    _pit_spacing = _pit_spacing + PIT_SPACING



pygame.display.flip()








#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False