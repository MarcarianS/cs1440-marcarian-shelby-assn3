class CardPrinter():
    # def __init__(self, size):
    #     self.__size = size

    def printEven(self, size, numberSet):
        cardString = "+"
        for i in range(size):
            cardString += "-----+"
        cardString += "\n"
        for i in range(size):
            cardString += "|"
            for j in range(1, size - 1):
                cardString += str("{:^5}".format(numberSet[i * size + j]))
                cardString += "|"
            cardString += "\n"
        return cardString

    def printOdd(self, size, numberSet):
        cardString = "+"
        for i in range(size):
            cardString += "-----+"
        cardString += "\n"
        for i in range(0, size):
            cardString += "|"
            for j in range(1, size - 1):
                if (i * size + j) == ((size / 2 + 1) ^ 2):
                    cardString += "{:^5}".format("FREE")
                else:
                    cardString += str("{:^5}".format(numberSet[i * size + j]))
                cardString += "|"
            cardString += "\n"
        return cardString