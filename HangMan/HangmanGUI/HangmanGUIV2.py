"""
Author: Josue Molina Morales
File: HangmanGUIV2.py
This module contains the class HangmanGUI that contains the hangman game
THIS IS THE MAIN VERSION
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from hangman import Hangman


class HangmanGUI(EasyFrame):
    """Class definition for a GUI based Hangman game"""

    def __init__(self):
        """
        This __init__ method contains everything that the user will see,
        apart from the pop up windows.
        """
        # Start a hangman game by creating a hangman object
        self.hangman = Hangman()
        EasyFrame.__init__(self, title="Hangman by: Josue", background='#add8e6', resizable=False)

        # set the hangman picture
        self.hangmanPic = self.addLabel(text="", row=0, column=0)
        self.image = ""
        self.resetHangmanPic()

        # set the text box for the guesses
        self.addLabel(text="Enter your guess (one letter at a time):", row=0, column=1, sticky='W')
        self.inputGuess = self.addTextField(text="", row=0, column=1, columnspan=2, sticky='E', state="normal")

        # binds the Enter key to the checkinput method so you don't need to press the button
        self.inputGuess.bind("<Return>", lambda event: self.checkinput())

        # set a text box for the user to enter the full word if they would like to guess it
        self.addLabel(text="Enter the full word here if you know it:", row=0,
                      column=1, sticky="SW")
        self.wordGuess = self.addTextField(text="", row=0, column=2, sticky='SW', state='normal')
        self.wordGuess.bind("<Return>", lambda event: self.checkinput())

        # set underscores
        self.underscores = self.addLabel(text=self.hangman.display_underscores(), row=2, column=0, sticky="N")

        # set words already guessed box
        self.addLabel(text="Letters Guessed Wrong:", row=1, column=1, sticky="SE")
        self.wrongGuesses = self.addTextField(text=self.hangman.get_wrongGuess(), row=1, column=2,
                                              state='readonly', sticky="SE")
        # display hint textfield and label
        self.addLabel(text="Here is your hint:", row=0, column=1, sticky='NE')
        self.hintText = self.addTextField(text=self.hangman.getHint(), state='readonly', row=0, column=2, sticky='NW')

        # display a reset button for when the user wants to reset and play again
        self.addButton(text='Reset', row=3, column=0, command=self.playAgain)

        # introduction popup
        self.messageBox(width=40, height=10, title="WELCOME TO HANGMAN", message=self.hangman.introduction())

    def resetHangmanPic(self):
        """
        Helper method that resets the hangman picture
        """
        self.image = PhotoImage(file='hangman1.png')
        self.hangmanPic['image'] = self.image

    def checkinput(self):
        """Helper Method that receives the guess from the textbox and places it
        into the var guess. guess is then validated, making sure it is just one character long
        after is checks to see if the guess is wrong if it is the hangman gets updated and the guess
        gets added to the wrong guesses output textbox. If the answer is right it updates the underscores
        and then sees if the user has won, if they have won a pop up message will appear
        If the user entered a guess in the wordGuess box the program will evaluate that"""
        char_guess = self.inputGuess.getText()
        word_guess = self.wordGuess.getText()
        self.inputGuess.delete('0', 'end')  # delete characters in textbox after pressing 'guess'
        self.wordGuess.delete('0', 'end')

        if len(char_guess) > 1:
            self.messageBox(width=40, height=10, title="ERROR",
                            message="Guess must be one character.")
        else:
            if not self.hangman.checkGuess(char_guess):
                self.updateHangman()
                self.wrongGuesses.setText(self.hangman.get_wrongGuess())
            else:
                self.underscores['text'] = self.hangman.display_underscores()
                if self.hangman.check_if_won():
                    self.youWin()
        if word_guess.lower() == self.hangman.getWord().lower():
            for char in word_guess:
                self.hangman.checkGuess(char)
            self.underscores['text'] = self.hangman.display_underscores()
            self.youWin()
        elif not word_guess == '':  # if word_guess is not empty
            self.messageBox(width=40, height=10, title="WRONG GUESS",
                            message="%s was the wrong guess!" % word_guess)

    def updateHangman(self):
        """Helper method that gets counter information from the hangman object.
        as the user enters wrong guesses the counter will increase and the hangman picture will change
        if the counter is at 6 then the user has lost and the youLose method is called."""
        if self.hangman.get_counter() == 1:
            self.image = PhotoImage(file='hangman2.png')
            self.hangmanPic['image'] = self.image
        elif self.hangman.get_counter() == 2:
            self.image = PhotoImage(file='hangman3.png')
            self.hangmanPic['image'] = self.image
        elif self.hangman.get_counter() == 3:
            self.image = PhotoImage(file='hangman4.png')
            self.hangmanPic['image'] = self.image
        elif self.hangman.get_counter() == 4:
            self.image = PhotoImage(file='hangman5.png')
            self.hangmanPic['image'] = self.image
        elif self.hangman.get_counter() == 5:
            self.image = PhotoImage(file='hangman6.png')
            self.hangmanPic['image'] = self.image
        elif self.hangman.get_counter() == 6:
            self.image = PhotoImage(file='hangman7.png')
            self.hangmanPic['image'] = self.image
            self.youLose()

    def youLose(self):
        """Helper function that displays that the user has lost and displays the correct answer
        Also disables the input box and button so that the user is not allowed to enter characters after losing"""
        self.messageBox(width=40, height=10, title="SORRY YOU LOSE",
                        message="YOU LOSE! \nThe Correct Word was: %s"
                                "\nHit the 'reset' button to play again!" % self.hangman.getWord())
        self.inputGuess['state'] = 'disabled'
        self.wordGuess['state'] = 'disabled'

    def youWin(self):
        """Helper method that displays that the user has won"""
        self.messageBox(width=40, height=10, title="CONGRATULATIONS!",
                        message="YOU WIN!\nPress 'Reset' to play again!")
        self.inputGuess['state'] = 'disabled'
        self.wordGuess['state'] = 'disabled'

    def playAgain(self):
        """Helper method that is used when the user presses the 'reset' button. If pressed this method
        will be called and resets all the necessary things to play a new game"""
        # makes a new hangman object to start a new game
        self.hangman = Hangman()

        # resets the hangman picture
        self.resetHangmanPic()

        # resets the underscores
        self.underscores['text'] = self.hangman.display_underscores()

        # resets the wrong guesses output box
        self.wrongGuesses.setText(self.hangman.get_wrongGuess())

        # resets the hint text box
        self.hintText.setText(self.hangman.getHint())

        # reverts the input Textbox back to normal and the button
        self.inputGuess['state'] = 'normal'

        self.wordGuess['state'] = 'normal'


def main():
    """Main function to play the hangman game."""
    HangmanGUI().mainloop()


if __name__ == '__main__':
    main()
