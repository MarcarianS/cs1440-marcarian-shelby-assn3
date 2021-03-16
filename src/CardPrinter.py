# class CardPrinter():
#     # def __init__(self, size, numberSet):
#     #     self.__size = size
#     #     self.__numberSet = numberSet
#
#     def printEven(self, size, numberSet):
#         cardString = "+"
#         for i in range(size):
#             cardString += "-----+"
#         cardString += "\n"
#         for i in range(size):
#             cardString += "|"
#             for j in range(1, size - 1):
#                 cardString += str("{:^5}".format(numberSet[i * size + j]))
#                 cardString += "|"
#             cardString += "\n"
#         return cardString
#
#     def printOdd(self, size, numberSet):
#         cardString = "+"
#         for i in range(size):
#             cardString += "-----+"
#         cardString += "\n"
#         for i in range(0, size):
#             cardString += "|"
#             for j in range(1, size - 1):
#                 if (i * size + j) == ((size / 2 + 1) ^ 2):
#                     cardString += "{:^5}".format("FREE")
#                 else:
#                     cardString += str("{:^5}".format(numberSet[i * size + j]))
#                 cardString += "|"
#             cardString += "\n"
#         return cardString