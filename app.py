from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route("/")
def start():
    for x in range(10):
        s = f"hi - {random.randint(1, 100} \n"
        s += s
    return s

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

