# import pygame
# import random
# import simpy
#
# # Configurações do grid
# GRID_SIZE = 20
# CELL_SIZE = 40
# WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
#
# pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("SimPy + Pygame Simulation")
#
# # Cores
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
#
# # Adicionar vários agentes ao ambiente
# class Ambiente:
#     def __init__(self, env, grid_size):
#         self.env = env
#         self.grid_size = grid_size
#         self.agentes = []
#
#     def adicionar_agente(self, agente):
#         self.agentes.append(agente)
#         self.env.process(agente.mover())  # Ativa o processo de movimentação do agente
#
# # Modificar classe Agente para suportar diferentes tipos
# class Agente:
#     def __init__(self, env, posicao, tipo):
#         self.env = env
#         self.posicao = posicao
#         self.tipo = tipo  # Define o tipo do agente (e.g., reativo, baseado em estado)
#
#     def mover(self):
#         while True:
#             dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
#             self.posicao = (max(0, min(self.posicao[0] + dx, GRID_SIZE - 1)),
#                             max(0, min(self.posicao[1] + dy, GRID_SIZE - 1)))
#             yield self.env.timeout(1)  # Aguarda 1 unidade de tempo
#
# def desenhar(agentes):
#     screen.fill(WHITE)
#
#     # Desenhar grid
#     for x in range(0, WIDTH, CELL_SIZE):
#         for y in range(0, HEIGHT, CELL_SIZE):
#             rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
#             pygame.draw.rect(screen, BLACK, rect, 1)
#
#     # Desenhar agente
#     # for agente in agentes:
#     #
#     #     agent_x, agent_y = agente.posicao[0] * CELL_SIZE, agente.posicao[1] * CELL_SIZE
#     #     pygame.draw.rect(screen, GREEN, (agent_x, agent_y, CELL_SIZE, CELL_SIZE))
#     #
#     #     agent_x, agent_y = agente.posicao[0] * CELL_SIZE, agente.posicao[1] * CELL_SIZE
#     #     pygame.draw.rect(screen, GREEN, (agent_x, agent_y, CELL_SIZE, CELL_SIZE))
#     #
#     #     agent_x, agent_y = agente.posicao[0] * CELL_SIZE, agente.posicao[1] * CELL_SIZE
#     #     pygame.draw.rect(screen, GREEN, (agent_x, agent_y, CELL_SIZE, CELL_SIZE))
#
#     agente1 = agentes[0]
#     agente2 = agentes[1]
#     agente3 = agentes[2]
#
#     agent1_x, agent1_y = agente1.posicao[0] * CELL_SIZE, agente1.posicao[1] * CELL_SIZE
#     pygame.draw.rect(screen, RED, (agent1_x, agent1_y, CELL_SIZE, CELL_SIZE))
#
#     agent2_x, agent2_y = agente2.posicao[0] * CELL_SIZE, agente2.posicao[1] * CELL_SIZE
#     pygame.draw.rect(screen, BLUE, (agent2_x, agent2_y, CELL_SIZE, CELL_SIZE))
#
#     agent3_x, agent3_y = agente3.posicao[0] * CELL_SIZE, agente3.posicao[1] * CELL_SIZE
#     pygame.draw.rect(screen, GREEN, (agent3_x, agent3_y, CELL_SIZE, CELL_SIZE))
#
#     pygame.display.flip()
#
# # Inicializar SimPy
# env = simpy.Environment()
# ambiente = Ambiente(env, GRID_SIZE)
#
# # Adicionar agentes de tipos variados
# ambiente.adicionar_agente(Agente(env, (2, 2), "reativo"))
# ambiente.adicionar_agente(Agente(env, (5, 5), "baseado em estado"))
# ambiente.adicionar_agente(Agente(env, (7, 7), "cooperativo"))
#
# # Loop de simulação e renderização
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Atualizar lógica da simulação
#     env.step()
#
#     # Atualizar visualização
#     desenhar(ambiente.agentes)
#
#     pygame.time.delay(50)
# pygame.quit()
#


import pygame
import simpy

from ExploratorsAgents.agentes import AgenteBaseadoEmObjetivos
from ExploratorsAgents.recursos import CristalEnergetico, MetalRaro, EstruturaAntiga
from configuracoes import WINDOW_SIZE, FPS, CELL_SIZE
from mapa import desenhar_grid
from agentes import AgenteReativo, AgenteEstado


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Simulação de Agentes")
    clock = pygame.time.Clock()

    # Inicializar o grid com as posições dos recursos
    def inicializar_grid():
        grid = {}
        # Adicionar os recursos às suas respectivas posições
        for recurso in [CristalEnergetico(), MetalRaro(), EstruturaAntiga()]:
            posicao = (recurso.rect.center[0] // CELL_SIZE, recurso.rect.center[1] // CELL_SIZE)
            grid[posicao] = (type(recurso).__name__, recurso)
        return grid

    env = simpy.Environment()


    reativo = AgenteReativo(env, "Agente 1", "Reativo")
    estados = AgenteEstado(env, "Agente 2", "Estado")
    objetivos = AgenteBaseadoEmObjetivos(env, "Agente3", "Objetivo")

    agentes = [reativo, estados]

    # Instanciando as sprites
    todas_as_sprites = pygame.sprite.Group()
    cristal_energetico = CristalEnergetico()
    metal_raro = MetalRaro()
    estrutura_antiga = EstruturaAntiga()
    todas_as_sprites.add(cristal_energetico)
    todas_as_sprites.add(metal_raro)
    todas_as_sprites.add(estrutura_antiga)
    todas_as_sprites.add(reativo)
    todas_as_sprites.add(estados)
    todas_as_sprites.add(objetivos)


    # env.process(simular(env, agentes))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        desenhar_grid(screen)
        # desenhar_agentes(agentes, screen)
        todas_as_sprites.draw(screen)
        todas_as_sprites.update()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()





