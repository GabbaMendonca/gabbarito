from typing import List

from gabbarito.domain.entitie.repair import Repair
from gabbarito.infra.farol import open_farol_infra, scrape_repairs_infra


def open_farol_use_case(driver):
    """Use case to open the farol page.

    Returns:
        None
    """
    open_farol_infra(driver)


def scrape_repairs_use_case(infra, driver) -> List[Repair]:
    """Use case to scrape the farol page.

    Returns:
        List[Repair]: A list of Repair objects containing the scraped data.
    """
    return infra(driver)
