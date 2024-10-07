
# Danny Mok
# Cerulean Calm: Danny, Alex, Colyi
# SoftDev
# Sep 2024

from flask import Flask, render_template
import csv
import random
app = Flask(__name__)

    
occupations = [] #list and dict for occupations

with open("data/occupations.csv", "r") as file:
    f = csv.reader(file)
    next(f) # skips first row     
    for line in f:
        if len(line) == 3:
            job, percentage, link = line
            job = job.replace('"', '') #removes extra quotes
            occupations.append({
                'job': job,
                'percentage' : float(percentage),
                'link': link
            })

@app.route("/")
def fxn():
    random_occupation = random.choice(occupations)
    return render_template( 'tablified.html', random_occupation = random_occupation, occupations = occupations)

if __name__ == "__main__":
    app.debug = True
    app.run()

app.run()