#app.py
from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def hello():
    return "Ohayoo, World from Flask!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5010)
