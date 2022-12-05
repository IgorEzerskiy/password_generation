from flask import Flask
from function import generate

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)