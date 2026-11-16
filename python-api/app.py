from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"service": "python-api", "status": "UP"})


if __name__ == "__main__":
    
