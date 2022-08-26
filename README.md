# wordle-solver

## Description
This is a Python program I created to solve the game of Wordle. At each turn, it gives you a best guess as well as all possible guesses at some turns. I created an information theory-based algorithm to maximize the amount of possible words eliminated on the first two guesses and every guess thereafter is the most common one of the possible words remaining. When I tried this on actual Wordle, it reported an average of 3.7 guesses per word.

## How to Run
The application is a command-line Python application; you can run `python wordle.py` in a terminal window to run it