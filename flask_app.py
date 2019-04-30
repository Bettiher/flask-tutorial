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
    data = [{"col 1": "a", "col 2": "b"}, {"col 1": "c", "col 2": "d"}]
    return jsonify(data)
