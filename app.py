# game_app.py

from flask import Flask, request

app = Flask(__name__)

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        return check_guess(guess)
    return """
    <h1>Guess the Number</h1>
    <form method="post" action="/">
        <label for="guess">Enter your guess (1-10):</label>
        <input type="number" name="guess" required min="1" max="10">
        <button type="submit">Submit Guess</button>
    </form>
    """

def check_guess(guess):
    if guess == secret_number:
        return "Congratulations! You guessed the correct number. <a href='/'>Play Again</a>"
    else:
        return "Wrong guess. Try again! <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
