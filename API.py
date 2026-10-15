from flask import Flask, jsonify, request
import os

app = Flask(__name__)

users = [
    {"id": 1, "name": "Raj", "city": "Chennai"},
    {"id": 2, "name": "Anita", "city": "Bangalore"}
]

@app.route("/")
def home():
    return jsonify({"message": "API is running successfully"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    body = request.get_json()
    if not body:
        return jsonify({"error": "No data provided"}), 400
    new_user = {
        "id": len(users) + 1,
        "name": body.get("name"),
        "city": body.get("city")
    }
    users.append(new_user)
    return jsonify({"message": "User created", "user": new_user}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    body = request.get_json()
    user["name"] = body.get("name", user["name"])
    user["city"] = body.get("city", user["city"])
    return jsonify({"message": "User updated", "user": user}), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users.remove(user)
    return jsonify({"message": f"User {user_id} deleted successfully"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
