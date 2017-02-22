#!usr/bin/env python3

import random
import string

class TypeTrainer:
    def __init__(self, charlist=False):
        self.charlist = charlist if charlist else string.printable[:94]
        self.n_chars = len(self.charlist)

    def get_word(self, word_length=5):
        return ''.join([self.charlist[random.randint(0, self.n_chars)] for _ in range(0, word_length)])

if __name__ == "__main__":
    tt = TypeTrainer()
    print(tt.get_word())

