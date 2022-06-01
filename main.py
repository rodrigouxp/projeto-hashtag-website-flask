# Python v3.10.4
# Flask v2.1.2
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/contato')
def conato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
