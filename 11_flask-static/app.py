# Alex Luo
# TummyAKE
# Clyde 'Thluffy' Sinclair
# SoftDev
# Sep 2024

# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

with open('static/fixie.html', 'r') as f:
    html_string = f.read()

'''
@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

'''

@app.route("/static/fixie.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(html_string)


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
