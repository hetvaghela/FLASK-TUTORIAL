from flask import Flask,url_for
app = Flask(__name__)

@app.route('/hello/<s>')
def hello_world(s):
    return s

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('hello_world', s='het'))

if __name__=="__main__":
    app.run(debug=True)
