import pygame
from whiskers_world.actors.Player import ActionType


class Renderer:
    """This class is responsible for drawing to the screen"""

    def __init__(self, logger):
        """This constructor sets some meaningful values"""
        self._logger = logger
        self._board_x_tiles = 16
        self._board_y_tiles = 16
        self._tile_size = 48
        self._level_data = []
        self._icon_path = "whiskers_world/resources/Steve_01.png"
        self._window_caption = "Whisker's World"

        # Stub out our screen and sprite groups
        self._screen = None
        self._backgrounds = pygame.sprite.Group()
        self._obstacles = pygame.sprite.Group()
        self._players = pygame.sprite.Group()

    def prepare_renderer(self):
        """This method initializes the renderer"""

        # Set the window's icon, size, and title
        pygame.display.set_icon(pygame.image.load(self._icon_path))
        self._screen = pygame.display.set_mode(
            (self._board_x_tiles * self._tile_size,
             self._board_y_tiles * self._tile_size)
        )
        pygame.display.set_caption(self._window_caption)

    def render_frame(self):
        """This method will draw the current frame"""
        self._backgrounds.update()
        self._obstacles.update()
        self._players.update(self._obstacles)

        # Draw all of the sprites to the back buffer
        self._backgrounds.draw(self._screen)
        self._obstacles.draw(self._screen)
        self._players.draw(self._screen)

        # Flip the front and back buffers
        pygame.display.update()

    def get_tile_size(self):
        """This method returns the tile size"""
        return self._tile_size

    def add_to_level_data(self, line):
        """Add this line to the level data"""
        self._level_data.append(line)

    def add_background(self, background):
        """This method will add a background to the renderer"""
        self._backgrounds.add(background)

    def add_obstacle(self, obstacle):
        """This method will add an obstacle to the renderer"""
        self._obstacles.add(obstacle)

    def add_player(self, player):
        """This method will add a player to the renderer"""
        self._players.add(player)

    def move_player(self, player_number, action):
        """This method will move a player according to the desired action"""
        if action == ActionType.MoveLeft:
            self._players.sprites()[player_number].move_left()
        elif action == ActionType.MoveRight:
            self._players.sprites()[player_number].move_right()
        elif action == ActionType.Fall:
            self._players.sprites()[player_number].move_down(self._obstacles)
