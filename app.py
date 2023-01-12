from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Worldllllll!</p>"


@app.route("/test/")
def hello_world2():
    return "<p>Hello</p>"