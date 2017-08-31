import sys
import pygame
from whiskers_world.actors.Player import Player
from whiskers_world.actors.Player import ActionType
from whiskers_world.actors.Obstacle import Obstacle
from whiskers_world.actors.Sky import Sky


class Game:
    """This is the main driver class for the simulator"""

    def __init__(self, renderer, input_handler):
        """Initialize pygame"""
        pygame.init()
        self._clock = pygame.time.Clock()

        # Get hooks to our dependencies
        self._renderer = renderer
        self._input_handler = input_handler

        # Set some values which we'll need later
        self._level_file_path = "whiskers_world/resources/level.dat"

        # Prepare the renderer
        self._renderer.prepare_renderer()

        # Load the board from disk
        self._load_file()

    def run(self):
        """This method contains the main game loop"""
        while 1:
            # Regulate the frame rate to 60 frames per second
            self._clock.tick(60)

            # Update object statuses based on input
            self._process_input()

            # Draw the frame
            self._renderer.render_frame()

    def _process_input(self):
        """This method will return the input that the user has inputted"""

        # Make the player so that it's always falling, per gravity
        self._renderer.move_player(0, ActionType.Fall)

        # Is the player moving left?
        if self._input_handler.should_move_left():
            self._renderer.move_player(0, ActionType.MoveLeft)

        # Is the player moving right?
        if self._input_handler.should_move_right():
            self._renderer.move_player(0, ActionType.MoveRight)

        # Also read pygame's events to look for typed input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Escape quits
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _load_file(self):
        """This method will load a file from disk, and add sprites to groups"""
        current_left = self._renderer.get_tile_size() / 2
        current_top = self._renderer.get_tile_size() / 2

        # For now, hardcode a single, large background tile
        self._renderer.add_background(Sky(384, 384, 768, 768))

        # Open a handle to the lawn file, loop through each line
        with open(self._level_file_path, "r") as file:
            for line in file:
                new_line = []

                # Loop through each character in the line and append it
                for character in line:
                    new_line.append(character)

                    # If the character is a player, then add to the group
                    if character == "P":
                        self._renderer.add_player(
                            Player(current_left, current_top)
                        )

                    # If the character is a grass block, then add to the group
                    if character == "G":
                        self._renderer.add_obstacle(
                            Obstacle(current_left, current_top)
                        )

                    # We're done with a character
                    current_left += self._renderer.get_tile_size()

                # We're done with a line
                current_left = self._renderer.get_tile_size() / 2
                current_top += self._renderer.get_tile_size()

                # Append the new line to the yard data
                self._renderer.add_to_level_data(new_line)
