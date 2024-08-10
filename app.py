from flask import Flask, render_template 
import random 

app = Flask(__name__)

@app.route("/")
def start():
    return "mmm" + str(random.randint(1, 1000))

@app.route("/mbsa")
def mbsa():
    return render_template('index.html')

