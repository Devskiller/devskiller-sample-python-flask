from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/add/<int:a>/<int:b>/", methods=["GET"])
def add(a, b):
    pass


@app.route("/subtract/<int:a>/<int:b>/", methods=["GET"])
def subtract(a, b):
    pass


@app.route("/multiply/<int:a>/<int:b>/", methods=["GET"])
def multiply(a, b):
    pass


@app.route("/divide/<int:a>/<int:b>/", methods=["GET"])
def divide(a, b):
    pass


if __name__ == "__main__":
    app.run(debug=True)
