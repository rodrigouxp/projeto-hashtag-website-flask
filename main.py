# Python v3.10.4
# Flask v2.1.2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/contato')
def conato():
    return 'Qualquer dúvida mande um e-mail para lalalala@gmail.com'

if __name__ == '__main__':
    app.run(debug=True)
