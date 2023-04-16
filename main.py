from flask import Flask, render_template, jsonify

app = Flask(__name__)

GAMES = [{
  'id': 1,
  'title': "Player 1 has won",
  'score': '3-0'
}, {
  'id': 2,
  'title': "Player 1 has won",
  'score': '2-1'
}]
SCORES = [{'David': 300}, {'Greg': 450}, {'Marie': 980}]


@app.route("/")
def hello_world():
  return render_template('home.html', games=GAMES, scores=SCORES)


@app.route("/api/SCORES")
def list_jobs():
  return jsonify(SCORES)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
