from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "API is running successfully"
    })


@app.route("/users")
def users():
    return jsonify([
        {
            "id": 1,
            "name": "Raj",
            "city": "Chennai"
        },
        {
            "id": 2,
            "name": "Anita",
            "city": "Bangalore"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
