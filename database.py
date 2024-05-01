import psycopg2
import psycopg2.extras
import os

DB_URL = os.environ['DB_CONNECTION_STRING']

def load_companies_from_db():
  Companies = []
  try:
    conn = psycopg2.connect(DB_URL)
    SQL = "SELECT * FROM Company"
    with conn:
      with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as curs:
          curs.execute(SQL)
          for row in curs:
            Companies.append(dict(row))
    conn.close()
    return Companies
  except psycopg2.OperationalError as e:
    return e
    return Companies

def load_company_from_db(id):
  company = []
  try:
    conn = psycopg2.connect(DB_URL)
    print("Connection to the database successful")
    SQL = "SELECT * FROM Company where id = %s"
    data = (id,)
    with conn:
      with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as curs:
           curs.execute(SQL,data)
           if curs.rowcount == 0:
            return None
           else:
            for row in curs:
             company.append(dict(row))  
    conn.close()
    return company
  except psycopg2.OperationalError as e:
    return e
    return company

def add_company_to_db(data):
  try:
    conn = psycopg2.connect(DB_URL)
    SQL = "INSERT INTO Company (name, license_number, commercial_register, owners,start_date, communication_numbers, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (data['name'], data['license_number'], data['commercial_register'], data['owners'], data['start_date'], data['communication_numbers'], data['email'])
    with conn:
      with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as curs:
             curs.execute(SQL,data)
    # conn.commit()
    curs.close()
    conn.close()
    return True
  except psycopg2.OperationalError as e:
      # print("Unable to connect to the database:", e)
      return False,e