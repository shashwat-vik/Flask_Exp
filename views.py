from app import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("pretty.html")

@app.route("/basic")
def basic():
    return render_template("basic.html")
