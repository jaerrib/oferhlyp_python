from flask import Flask, redirect, render_template, session

from app.game import Game
from app.game_loops import (
    assign_selected,
    select_token,
    get_available_moves,
    turn_reset,
    get_jumped_position,
    assign_jump,
)

app = Flask(__name__)
app.secret_key = "dev"


@app.route("/")
def index():
    if "data" not in session:
        game = Game()
        game.active_player = 1
        session["data"] = {
            "board": game.board.data,
            "move_list": game.move_list,
            "jumped_list": game.jumped_list,
            "active_player": game.active_player,
            "game_over": game.game_over,
            "active_row": game.active_row,
            "active_col": game.active_col,
            "active_token": None,
            "actively_jumping": False,
            "possible_moves": [],
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
        session["data"]["possible_moves"] = get_available_moves(
            session["data"], (col, row)
        )
    elif (
        session["data"]["active_token"] is not None and not session["data"]["game_over"]
    ):
        move_position = (col, row)
        if (
            move_position in session["data"]["possible_moves"]["possible_moves"]
            and session["data"]["actively_jumping"] == False
        ):
            session["data"] = assign_selected(session["data"], row, col)
            session["data"] = turn_reset(session["data"])
        elif move_position in session["data"]["possible_moves"]["possible_jumps"]:
            session["data"] = assign_jump(
                session["data"],
                move_position,
                col=session["data"]["active_col"],
                row=session["data"]["active_row"],
            )
    return render_template("index.html", data=session["data"])


@app.route("/reset")
def reset():
    session.pop("data")
    return redirect("/")


@app.route("/end-turn")
def end_turn():
    session["data"] = turn_reset(session["data"])
    session["data"]["actively_jumping"] = False
    return redirect("/")
