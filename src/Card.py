import sys

import NumberSet
import CardPrinter


class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.__idnum = idnum
        self.__size = size
        self.__numberSet = numberSet
        pass

    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__idnum
        pass

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__size
        pass

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        if self.__size % 2 == 0:
            print(CardPrinter.printEven(self.__size, self.__numberSet), file=file)
        else :
            print(CardPrinter.printOdd(self.__size, self.__numberSet), file=file)
        pass
