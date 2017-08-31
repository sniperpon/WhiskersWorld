import time
import os


class Logger:
    """This class handles log output"""

    def __init__(self):
        """This constructor initializes the class"""
        self._file = open("logs/" + str(time.time()) + ".log", "w")

    def write_to_log(self, message):
        """This method will write a line to the log file"""
        self._file.write(message + os.linesep)
        print(message)

    def close_log(self):
        """This method will close the file handle"""
        self._file.close()
