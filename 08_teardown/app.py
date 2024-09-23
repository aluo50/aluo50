# Alex Luo

'''
DISCO:
 - flask is a python framework used for web dev
 @app.route("/") is a route to handle http requests at the url
 app.run starts the flask server

QCC:
0. I have seen similar syntax in python functions.
1. The / also represents the root directory in file systems.
2. It will print to the terminal
3.  It will print "__main__"
4. It will be sent back to the client when accessing the /
5. I have seen similar constructs in java
 ...

INVESTIGATIVE APPROACH:
First we pip installed flask and activated a virtual isolated environment.
After the instillation, we read the output in the terminal that consisted of flask and it's dependencies.
Flask uses a WSGI, an HTML renderer(Jinja2), itsdangerous, click.
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?