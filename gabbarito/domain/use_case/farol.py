from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List

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


def separete_repair_by_posto(repairs: List[Repair]) -> Dict[str, List[Repair]]:
    """Separate repairs by posto.

    Args:
        repairs (List[Repair]): List of Repair objects.
    """
    repairs_by_posto = defaultdict(list)

    for repair in repairs:
        repairs_by_posto[repair.posto].append(repair)

    return dict(repairs_by_posto)


def filter_repairs_by_postos(repairs: List[Repair], postos: List[str]) -> List[Repair]:
    """
    Filters the repairs by specific postos.

    Args:
        repairs (List[Repair]): List of Repair objects.
        postos (List[str]): List of desired postos names.

    Returns:
        List[Repair]: Filtered list of repairs belonging to the desired postos.
    """
    return [repair for repair in repairs if repair.posto in postos]


def delete_repairs_by_postos(repairs: List[Repair], postos: List[str]) -> List[Repair]:
    """
    Delete the repairs by specific postos.

    Args:
        repairs (List[Repair]): List of Repair objects.
        postos (List[str]): List of desired postos names.

    Returns:
        List[Repair]: Filtered list of repairs belonging to the desired postos.
    """
    return [repair for repair in repairs if not repair.posto in postos]


def ordenar_reparos_por_posto(
    reparos: List[Repair], ordem_postos: List[str]
) -> List[Repair]:
    """
    Ordena os reparos com base em uma ordem específica de postos.

    Args:
        reparos (List[Repair]): Lista de objetos Repair.
        ordem_postos (List[str]): Lista indicando a ordem desejada dos postos.

    Returns:
        List[Repair]: Lista ordenada de reparos.
    """
    # Cria um mapa que atribui um peso para cada posto com base na ordem desejada
    prioridade = {posto: i for i, posto in enumerate(ordem_postos)}

    # Ordena os reparos com base no peso atribuído ao posto
    reparos_ordenados = sorted(
        reparos,
        key=lambda reparo: prioridade.get(
            reparo.posto, float("inf")
        ),  # Default para postos fora da ordem
    )

    return reparos_ordenados


def ordenar_por_data(reparos: List[Repair]) -> List[Repair]:
    """
    Ordena os reparos pelo atributo 'prox_acao', que contém a data no formato 'DD/MM/YYYY HH:MM'.

    Args:
        reparos (List[Repair]): Lista de objetos Repair.

    Returns:
        List[Repair]: Lista de objetos Repair ordenados por data.
    """

    # Define uma função de chave para converter a data de string para datetime
    def extrair_data(reparo):
        try:
            return datetime.strptime(reparo.prox_acao, "%d/%m/%Y %H:%M")
        except:
            return datetime.strptime("01/01/2000 00:00", "%d/%m/%Y %H:%M")

    # Ordena os reparos com base na data de abertura
    return sorted(reparos, key=extrair_data)


def atualizar_cor_prox_acao(reparos: List[Repair]) -> List[Repair]:
    """
    Atualiza a cor da próxima ação (cor_prox_acao) com base no tempo restante até 'prox_acao'.
    As cores são definidas assim:
    - Amarelo: Falta menos de 1 hora.
    - Laranja: Falta menos de 15 minutos.
    - Vermelho: Tempo já passou.

    Args:
        reparos (List[Repair]): Lista de objetos Repair para atualizar.
    """
    agora = datetime.now()

    for reparo in reparos:
        # Converter a string `prox_acao` para um objeto datetime
        try:
            data_prox_acao = datetime.strptime(reparo.prox_acao, "%d/%m/%Y %H:%M")
        except:
            data_prox_acao = datetime.strptime("01/01/2000 00:00", "%d/%m/%Y %H:%M")

        # Calcula a diferença de tempo
        diferenca = data_prox_acao - agora

        # Atualiza a cor com base no tempo restante
        if diferenca < timedelta(minutes=0):
            reparo.next_action_color = "0"  # Já passou
        elif diferenca <= timedelta(minutes=15):
            reparo.next_action_color = "1"  # Menos de 15 minutos
        elif diferenca <= timedelta(hours=1):
            reparo.next_action_color = "2"  # Menos de 1 hora
        elif diferenca <= timedelta(days=1):
            reparo.next_action_color = "3"  # Menos de 1 hora
        else:
            reparo.next_action_color = "4"  # Ainda está longe (opcional)

    return reparos
