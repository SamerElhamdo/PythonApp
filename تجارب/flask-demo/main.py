from flask import Flask

app = Flask(__name__)

@app.route("/index")

def home():
    return "hi samer"



@app.route("/sayhello/<name>")

def say_hello(name):
    return "hello {}".format(name)

app.run()