from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route("/")
def start():
    for x in range(10):
        x += x
    return str(x)

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

