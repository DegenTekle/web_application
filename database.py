from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING'] 

engine = create_engine(db_connection_string,connect_args={"ssl":{"ssl_ca":"/etc/ssl/cert.pem"}})

def load_games_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from games"))
    games = []
    for row in result.mappings():
      games.append(dict(row))
    return games

def load_game_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM games WHERE id={id}"))
    rows = []
    column_name = result.keys()
    for rowi in result.all():
      rows.append(dict(zip(column_name, rowi)))
    if len(rows) == 0:
      return None
    else:
      return (rows[0])