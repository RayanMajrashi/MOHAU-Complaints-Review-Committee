import psycopg2
import psycopg2.extras
import os

DB_URL = os.environ['DB_CONNECTION_STRING']

def load_companies_from_db():
  Companies = []
  try:
    conn = psycopg2.connect(DB_URL)
    print("Connection to the database successful")
    SQL = "SELECT * FROM Company"
    with conn:
      with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as curs:
          curs.execute(SQL)
          for row in curs:
            Companies.append(dict(row))
    conn.close()
    return Companies
  except psycopg2.OperationalError as e:
    print("Unable to connect to the database:", e)
    return Companies
  