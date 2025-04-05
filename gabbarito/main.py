# gabbarito/main.py
from rich.prompt import Prompt

from .domain.use_case import farol
from .domain.use_case.driver import close_driver_use_case, get_driver_use_case


def main():
    # inicialize
    driver = get_driver_use_case()
    farol.open_farol_use_case(driver)
    Prompt.ask(
        "Press Enter to continue after the page has loaded.",
        default="",
        show_default=False,
    )
    # # up flask server

    # # scrape in route /
    # data = farol.scrape_farol(driver)
    # from pprint import pprint

    # pprint(data)
    Prompt.ask(
        "Press Enter to close the browser and exit the program.",
        default="",
        show_default=False,
    )
    close_driver_use_case(driver)
