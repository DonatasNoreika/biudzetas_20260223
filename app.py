from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    zmones = ['Tomas', "Laura", "Rokas"]
    return render_template("index.html", zmones=zmones)


if __name__ == "__main__":
    app.run(debug=True)
