#coding: utf-8
from flask import import render_template,Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)

