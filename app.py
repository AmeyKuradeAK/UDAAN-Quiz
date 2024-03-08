# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Viewer</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a basic HTML content displayed using Flask.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
