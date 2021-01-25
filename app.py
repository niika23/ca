from flask import Flask
from flask import render_template, request, redirect, url_for

import requests

from ca import CA_1d

app = Flask(__name__)


@app.route('/')
def main():
    graph_url = None
    return render_template("main.html", graph_url=graph_url)

@app.route('/a')
def after_gen():
    graph_url = "static/img/generated_ca.png"
    print(graph_url)
    return render_template("main.html", graph_url=graph_url)


@app.route("/generator1d", methods=["POST", "GET"])
def generator1D():
    if request.method == "GET":
        rule = request.args.get("rule")
        col = request.args.get("col")

        generator = CA_1d(int(rule), int(col))

        return redirect(url_for("after_gen"))

if __name__ == "__main__":
    app.run(debug=True)