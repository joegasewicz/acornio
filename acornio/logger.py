import logging

from enum import StrEnum


class Color(StrEnum):
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"


def color_formating() -> str:
    fmt = Color.CYAN + "{asctime} " + Color.RESET
    fmt += "[🐿️" + Color.GREEN + "AcornIO" + Color.RESET + "] "
    fmt += Color.CYAN + "{message}" + Color.RESET
    return fmt


logging.basicConfig(
    level=logging.INFO,
)

# Logger
log = logging.getLogger(__name__)
bare_log = logging.getLogger("bare")
log.propagate = False
bare_log.propagate = False

# Handlers
console_handler = logging.StreamHandler()
log.addHandler(console_handler)
bare_handler = logging.StreamHandler()
bare_log.addHandler(bare_handler)

# Formatters
formatter = logging.Formatter(
    color_formating(),
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