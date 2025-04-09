from gabbarito.external.selenium.driver.chrome import (
    close_chrome_driver,
    get_chrome_driver,
)


def get_driver_infra():
    """Get the Selenium driver.

    Returns:
        The Selenium WebDriver instance.
    """
    return get_chrome_driver()


def close_driver_infra(driver):
    """Close the Selenium driver.

    Args:
        driver: The Selenium WebDriver instance to close.

    Returns:
        None
    """
    close_chrome_driver(driver)
