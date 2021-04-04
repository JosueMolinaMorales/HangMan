"""
Author: Josue Molina Morales
File: hangman.py
This module contains the class 'Hangman' that can be used for
playing a hangman game
"""
import random


class Hangman:
    MAX_TRIES = 6  # The number of tries a person gets

    # dic of words and their corresponding hints
    words_hints = {"Pasta": "Carbs", "Winter": "Holidays!", "Lion": "Fierce", "Laptop": "Portable",
                   "Water": "Refreshing", "Hello": "Greetings", "Lawn": "Grass", "Beach": "Sandy",
                   "iPhone": "Steve Jobs", "Turtle": "Slow and Green", "Thunderstorm": "Rain",
                   "Christmas": "Presents", "Keyboard": "Lots of typing", "Television": "Big Screen",
                   "Mask": "Wear it!", "Face": "Cover it!", "Pandemic": "End of the world",
                   "Wedding": "White dress", "Socks": "Keep your piggies warm", "Stars": "Twinkle",
                   "Broccoli": "Vegetables", "Netflix": "And Chill"}

    def __init__(self):
        """Initialize all the necessary variables for the hangman game"""
        self.word = self.getRandomWord()
        self.underscores = ['___'] * len(self.word)
        self.counter = 0
        self.wrongGuesses = []

    def getRandomWord(self):
        """Helper method that returns a random word from a list of keys from
        words_hints keys"""
        return random.choice(list(self.words_hints.keys()))

    def getWord(self):
        """Returns the random word chosen"""
        return self.word

    def getHint(self):
        """Returns the hint to the corresponding word that was chosen"""
        return self.words_hints.get(self.word)

    def checkGuess(self, guess):
        """Checks to see if the guess is in the word, if it is it checks where in
        the word is appears and checks for every occurrence of the letter return True
        Else the guess is added to the wrong guess list and the counter is increased, returns False"""
        if guess.lower() in self.word.lower():
            index = 0
            for char in self.word.lower():
                if guess == char:
                    self.underscores.pop(index)
                    self.underscores.insert(index, guess)
                index += 1
            return True
        else:
            self.wrong_guess(guess)
            self.counter += 1
            return False

    def wrong_guess(self, guess):
        """Helper method that adds a wrong guess to the wrongGuess list"""
        self.wrongGuesses.append(guess)

    def get_counter(self):
        """Returns the counter"""
        return self.counter

    def get_wrongGuess(self):
        """Returns all the wrong guesses"""
        return ', '.join(map(str, self.wrongGuesses))

    def display_underscores(self):
        """Returns the underscores"""
        return '  '.join((map(str, self.underscores)))

    def check_if_won(self):
        """Helper method that checks to see if there is any underscore in
        the list, underscore. If there is then the user has not won yet, else the user has won"""
        if '___' not in self.underscores:
            return True
        else:
            return False

    def introduction(self):
        """Introduction to the game"""
        message = "WElCOME TO HANGMAN!\n" \
                  "You have a limited amount of guesses." \
                  "\nFor every wrong guess a body part will be added." \
                  "\nIf you make a man, GAME OVER!" \
                  "\nEnter your guess then press 'Enter'" \
                  "\nCreated by Josue Molina Morales."
        return message
