from flask import Flask, jsonify, request
from app.cody import run_code

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"name": "Cody"})


@app.route("/api/v1/cody", methods=["GET", "POST"])
def run():
    data = request.get_json()

    language = data.get("language")
    code = data.get("code")

    if not language and not code:
        return jsonify({"error": "Please provide the language & code parameters"}), 400

    output = run_code(language, code)
    return jsonify(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)