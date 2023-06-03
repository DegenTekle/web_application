from flask import Flask, render_template, jsonify
from database import load_games_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  games = load_games_from_db()
  return render_template('home.html', games=games)


@app.route("/api/games")
def list_games():
  games = load_games_from_db()
  return jsonify(games)

if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
