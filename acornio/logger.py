import logging

from enum import StrEnum


class Color(StrEnum):
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"


class CustomFormatter(logging.Formatter):

    COLOR = {
        "DEBUG": Color.MAGENTA,
        "INFO": Color.CYAN,
        "WARNING": Color.YELLOW,
        "ERROR": Color.RED,
        "CRITICAL": Color.RED,
    }

    def format(self, record):
        color = self.COLOR.get(record.levelname, Color.RESET)

        self._style._fmt = self.__color_formating(color=color)
        return super().format(record)

    def __color_formating(self, *, color: str) -> str:
        fmt = color + "{asctime} " + Color.RESET
        fmt += "[🐿️" + Color.GREEN + "AcornIO" + Color.RESET + "] "
        fmt += color + "{levelname}: {message}" + Color.RESET
        return fmt


logging.basicConfig(
    level=logging.INFO,
)

# Logger
log = logging.getLogger("acornio")
bare_log = logging.getLogger("bare")
log.propagate = False
bare_log.propagate = False

# Handlers
console_handler = logging.StreamHandler()
console_handler.setLevel(level=logging.INFO)
log.addHandler(console_handler)
bare_handler = logging.StreamHandler()
bare_log.addHandler(bare_handler)

# Formatters
formatter = CustomFormatter(
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
console_handler.setFormatter(formatter)
bare_formatter = logging.Formatter("{message}", style="{")
bare_handler.setFormatter(bare_formatter)


def print_preamble() -> None:
    bare_log.info(Color.GREEN + r"""
                                ___ ___ 
      __ _  ___ ___  _ __ _ __  |_ _/ _ \
     / _` |/ __/ _ \| '__| '_ \  | | | | |
    | (_| | (_| (_) | |  | | | | | | |_| |
     \__,_|\___\___/|_|  |_| |_||___\___/

                    🐿️acornIO
                ASGI Application Server
    """ + Color.RESET)