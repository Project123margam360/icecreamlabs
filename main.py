from flask import Flask, send_from_directory
from pathlib import Path

app = Flask(__name__)
IMAGES_DIR = Path(app.root_path) / "images"


@app.route("/")
def home():
    return send_from_directory(app.root_path, "commingsoonpage.html")


@app.route("/comingsoon")
def comingsoon_alias():
    return send_from_directory(app.root_path, "commingsoonpage.html")


@app.route("/commingsoon")
def commingsoon():
    return send_from_directory(app.root_path, "commingsoonpage.html")


@app.route("/design1")
def design1():
    # Serves the existing file in the workspace.
    return send_from_directory(app.root_path, "icecream-slideshow-sections-tv.html")


@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory(IMAGES_DIR, filename)


if __name__ == "__main__":
    app.run(debug=True)
