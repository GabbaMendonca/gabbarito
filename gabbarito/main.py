# gabbarito/main.py
from rich.prompt import Prompt

from gabbarito.presenter.init import run_flask

from .domain.use_case import farol
from .domain.use_case.driver import close_driver_use_case, get_driver_use_case


def main():
    # inicialize
    driver = get_driver_use_case()
    farol.open_farol_use_case(driver)
    Prompt.ask(
        "Press Enter to continue after the page has loaded and grid configured.",
        default="",
        show_default=False,
    )

    # Up flask server
    run_flask()

    # Close the browser and exit the program
    Prompt.ask(
        "Press Enter to close the browser and exit the program.",
        default="",
        show_default=False,
    )
    close_driver_use_case(driver)
