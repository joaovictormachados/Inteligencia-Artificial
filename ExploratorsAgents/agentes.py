import random
import pygame
from configuracoes import GRID_SIZE, base_position

class Agente(pygame.sprite.Sprite):
    """Classe base para todos os agentes."""

    def __init__(self, env, name, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.env = env
        self.name = name
        self.tipo = tipo
        self.carga = None




class AgenteReativo(Agente):
    """Agente reativo que se move aleatoriamente e coleta qualquer recurso."""

    def __init__(self, env, name, tipo):
        super().__init__(env, name, tipo)
        self.sprite = pygame.image.load('sprites/Attack_1.png')
        self.image = pygame.transform.scale(self.sprite, (128 * 0.7, 128 * 0.7))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (100, 350)


class AgenteEstado(Agente):
    """Agente baseado em estado que evita revisitar áreas."""

    def __init__(self, env, name, tipo):
        super().__init__(env, name, tipo)
        self.sprite = pygame.image.load('sprites/Shutdown.png')
        self.image = pygame.transform.scale(self.sprite, (128 * 0.65, 128 * 0.65))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (75, 150)


class AgenteBaseadoEmObjetivos(Agente):

    def __init__(self, env, name, tipo):
        super().__init__(env, name, tipo)
        self.sprite = pygame.image.load('sprites/Shutdown2.png')
        self.image = pygame.transform.scale(self.sprite, (128 * 0.65, 128 * 0.65))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (325, 100)



