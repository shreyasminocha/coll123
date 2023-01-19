from flask import Flask, request, render_template, flash, session
from stockfish import Stockfish
import chess
import chess.engine
import chess.svg
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

engine = chess.engine.SimpleEngine.popen_uci("stockfish", timeout=30)


@app.route("/", methods=["GET", "POST"])
def index():
    board = chess.Board()

    if request.method == "GET":
        fen = request.cookies.get("fen")

        if not fen:
            fen = board.fen()
            return (
                render_template("index.html", game=chess.svg.board(board, size=300)),
                {"set-cookie": f"fen={fen}"},
            )

        try:
            board.set_fen(fen)
        except:
            flash("Invalid position — you're not trying something naughty, are you?")
            board.reset()
            return (
                render_template("index.html", game=chess.svg.board(board, size=300)),
                {"set-cookie": f"fen={board.fen()}"},
            )

        if board.is_game_over():
            flash("GG, but you must win to get the flag")
            board.reset()
            return (
                render_template("index.html", game=chess.svg.board(board, size=300)),
                {"set-cookie": f"fen={board.fen()}"},
            )

        return render_template("index.html", game=chess.svg.board(board, size=300))

    if request.method == "POST":
        session.clear()

        move = request.form.get("move", "")
        fen = request.cookies.get("fen")

        try:
            board.set_fen(fen)
        except:
            flash("Invalid position — you're not trying something naughty, are you?")
            board.reset()
            return (
                render_template("index.html", game=chess.svg.board(board, size=300)),
                {"set-cookie": f"fen={board.fen()}"},
            )

        try:
            board.push_san(move)
        except:
            flash("Invalid move")
            return render_template("index.html", game=chess.svg.board(board, size=300))

        if board.is_game_over():
            if board.is_checkmate() and board.outcome().winner == chess.WHITE:
                return open("flag.txt").read()
            else:
                flash("GG, but you must win to get the flag")
                board.reset()
                return (
                    render_template(
                        "index.html", game=chess.svg.board(board, size=300)
                    ),
                    {"set-cookie": f"fen={board.fen()}"},
                )

        result = engine.play(board, chess.engine.Limit(time=0.5))
        board.push(result.move)

        if board.is_game_over():
            flash("GG, but you must win to get the flag")
            board.reset()
            return (
                render_template("index.html", game=chess.svg.board(board, size=300)),
                {"set-cookie": f"fen={board.fen()}"},
            )

        return render_template("index.html", game=chess.svg.board(board, size=300)), {
            "set-cookie": f"fen={board.fen()}"
        }
