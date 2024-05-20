from flask import Flask, render_template, redirect, session

from app.game import Game
from app.game_loops import game_loop

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
    if "data" in session:
        session.pop("data")
    if "data" not in session:
        game = Game()
        game.active_player = 2
        session["data"] = {
            "board": game.board.data,
            "move_list": game.move_list,
            "jumped_list": game.jumped_list,
            "active_player": game.active_player,
            "game_over": game.game_over,
            "turn_over": game.turn_over,
        }
    return render_template("index.html", data=session["data"])


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    return redirect("/")


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")
