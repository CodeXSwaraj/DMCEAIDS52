# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Azure! This is a simple Flask app hosted on Azure.'

if __name__ == '__main__':
    app.run(debug=True)
