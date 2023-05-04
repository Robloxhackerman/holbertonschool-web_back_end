#!/usr/bin/env python3
from os import getenv

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('0-index.html')

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
