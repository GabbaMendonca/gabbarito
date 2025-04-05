from rich.console import Console
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
    if not driver:
        Console().log("Erro: driver not initialized.", style="bold red")
        return

    try:
        commands.open_new_page(driver, PageName.FAROL.value)
        commands.navigate_to_page(driver, URL_FAROL)
        Console().log(f"Farol page opened: {URL_FAROL}", style="bold green")
    except Exception as e:
        Console().log(f"Error opening Farol page: {e}", style="bold red")
        raise
