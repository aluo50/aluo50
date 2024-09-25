# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # determine names of app

@app.route("/")                # :routes" the app to / ?
def hello_world():
    print(__name__)            # prints the "__name__" in the terminal
    return "No hablo queso!"   # text returned on the website

app.run()                      # runs actual app
                
