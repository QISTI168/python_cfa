#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Welcome to the Music Genre Guessing Game!")

    max_trials = 5
    trials = 0
    score = 100 # Initialize the score to 100

    music_genres = [
        "pop",
        "rock",
        "hip hop",
        "jazz",
        "electronic",
        "classical",
        "dj",
        "remix"
        ]

    x = random.choice(music_genres)
    guess = None

    while x != guess:

        guess = str(input("What music genre am I thinking of? "))
        trials += 5
        
        if x == guess:
            print("You've guessed {}. Congratulations, you guessed the correct music genre!".format(guess))
            score += 50
            print(score)
           
        else:
            print("You've guessed {}. Unfortunately, your guess is incorrect. Try again!".format(guess))
            score -= 20
            print(score)
         
        

main()