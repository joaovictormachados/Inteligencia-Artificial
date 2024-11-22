import pygame

class CristalEnergetico(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('sprites/Icon16.png')
        self.image = self.sprite
        self.imageSizeX = 32
        self.imageSizeY = 32
        self.image = pygame.transform.scale(self.image, (self.imageSizeX*1.3, self.imageSizeY*1.3))
        self.rect = self.image.get_rect()
        self.rect.center = 25, 25


class MetalRaro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('sprites/Icon4.png')
        self.image = self.sprite
        self.imageSizeX = 32
        self.imageSizeY = 32
        self.image = pygame.transform.scale(self.image, (self.imageSizeX*1.3, self.imageSizeY*1.3))
        self.rect = self.image.get_rect()
        self.rect.center = 225, 225


class EstruturaAntiga(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load('sprites/Rock_statue_fox_ground_shadow.png')
        self.image = self.sprite
        self.imageSizeX = 64
        self.imageSizeY = 64
        self.image = pygame.transform.scale(self.image, (self.imageSizeX*0.8, self.imageSizeY*0.8))
        self.rect = self.image.get_rect()
        self.rect.center = 325, 275