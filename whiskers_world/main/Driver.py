import argparse
from whiskers_world.main.Logger import Logger
from whiskers_world.graphics.Renderer import Renderer
from whiskers_world.input.InputHandler import InputHandler
from whiskers_world.main.Game import Game


class Driver:
    """This class bootstraps everything so we're ready to go"""

    def __init__(self):
        """This constructor initializes the class appropriately"""
        self._prepare_args()
        self._prepare_logger()

    def _prepare_args(self):
        """This private method preps the args parser"""
        args_parser = argparse.ArgumentParser(
            description="This program will execute the game")

        # Add the mode argument
        args_parser.add_argument("mode",
                                 choices=[
                                     "demo",
                                     "play"
                                 ],
                                 help="Indicate the execution mode")

        # Parse whatever the user has sent in
        self._args = args_parser.parse_args()

    def _prepare_logger(self):
        """This private method will get the logger up and running"""
        self._logger = Logger()

    def drive(self):
        """This method is the logical entry point for the class"""
        if self._args.mode == "demo":
            self._logger.write_to_log("Executing in demo mode")

            # Execute the game in demo mode

        if self._args.mode == "play":
            self._logger.write_to_log("Executing in play mode")

            # Execute the game in play mode
            game = Game(
                Renderer(self._logger), InputHandler(self._logger)
            )
            game.run()

        # Close the logger now that we're done
        self._logger.close_log()
