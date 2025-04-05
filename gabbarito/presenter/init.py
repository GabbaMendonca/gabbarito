from flask import Flask, render_template

from gabbarito.domain.use_case import farol
from gabbarito.domain.use_case.driver import get_driver_use_case
from gabbarito.external.farol.farol import scrape_farol
from gabbarito.infra.farol import scrape_repairs_infra

app = Flask(__name__)


def run_flask() -> None:
    app.run()


def injector(infra, external):
    def inner_interface(*args, **kwargs):
        return infra(external, *args, **kwargs)

    return inner_interface


@app.route("/", methods=["GET"])
def hello_world():
    driver = get_driver_use_case()
    injection = injector(scrape_repairs_infra, scrape_farol)
    grid = farol.scrape_repairs_use_case(injection, driver)
    return render_template("index.html", grid=grid)
