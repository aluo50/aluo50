# Alex Luo
# TummyAKE
# SoftDev
# K18: Serving Looks
# 2024-10-16
# time spent: 0.3 hours

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('mimic.html')

if __name__ == '__main__':
    app.run(debug=True)