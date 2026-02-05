from flask import Flask, jsonify, request, render_template
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.items

@app.route("/")
def home():
    return "Flask App Running with Frontend and Backend"

@app.route("/todo")
def todo():
    return render_template("todo.html")

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json
    collection.insert_one({
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    })
    return jsonify({"message": "Item stored successfully"})

if __name__ == "__main__":
    app.run(debug=True)
