import random


class NumberSet():
    def __init__(self, size, max):
        """NumberSet constructor"""
        self.__size = pow(size, 2)
        self.__max = max
        self.numberSet = self.__createSet()
        self.__getNextCounter = 0
        pass

    def __createSet(self):
        aNumberSet = list(range(1, self.__max + 1))
        self.randomize(aNumberSet)
        return aNumberSet[0:self.__size]

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.__size
        pass

    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self.numberSet[index]
        pass

    def randomize(self, aNumberSet):
        """void function: Shuffle this NumberSet"""
        return random.shuffle(aNumberSet)
        pass

    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        self.__getNextCounter += 1
        if self.__getNextCounter > self.__max:
            return None
        return self.numberSet[self.__getNextCounter - 1]
        pass
