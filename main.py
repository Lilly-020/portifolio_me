from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    pass

@app.route("/inicio")
def inicio():
    pass

@app.route("/animation")
def animation():
    pass

@app.route("/laptop")
def laptop():
    pass