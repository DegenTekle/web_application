from flask import Flask, render_template, jsonify

app = Flask(__name__)

GAMES = [{
  'id': 1,
  'winner': "David",
  'score': '300'
}, {
  'id': 2,
  'winner': "Greg",
  'score': '450'
},{
  'id': 3,
  'winner': "Marie",
  'score': '980'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', games=GAMES)


@app.route("/api/games")
def list_jobs():
  return jsonify(GAMES)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
