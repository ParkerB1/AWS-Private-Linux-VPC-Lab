#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!<br>Testing CI/CD"

if __name__ == "__main__":
    # Listen on all interfaces (0.0.0.0) and port 8080
    app.run(host="0.0.0.0", port=8080)
