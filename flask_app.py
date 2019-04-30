import pandas as pd

from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello!!"


@app.route("/bla")
def blabla():
    return "Blabla!"


@app.route("/api")
def data_jsonify():
    data = pd.DataFrame([{'name': 'lili', 'age': 12}, {'name': 'jules', 'age': 30}])
    return data.to_json(orient='records')  # return jsonify({'a': 1, 'b': 2})
