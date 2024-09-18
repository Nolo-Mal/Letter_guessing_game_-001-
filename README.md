## Overview

This is a Python-based Hangman game that challenges players to guess a randomly selected word by inputting missing letters. The game is designed to be interactive and fun, with a limited number of guesses and a visual representation of the hangman figure as incorrect guesses are made.


## Features

- Random Word Selection: Words are chosen randomly from a provided text file.
- Word Completion: A random letter from the selected word is revealed to the player.
- Input Handling: Players input guesses one letter at a time.
- Guess Limit: Players have 5 guesses before the game ends.
- Stick Figure Drawing: A stick figure is drawn with each incorrect guess.
- Quit Option: Players can type "quit" or "exit" to stop the game.


## Game Flow

1.    Word Selection: The program selects a word from a text file. If no file is provided, it defaults to short_words.txt.      

2.    Guessing: The player guesses one letter at a time to complete the word. If the guess is correct, the letter is filled in; otherwise, they lose a guess.

3.    Winning Condition: The player wins if they guess all the letters in the word.

4.    Losing Condition: The game ends if the player runs out of guesses, displaying the correct word.

5.    Exit: Players can exit the game at any time by typing "quit" or "exit."


## How to Play

1. Run the script by using the following command:
`python3 hangman.py`

2. The game will prompt you to guess the missing letters of a randomly selected word.

3. After each guess:

   * If correct, the letter is filled in the word.
   * If incorrect, the number of remaining guesses decreases, and part of the hangman figure is drawn.

4. You can quit the game at any time by typing "quit" or "exit."


## Installation

1. Clone this repository or download the hangman.py file.
2. Ensure you have Python installed on your system.
3. Optionally, prepare a .txt file with a list of words (one word per line) for the game to choose from.


## License

This project is open-source and free to use under the MIT License.

Enjoy playing the game!

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.
