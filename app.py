from flask import Flask, jsonify
from uuid import uuid4

app = Flask(__name__)


@app.route("/")
def uuid():
    return {"uuid": str(uuid4())}


if __name__ == '__main__':
    # Only used when running locally
    app.run(host='localhost', port=8080, debug=True)
