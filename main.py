from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.abspath("templates"), static_folder=os.path.abspath("static"))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/inicio")
def inicio():
    return render_template('inicio.html')

@app.route("/play")
def play():
    return render_template('play.html')

@app.route("/animation")
def animation():
    return render_template('note_animacao.html')

if __name__ == '__main__':
    app.run(debug=True)