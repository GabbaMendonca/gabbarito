from flask import Flask, render_template

from gabbarito.domain.use_case import farol
from gabbarito.domain.use_case.driver import get_driver_use_case

app = Flask(__name__)


def run_flask() -> None:
    app.run()


@app.route("/", methods=["GET"])
def hello_world():
    driver = get_driver_use_case()
    grid = farol.scrape_repairs_use_case(driver)
    return render_template("index.html", grid=grid)
