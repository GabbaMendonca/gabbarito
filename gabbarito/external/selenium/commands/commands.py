from rich.console import Console
from selenium import webdriver


def open_new_page(driver: webdriver.Chrome, page_name: str) -> None:
    """Open a new page in the browser with the given name.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        page_name (str): The name to assign to the new page.

    Returns:
        None
    """
    driver.execute_script(f"window.open('about:blank','{page_name}');")
    driver.switch_to.window(page_name)
    Console().log(f"New page opened with name: {page_name}")


def navigate_to_page(driver: webdriver.Chrome, url: str) -> None:
    """Navigate to the specified URL in the current browser window.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        url (str): The URL to navigate to.

    Returns:
        None
    """
    driver.get(url)
    driver.switch_to.window(driver.current_window_handle)
    Console().log(f"Navigated to URL: {url}")


def replace_current_page(driver: webdriver.Chrome, page_name: str) -> None:
    """Switch to the browser window with the specified page name.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        page_name (str): The name of the page to switch to.

    Returns:
        None
    """
    driver.switch_to.window(page_name)
    Console().log(f"Switched to page: {page_name}")
