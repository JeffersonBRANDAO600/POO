from flask import Flask 

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Hello World! aqui é Jefferson testando flask'

app.run()