from flask import Flask
from threading import Thread
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def run():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()
    time.sleep(2)
    t.join()
