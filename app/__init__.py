from flask import Flask, render_template

from app.game import Game
from app.game_loops import game_loop

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    pass
