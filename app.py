from flask import Flask, render_template
import random 

app = Flask(__name__)

@app.route("/")
def start():
    s = random.randint(2, 20)
    s = f"hi  -  {s}"
    return s

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

