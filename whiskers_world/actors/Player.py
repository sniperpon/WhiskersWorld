import pygame


class Player(pygame.sprite.Sprite):
    """This class represents a lawn mower"""

    def __init__(self, left, top):
        """This constructor will prepare the mower for usage"""
        pygame.sprite.Sprite.__init__(self)

        # Set some initial values
        self._left = left
        self._top = top
        self._move_speed = 8
        self._vertical_speed = 4

        # Prepare the mower for rendering
        self._orig_image = pygame.image.load(
            "whiskers_world/resources/Steve_01.png"
        )
        self._orig_image = self._orig_image.convert_alpha()
        self.image = self._orig_image
        self.rect = self.image.get_rect()
        self._bottomed_out = False
        self._undo_method = None

    def update(self, obstacles):
        """This method is called by pygame's group, each frame"""
        if self._check_for_collision(obstacles):
            self._undo_method()

    def move_left(self):
        """This method will move the player to the left"""
        self._left -= self._move_speed

        # How would we undo this?
        self._undo_method = self.move_right

    def move_right(self):
        """This method will move the player to the right"""
        self._left += self._move_speed

        # How would we undo this?
        self._undo_method = self.move_left

    def move_down(self, obstacles):
        """This method will move the player down, if they aren't floored"""
        if not self._bottomed_out:
            self._top += self._vertical_speed

        # How would we undo this?
        self._undo_method = self.move_up

        # Are we colliding as a result of this action?
        if self._check_for_collision(obstacles):
            self._bottomed_out = True

    def move_up(self):
        """This method will move the player up"""
        self._top -= self._vertical_speed

        # How would we undo this?
        self._undo_method = self.move_down

    def _check_for_collision(self, obstacles):
        """This method will check for obstacle collisions"""
        self.rect.center = (self._left, self._top)

        # Are we colliding?
        res = (self._undo_method is not None
               and len(pygame.sprite.spritecollide(self, obstacles, False)) > 0
               )

        # Return the result of the check
        return res


class ActionType:
    """This class serves as an enum for the various player actions"""
    MoveLeft = 0
    MoveRight = 1
    Fly = 2
    Fall = 3
