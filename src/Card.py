import sys

import NumberSet



class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.__idnum = idnum
        self.__size = size
        self.__numberSet = numberSet


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__idnum


    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__size


    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        print(self.__printCard(self.__size, self.__numberSet.numberSet), file=file)

    def __printCard(self, size, numberSet):
        cardString = "+"
        for i in range(size):
            cardString += "-----+"
        cardString += "\n"
        for i in range(0, size):
            cardString += "|"
            for j in range(0, size):
                if size % 2 != 0 and (i * size + j) == int(pow(self.__size, 2) / 2):
                    cardString += "{:^5}".format("FREE!")
                else:
                    cardString += str("{:^5}".format(numberSet[i * size + j]))
                cardString += "|"
            cardString += "\n"
            cardString += "+"
            for k in range(size):
                cardString += "-----+"
            cardString += "\n"
        return cardString