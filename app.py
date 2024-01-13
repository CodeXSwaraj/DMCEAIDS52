from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Azure! This is a simple Flask app hosted on not Azure.'

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(debug=True, port=5000)

