###faulty code
from flask import Flask, request

app = Flask(__name__)

DB_PASSWORD = "SuperSecretPassword123"


@app.route("/")
def home():
    user = request.args.get("user")

    query = "SELECT * FROM users WHERE username = '" + user + "'"

    return query


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



# from flask import Flask, jsonify

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return jsonify({
#         "application": "security-aspects",
#         "status": "running"
#     })


# @app.route("/health")
# def health():
#     return jsonify({
#         "status": "healthy"
#     })


# @app.route("/users/<int:user_id>")
# def get_user(user_id):
#     return jsonify({
#         "user_id": user_id,
#         "name": f"user-{user_id}"
#     })


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
