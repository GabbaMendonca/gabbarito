from flask import Flask, render_template

import dados_fake
from gabbarito.domain.use_case import farol
from gabbarito.domain.use_case.driver import get_driver_use_case
from gabbarito.external.farol.farol import scrape_farol
from gabbarito.infra.farol import scrape_repairs_infra


def scrape_fake(driver):
    return dados_fake.reparos_fake


app = Flask(__name__)


def run_flask() -> None:
    # app.run(debug=True)
    app.run()


def injector(infra, external):
    def inner_interface(*args, **kwargs):
        return infra(external, *args, **kwargs)

    return inner_interface


@app.route("/", methods=["GET"])
def hello_world():
    driver = get_driver_use_case()
    injection = injector(scrape_repairs_infra, scrape_farol)
    repairs = farol.scrape_repairs_use_case(injection, driver)

    # New repairs
    new_p = ["FCRDE"]
    new = farol.filter_repairs_by_postos(
        repairs,
        new_p,
    )

    # OEMP repairs
    omep_p = ["OEMP"]
    oemp_filter = farol.filter_repairs_by_postos(
        repairs,
        omep_p,
    )
    oemp = farol.ordenar_por_data(oemp_filter)

    # Vtal repairs
    vtal_p = ["TRIAV"]
    vtal_filter = farol.filter_repairs_by_postos(
        repairs,
        vtal_p,
    )
    vtal = farol.ordenar_por_data(vtal_filter)

    # Tade repairs
    tade_p = ["TADE"]
    tade_filter = farol.filter_repairs_by_postos(
        repairs,
        tade_p,
    )
    tade = farol.ordenar_por_data(tade_filter)

    # Limbo repairs
    limbo_p = [
        "CONF",
        "EIAD",
        "REDEA",
        "CB",
        "GETP",
    ]
    limbo_filter = farol.filter_repairs_by_postos(
        repairs,
        limbo_p,
    )
    limbo_by_posto = farol.separete_repair_by_posto(limbo_filter)
    limbo = []
    for posto in limbo_by_posto:
        limbo += farol.ordenar_por_data(limbo_by_posto[posto])

    # Outhes repairs
    outhes_filter = farol.delete_repairs_by_postos(
        repairs,
        new_p + omep_p + vtal_p + tade_p + limbo_p,
    )
    outhes_by_posto = farol.separete_repair_by_posto(outhes_filter)
    outhes = []
    for posto in outhes_by_posto:
        outhes += farol.ordenar_por_data(outhes_by_posto[posto])

    grid = {
        "new": new,
        "oemp": oemp,
        "vtal": vtal,
        "outhes": outhes,
        "tade": tade,
        "limbo": limbo,
    }

    return render_template(
        "index.html",
        grid=grid,
    )
