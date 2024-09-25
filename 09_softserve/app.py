'''
Alex Luo
ADD
SoftDev
K09 -- Display occupations at random on the loopback interface from the occupations csv file
2024-09-23
time spent: 1.2
'''

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")

def randfxn():
    f = open("occupations.csv", "r").read()
    f = f.split("\n")[1:-1]
    
    print(len(f))
    flist = []
    
    for i in f:
        i = i.split(",")[:-1]
        i = ",".join(i).replace('"',"")
        flist.append(i)
    
    print(__name__)
    num = random.randint(0, len(flist)-1)
    return flist[num]

app.run()