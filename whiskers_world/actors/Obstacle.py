import pygame


class Obstacle(pygame.sprite.Sprite):
    """This class represents an obstacle"""

    def __init__(self, left, top):
        """This constructor will prepare the obstacle for usage"""
        pygame.sprite.Sprite.__init__(self)

        # Set the tree's location
        self._left = left
        self._top = top

        # Load the image and set the rectangle
        self.image = pygame.image.load("whiskers_world/resources/Grass.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        """This method is called by pygame's group, each frame"""
        self.rect.center = (self._left, self._top)
