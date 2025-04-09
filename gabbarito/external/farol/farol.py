from typing import Dict, List

from rich.console import Console
from rich.progress import track
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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
        # commands.open_new_page(driver, PageName.FAROL.value)
        commands.navigate_to_page(driver, URL_FAROL)
        Console().log(f"Farol page opened: {URL_FAROL}", style="bold green")
    except Exception as e:
        Console().log(f"Error opening Farol page: {e}", style="bold red")
        raise


def _scrape_table(driver: webdriver.Chrome) -> WebElement:  # type: ignore
    """Scrape the table from the farol page.

    Args:
        driver: The Selenium WebDriver instance.

    Returns:
        None
    """
    Console().log("Scraping table from Farol page...", style="bold blue")
    return driver.find_element(By.TAG_NAME, "table")


def _scrape_body_of_table(table: WebElement) -> WebElement:  # type: ignore
    """Scrape the body of the table.

    Args:
        table (WebElement): The table element containing the body.

    Returns:
        WebElement: The tbody element containing the table body.
    """
    Console().log("Scraping body of table...", style="bold blue")
    return table.find_element(By.TAG_NAME, "tbody")


def _scrape_lines_of_table(body_table: WebElement) -> List[WebElement]:  # type: ignore
    """Scrape the lines of the table.

    Args:
        body_table (WebElement): The tbody element containing the table body.

    Returns:
        List[WebElement]: A list of tr elements representing the lines of the table.
    """
    Console().log("Scraping lines of table...", style="bold blue")
    lines = body_table.find_elements(By.TAG_NAME, "tr")
    Console().log(f"Total of lines: {len(lines)}", style="bold green")
    return lines


def _generate_list_json(lines: List[WebElement]) -> List[Dict[str, str]]:  # type: ignore
    """Generate a list of dictionaries containing repairs data from the scraped table.

    Args:
        lines (List[WebElement]): A list of tr elements representing the lines of the table.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing repairs data.
    """

    def extract_celula_circuito(celula: WebElement) -> str:  # type: ignore
        """Extract the text from the div with class 'flex' in the celula."""
        return celula.find_element(By.CLASS_NAME, "flex").text

    def extract_celula_abertura(celula: WebElement) -> str:  # type: ignore
        """Extract the date and time from the celula."""
        c_abertura = celula.find_element(By.CLASS_NAME, "text-center")
        divs = c_abertura.find_elements(By.TAG_NAME, "div")
        date = divs[0].text
        hour = divs[1].text
        return date + " " + hour

    def extract_celula_posicionamento(celula: WebElement) -> str:  # type: ignore
        """Extract the text from the div with class 'read-more' in the celula."""
        div_warp = celula.find_element(By.TAG_NAME, "div")
        divs = div_warp.find_elements(By.TAG_NAME, "div")

        if len(divs) == 5:
            # If the div has 5 elements, click on the 'a' element to expand the div.
            try:
                a = div_warp.find_element(By.TAG_NAME, "a")
                a.click()
            except:
                ...
            finally:
                # Extract the text from the div with class 'read-more'.
                posicionamento = div_warp.find_element(By.CLASS_NAME, "read-more")

                return posicionamento.text

        return ""

    def extract_celula_prox_acao(celula: WebElement) -> str:  # type: ignore
        """Extract the text from the div with class 'text-center' in the celula."""
        div = celula.find_element(By.CLASS_NAME, "text-center")
        return div.text

    json_list = []

    for line in track(lines, description="Extraindo reparos do oi360 ..."):
        celulas = line.find_elements(By.TAG_NAME, "td")
        reparo = {
            "cliente": celulas[0].find_element(By.CLASS_NAME, "pl-1").text,
            "ticket": celulas[1].find_element(By.CLASS_NAME, "text-primary").text,
            "circuito": extract_celula_circuito(celulas[2]),
            "uf": celulas[3].find_element(By.CLASS_NAME, "text-center").text,
            "resumo": celulas[4].find_element(By.CLASS_NAME, "font-bold").text,
            "posto": celulas[5].find_element(By.CLASS_NAME, "text-center").text,
            "abertura": extract_celula_abertura(celulas[9]),
            "posicionamento": extract_celula_posicionamento(celulas[10]),
            "prox_acao": extract_celula_prox_acao(celulas[11]),
        }

        json_list.append(reparo)

    return json_list


def scrape_farol(driver: webdriver.Chrome) -> List[Dict[str, str]]:
    """Scrape the farol page.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing repairs data.
    """
    if not driver:
        Console().log("Erro: driver not initialized.", style="bold red")
        return

    try:
        table = _scrape_table(driver)
        body_table = _scrape_body_of_table(table)
        lines = _scrape_lines_of_table(body_table)
        json_list = _generate_list_json(lines)
        Console().log(f"Total of repairs: {len(json_list)}", style="bold green")
        Console().log("Repairs data extracted successfully.", style="bold green")
        return json_list
    except Exception as e:
        Console().log(f"Error scraping Farol page: {e}", style="bold red")
        raise
