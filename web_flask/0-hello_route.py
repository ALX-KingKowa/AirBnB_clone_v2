#!/usr/bin/python3
""" Web application using Flask Framework """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Funcion that displays a text """
    return 'HELLO HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
