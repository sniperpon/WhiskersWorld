import pygame


class Sky(pygame.sprite.Sprite):
    """This class represents the a sky background tile"""

    def __init__(self, left, top, width, height):
        """This constructor prepares our grass"""
        pygame.sprite.Sprite.__init__(self)

        # Set some values
        color = pygame.Color(0, 200, 200, 0)
        self._left = left
        self._top = top

        # Prepare the image for rendering
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        """This method is called by pygame's group, each frame"""
        self.rect.center = (self._left, self._top)
