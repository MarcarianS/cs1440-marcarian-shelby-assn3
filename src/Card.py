import sys

import NumberSet
# import CardPrinter


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
        # if self.__size % 2 == 0:
        print(self.printCard(self.__size, self.__numberSet.numberSet), file=file)
        # else:
        #     print(self.printOdd(self.__size, self.__numberSet.numberSet), file=file)

    # def printEven(self, size, numberSet):
    #     cardString = "+"
    #     for i in range(size):
    #         cardString += "-----+"
    #     cardString += "\n"
    #     for i in range(size):
    #         cardString += "|"
    #         for j in range(1, size - 1):
    #             cardString += str("{:^5}".format(numberSet[i * size + j]))
    #             cardString += "|"
    #         cardString += "\n\n"
    #     return cardString

    def printCard(self, size, numberSet):
        cardString = "+"
        for i in range(size):
            cardString += "-----+"
        cardString += "\n"
        for i in range(0, size):
            cardString += "|"
            for j in range(0, size):
                if size % 2 != 0 and (i * size + j) == pow((int(size / 2) + 1), 2):
                    # if (i * size + j) == pow((int(size / 2) + 1), 2):
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