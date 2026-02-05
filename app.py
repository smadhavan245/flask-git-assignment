from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   return "Flask App Running from Tutedude branch"

if __name__ == "__main__":
    app.run(debug=True)
