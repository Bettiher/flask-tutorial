from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello!!"


@app.route("/bla/")
def blabla():
    return "Blabla!"
