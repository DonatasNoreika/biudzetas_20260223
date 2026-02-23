from flask import Flask, render_template, request
import pendulum

app = Flask(__name__)


@app.route("/")
def index():
    zmones = ['Tomas', "Laura", "Rokas"]
    return render_template("index.html", zmones=zmones)

@app.route("/data/", methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        metai, menuo, diena = request.form['data'].split("-")
        data = pendulum.date(int(metai), int(menuo), int(diena))
        diff = data.diff(pendulum.today())
        return render_template('result.html', data=data, diff=diff)
    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True)
