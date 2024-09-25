heading = '''
Alex Luo <br>
ADD <br>
SoftDev <br>
K09 -- Display occupations at random on the loopback interface from the occupations csv file <br>
2024-09-23 <br>
Time spent: 0.3 <br>
'''

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")

def randfxn():
    f = open("occupations.csv", "r").read()
    f = f.split("\n")[1:-1] # Turns data into list
    
    flist = []
    
    for i in f:
        i = i.split(",")[:-1] # Turns list elements into sublists while getting rid of the percentages
        i = ",".join(i).replace('"',"") # Sublists are joined back into strings while extra "" are removed
        flist.append(i)
    
    print(__name__)
    num = random.randint(0, len(flist)-2) # Needs to exclude the "Total" name

    fstring = "Occupations List: <br><br>"

    for i in flist[:-1]: # Turns the list into a string
        fstring += i + "<br>"

    return heading + "<br> " + fstring + "<br>Random Occupation:<br> " + flist[num]

app.run()
