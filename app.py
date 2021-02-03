from flask import Flask
from flask import render_template, request, redirect, url_for

import requests
import json

from ca import CA_1d

app = Flask(__name__)
GRAPH_URL = None

@app.route('/')
def main():
    return render_template("main.html")

@app.route("/generator/<string:rule>/<string:col>", methods=["POST", "GET"])
def generator1D(rule, col):
    final_json = {
        "url" : None,
        "response" : None
    }

    try:
        generator = CA_1d(int(rule), int(col))
        final_json["url"] = "static/img/generated_ca_{}_{}.png".format(rule, col)
        final_json["response"] = "ok"
    except:
        final_json["response"] = "nok"

    return json.dumps(final_json, indent = 6)


if __name__ == "__main__":
    app.run(debug=True)
