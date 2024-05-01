from flask import Flask, render_template, jsonify, request
from database import load_companies_from_db, load_company_from_db, add_company_to_db

app = Flask(__name__)


@app.route("/")
def home():
  return render_template("Pages/home.html")


@app.route("/RegisterCompany", methods=['GET', 'POST'])
def RegisterCompany():
  if request.method == 'POST':
    # Get form data
    company_data = {
        "name":
        request.form['name'],
        "license_number":
        request.form['license_number'],
        "commercial_register":
        request.form['commercial_register'],
        "owners": [
            request.form['owner1'], request.form['owner2'],
            request.form['owner3']
        ],
        "start_date":
        request.form['start_date'],
        "communication_numbers": [
            request.form['communication_number1'],
            request.form['communication_number2'],
            request.form['communication_number3']
        ],
        "email":
        request.form['email']
    }
    result = add_company_to_db(company_data)

    # Check the result of the insertion
    if result is True:
      success_message = "Company inserted successfully."
      return render_template('Pages/RegisterCompany.html',
                             success_message=success_message)
    else:
      error_message = "Failed to insert company: " + str(result)
      return render_template('Pages/RegisterCompany.html',
                             error_message=error_message)

  return render_template("Pages/RegisterCompany.html")


@app.route("/Companies")
def Companies():
  Companies = load_companies_from_db()
  return render_template("Pages/Companies.html", companies=Companies)


@app.route("/Company/<id>")
def show_Company(id):
  company = load_company_from_db(id)
  if not company:
    return "Not Found", 404
  # return render_template("Pages/Company.html", company=company)
  return jsonify(company)


if __name__ == "__main__":
  print("Running")
  app.run(host="0.0.0.0", debug=True)
