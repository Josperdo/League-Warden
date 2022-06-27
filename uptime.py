from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return 'League is a threat to our friend group. It must be exterminated'

def run():
    app.run(host="0.0.0.0", port=8080)

def upTime():
    server = Thread(target=run)
    server.start()