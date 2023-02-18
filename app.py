import os

from flask import Flask, render_template, request, session
import to_paint, subprocess

app = Flask(__name__)

app.secret_key = '28bee993c5553ec59b3c051d535760198f6f018ed1cca1ddadcdb570352ef05b'

APP_ROOT = "C:/Users/user/Documents/IT/dynamic_systems/site/"

@app.route('/')
def main():
    return render_template("main.html")

@app.route('/calc')
def calc():
    return render_template("calc.html")

@app.route('/tables', methods=["POST", "GET"])
def tables():
    val = session.get("gen")
    if val:
        os.remove(APP_ROOT + f'static/others/answer_for_{val}.png')
        session["gen"] = None
    if request.method == "POST":
        mod = request.form["module"]
        try:
            mod = int(mod)
        except:
            return render_template("painted.html", type=0)
        if mod > 200:
            return render_template("painted.html", type=1)
        tab = to_paint.paint(mod=mod)
        cmd = f"./static/others/Math.exe {mod} {mod} 60 length"
        session["gen"] = mod
        subprocess.run(cmd)
        return render_template("painted.html", type=2, data=tab, order=[i for i in range(mod)], link=f"others/answer_for_{mod}.png")
    return render_template("painted.html")

@app.route("/materials")
def mat():
    return render_template("materials.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()
