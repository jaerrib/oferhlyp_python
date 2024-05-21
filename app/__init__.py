from flask import Flask, render_template, redirect, session

from app.game import Game

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
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
            "active_row": game.active_row,
            "active_col": game.active_col,
        }
    return render_template("index.html", data=session["data"])


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    session["data"]["active_row"] = row
    session["data"]["active_col"] = col
    return render_template("index.html", data=session["data"])


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")
