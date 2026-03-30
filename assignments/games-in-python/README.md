
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a command-line Hangman game to practice core Python concepts such as loops, conditionals, string manipulation, and user input handling.

## 📝 Tasks

### 🛠️ Build the Game Setup

#### Description
Create the initial game setup, including a word list, random word selection, and variables for tracking guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Randomly select one word for each new game.
- Initialize a display showing hidden letters using underscores (for example, `_ _ _ _`).
- Set a fixed number of incorrect guesses allowed (for example, 6 attempts).

### 🛠️ Implement the Guessing Loop

#### Description
Implement the main loop where the player enters one letter at a time, the game updates progress, and win/lose conditions are checked.

#### Requirements
Completed program should:

- Ask the user to enter a single letter on each turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only when the guessed letter is not in the word.
- End the game with a win message when all letters are revealed.
- End the game with a lose message when attempts reach 0, and show the correct word.
