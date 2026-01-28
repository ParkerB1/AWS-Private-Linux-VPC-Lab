#!/usr/bin/env python3
from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello():
    html_content = """
    <html>
        <body style="background-color:black; color:white; font-family:monospace; white-space:pre;">
Hello, World!
Testing CI/CD
        </body>
    </html>
    """
    return Response(html_content, mimtype="text/html")

if __name__ == "__main__":
    # Listen on all interfaces (0.0.0.0) and port 8080
    app.run(host="0.0.0.0", port=8080)