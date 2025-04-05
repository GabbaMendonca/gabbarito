import os

from rich.console import Console
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from gabbarito.load_config import PATH_PERFIL_CHROME

# Global variable to store the driver instance
driver_instance = None


def get_chrome_driver() -> webdriver.Chrome:
    """Configure and get the driver for Chrome.

    Returns:
        webdriver.Chrome: An instance of the Chrome WebDriver.
    """
    # For atualizing the Chrome version
    # https://googlechromelabs.github.io/chrome-for-testing/#stable
    # Current version: 135.0.7049.42
    global driver_instance

    # If the driver instance already exists, return it
    if driver_instance is not None:
        return driver_instance

    # Get the current directory path
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Build the driver path
    driver_path = os.path.join(
        current_directory,
        "chromedriver-win64",
        "chromedriver.exe",
    )

    Console().log(f"Loading Chrome driver from: {driver_path}")

    # Set up Chrome options
    options = Options()
    options.add_argument(f"user-data-dir={PATH_PERFIL_CHROME}")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-gpu")
    service = ChromeService(executable_path=driver_path)
    try:
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        Console().log(f"Error loading Chrome driver: {e}", style="bold red")
        raise

    return driver


def close_driver(driver: webdriver.Chrome) -> None:
    """Close the Selenium driver.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance to close.

    Returns:
        None
    """
    if driver is not None:
        Console().log("Closing Selenium driver...")
        driver.quit()
        global driver_instance
        driver_instance = None
        Console().log(
            f"Driver closed successfully from path: {
                os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "chromedriver-win64",
                "chromedriver.exe",
                )
            }"
        )
    else:
        Console().log("Driver is already closed or not initialized.")
