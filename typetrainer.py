#!/usr/bin/env python3

"""A simple typetrainer that shows a random string and checks if it matches
the user input"""

import random
import string

class WordGenerator:
    """Generator for random words consting of both uppercase, lowercase,
    digits, and special characters.
    """

    def __init__(self, charlist=False, word_length=5):
        self.charlist = charlist if charlist else string.printable[:94]
        self.n_chars = len(self.charlist)
        self.word_length = word_length

    def __next__(self):
        """Generate a random word with the specified length (default=5)
        """

        return ''.join(
            [
                self.charlist[random.randint(0, self.n_chars - 1)]
                for _
                in range(0, self.word_length)
            ]
        )


def main():
    """Show a word, check if user input matches, repeat
    """

    print('Type the characters (excluding "> " and hit enter. To quit, enter "exit" as answer.')

    word_generator = WordGenerator()

    while True:
        word = next(word_generator)
        print(word)
        answer = input("> ")

        if answer in ['quit', 'exit']:
            quit()

        if answer != word:
            print('You typed "{}" instead of "{}"'.format(answer, word))

if __name__ == "__main__":
    main()
