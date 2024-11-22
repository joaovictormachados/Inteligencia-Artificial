import pygame
from configuracoes import GRID_SIZE, CELL_SIZE, GREEN, RED, BLUE

def desenhar_grid(screen):
    """Desenha o grid e os recursos."""
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.rect(
                screen, (200, 200, 200), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )
