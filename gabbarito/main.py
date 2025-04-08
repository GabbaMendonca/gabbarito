# gabbarito/main.py
from rich.prompt import Prompt

from gabbarito.presenter.init import run_flask

from .domain.use_case import farol
from .domain.use_case.driver import close_driver_use_case, get_driver_use_case


def inicializar_driver():
    """Initialize the driver for the use case.

    Returns:
        WebDriver: The initialized WebDriver instance.
    """
    driver = get_driver_use_case()
    farol.open_farol_use_case(driver)
    Prompt.ask(
        "Press Enter to continue after the page has loaded and grid configured.",
        default="",
        show_default=False,
    )
    return driver


def close_driver(driver):
    """Close the driver for the use case."""
    Prompt.ask(
        "Press Enter to close the browser and exit the program.",
        default="",
        show_default=False,
    )
    close_driver_use_case(driver)


def main():
    # inicialize
    driver = inicializar_driver()

    # Up flask server
    run_flask()

    # Close the browser and exit the program
    close_driver(driver)
