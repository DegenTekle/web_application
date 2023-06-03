from flask import Flask, render_template, jsonify
from database import load_games_from_db, load_game_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  games = load_games_from_db()
  return render_template('home.html', games=games)


@app.route("/game/<id>")
def show_game_history(id):
  game = load_game_from_db(id)
  if not game:
    return "Not Found", 404
  else:
    return render_template('gamehistory.html',game=game)



if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
