import logging
from termcolor import colored


class ColorLogger(logging.Logger):
    """
    A logger that prints colored messages
    """
    def __init__(self, name):
        """
        Initializes the logger and color map
        """
        super().__init__(name)
        self.color_map = {
            'DEBUG': 'grey',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'magenta'
        }

    def _log(
            self,
            level,
            msg,
            args,
            exc_info=None,
            extra=None,
            stack_info=False
    ):
        """
        Logs a message with a color
        """
        if self.isEnabledFor(level):
            msg = colored(msg, self.color_map[level])
            super()._log(level, msg, args, exc_info, extra, stack_info)


class LogHandler:
    """
    A class that handles logging
    """

    def __init__(self, name: str):
        """
        Initializes the logger
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.DEBUG)

        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.handler.setFormatter(self.formatter)

        self.logger.addHandler(self.handler)
