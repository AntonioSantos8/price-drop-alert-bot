from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route("/")
def home():

    data = []

    with open("prices.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return render_template("index.html", data=data)

app.run(debug=True)