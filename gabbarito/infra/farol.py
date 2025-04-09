from typing import List

from gabbarito.domain.entitie.repair import Repair
from gabbarito.external.farol.farol import open_farol, scrape_farol


def open_farol_infra(driver):
    """Open the farol page using the Selenium driver."""
    open_farol(driver)


def _convert_to_repairs(data: List[dict]) -> List[Repair]:
    """Convert raw data to a list of Repair objects."""
    return [
        Repair(
            cliente=item["cliente"],
            ticket=item["ticket"],
            circuito=item["circuito"],
            uf=item["uf"],
            resumo=item["resumo"],
            posto=item["posto"],
            abertura=item["abertura"],
            posicionamento=item["posicionamento"],
            prox_acao=item["prox_acao"],
        )
        for item in data
    ]


def scrape_repairs_infra(external, driver) -> List[Repair]:
    """Scrape the farol page using the Selenium driver."""
    raw_data = external(driver)
    return _convert_to_repairs(raw_data)
