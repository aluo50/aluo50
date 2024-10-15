'''
Alex Luo, Kishi, Eve
SoftDev
2024-10-08
K15 - Analyzing the different forms of server responses of user inputs.

'''
# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

import testmod0
import os

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not.

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    username = session.get('username') #gets session username
    return render_template('login.html', username=username)


@app.route("/auth", methods=['POST'])
def authenticate():
    username = request.form['username']
    if username:
        session['username'] = username
        return render_template('response.html', user=username, form = 'POST')

    else:
        return render_template('login.html')  #response to a form submission

@app.route("/secret")
def secret_key():
    username = session.get('username')
    if username:
        return render_template('response.html', user=username, form ='session')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template('login.html')


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
