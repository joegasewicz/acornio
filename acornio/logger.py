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
log.propagate = False

# Handlers
console_handler = logging.StreamHandler()
log.addHandler(console_handler)

# Formatters
formatter = logging.Formatter(
    color_formating(),
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
console_handler.setFormatter(formatter)
