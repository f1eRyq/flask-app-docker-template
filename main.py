from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! I am not use Docker'

app.run()