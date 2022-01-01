import pandas as pd
from flask import Flask, jsonify
from pandas.io.parsers import read_csv

app = Flask(__name__)
data = pd.read_csv(
    "/Users/gabrielsantos/my-first-python-api/my-first-python-api/data/username-password-recovery-code.csv"
)

# API FUNCTIONS
@app.route("/")
def homepage():
    return "API Running"


@app.route("/location")
def location():
    for row in data.iterrows():  # iterate over the rows
        data_push = {"location_list": row["Location"]}
        return jsonify(data_push)


@app.route("/total_salary")
def total_salary():
    data_push = {"total_salary": int(data["Salary"].sum())}
    return jsonify(data_push)


# RUN API
app.run()
