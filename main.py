from flask import Flask, Response, redirect, render_template, request, url_for

import helper

app = Flask(__name__)


@app.route("/")
def index():
    items = helper.get_all()
    return render_template("index.html", items=items)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("deadline")
    category = request.form.get("category")
    description = request.form.get("description")
    helper.add(text, date=date, category=category, description=description)
    return redirect(url_for("index"))


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
