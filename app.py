from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route("/")
def start():
    s = ""
    for x in range(10):
        r = random.randint(1, 100)
        s += "hi" + str(r) + "\n"
    return s

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

