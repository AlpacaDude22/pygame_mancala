import pygame
import sys
from mancala import pit




pygame.init()

WINDOW_W, WINDOW_H = 650, 200
WHITE = (255, 255, 255)
PIT_SPACING = 10
PIT_RADIUS = 50

window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("LAN Mancala")

window.fill(WHITE)

#Draw Pits
_pit_spacing = 0
for pit_count in range(0, 6):

    pit.Pit(window, _pit_spacing, PIT_RADIUS , PIT_RADIUS)
    pit.Pit(window, _pit_spacing, (PIT_RADIUS * 2) + PIT_SPACING, PIT_RADIUS)
    _pit_spacing = _pit_spacing + (PIT_RADIUS * 2) + PIT_SPACING




pygame.display.flip()








#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False