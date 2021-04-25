from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status')
def status():
    return 'Up'

@app.route('/note')
def get_note():
    return 'hi'

@app.route('/note', methods=['POST'])
def post_note():
    return 'here'