from flask import Flask, render_template
from database import load_companies_from_db

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("Pages/home.html")


@app.route("/RegisterCompany")
def RegisterCompany():
  return render_template("Pages/RegisterCompany.html")


@app.route("/Companies")
def Companies():
  Companies = load_companies_from_db()
  return render_template("Pages/Companies.html",
                         companies=Companies)


if __name__ == "__main__":
  print("Running")
  app.run(host="0.0.0.0", debug=True)
