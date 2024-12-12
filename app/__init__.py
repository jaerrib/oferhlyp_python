from flask import Flask, redirect, render_template, session

from app.game import Game
from app.game_loops import assign_selected, select_token

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
            "active_token": None,
        }
    return render_template("index.html", data=session["data"])


@app.route("/process/<int:row>/<int:col>")
def process(row, col):
    # Check if the selected board position contains a token belonging to the player
    if (
        session["data"]["board"][row][col] != 0
        and session["data"]["board"][row][col]["player"]
        == session["data"]["active_player"]
    ):
        session["data"] = select_token(session["data"], row, col)
    elif (
        session["data"]["active_token"] is not None and not session["data"]["game_over"]
    ):
        session["data"] = assign_selected(session["data"], row, col)
    return render_template("index.html", data=session["data"])


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")
