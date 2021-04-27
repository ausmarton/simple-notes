from flask import Flask
app = Flask(__name__)

notes_db = []
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status')
def status():
    return 'Up'

@app.route('/note')
def get_note():
    return print_list(notes_db)

@app.route('/note', methods=['POST'])
def post_note():
    notes_db.append("a")
    return print_list(notes_db)

def print_list(list):
    output = ""
    for item in list:
        output = output + "," + str(item)
    return output.strip(",")