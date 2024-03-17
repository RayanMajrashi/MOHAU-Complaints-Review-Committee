from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "Rayan Majrashi"


if __name__ == "__main__":
  print("Running")
  app.run(host="0.0.0.0", debug=True)
