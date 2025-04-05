from rich.prompt import Prompt

from gabbarito.external.farol import farol
from gabbarito.external.selenium.driver import chrome


def main():
    driver = chrome.get_chrome_driver()
    farol.open_farol(driver)
    Prompt.ask(
        "Press Enter to continue after the page has loaded.",
        default="",
        show_default=False,
    )
    data = farol.scrape_farol(driver)
    from pprint import pprint

    pprint(data)
    Prompt.ask(
        "Press Enter to close the browser and exit the program.",
        default="",
        show_default=False,
    )
    chrome.close_driver(driver)
