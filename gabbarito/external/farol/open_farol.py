from selenium import webdriver

from gabbarito.external.selenium.commands import commands
from gabbarito.external.selenium.commands.page_name import PageName
from gabbarito.load_config import URL_FAROL


def open_farol(driver: webdriver.Chrome) -> None:
    """Open the farol page.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None
    """
    commands.open_new_page(driver, PageName.FAROL.value)
    commands.navigate_to_page(driver, URL_FAROL)
