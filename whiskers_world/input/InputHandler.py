import pygame


class InputHandler:
    """This class reads keyboard input and returns relevant values"""

    def __init__(self, logger):
        """Set some initial values"""
        self._logger = logger

    def should_move_left(self):
        """This method determines if the player wants to move left"""
        result = pygame.key.get_pressed()[pygame.K_LEFT]

        # Is the player pressing left?
        if result:
            self._logger.write_to_log("Left input press")

        # Return the result
        return result

    def should_move_right(self):
        """This method determines if the player wants to move right"""
        result = pygame.key.get_pressed()[pygame.K_RIGHT]

        # Is the player pressing right?
        if result:
            self._logger.write_to_log("Right input press")

        # Return the result
        return result
