from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello():
    return "Hello!!"


@app.route("/bla")
def blabla():
    return "Blabla!"


@app.route("/api", methods=['POST'])
def increment_age():
    if request.method == 'POST':
        data = request.form.to_dict()
        data['age'] = float(data.get('age', 0))
        data['age_plus_one'] = data.get('age') + 1
        return jsonify(data)


# data = pd.DataFrame({'name': ['lili', 'jules'], 'age': [12, 30]})
# data.to_json(orient='records')
