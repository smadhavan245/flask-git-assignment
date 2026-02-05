from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Running from Tutedude branch"

@app.route("/api")
def api():
    with open("data.json") as f:
        return jsonify(json.load(f))

@app.route("/todo")
def todo():
    return render_template("todo.html")

if __name__ == "__main__":
    app.run(debug=True)
