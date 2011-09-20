# -*- coding: utf-8 -*-

from flask import Flask

application = Flask(__name__)
app = application

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

