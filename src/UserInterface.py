import Deck
import Menu


class UserInterface():

    def __init__(self):
        pass

    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False

    def __getNumberInput(self, description, min, max):
        notValid = True
        while notValid:
            print(f"\n{description} [{min} - {max}]")
            number = int(input())
            if min <= number <= max:
                return int(number)
            print(f"Please input a number in the range [{min} - {max}]\n")

    def __getStringInput(self, description):
        print(f"\n{description}")
        return input()

    def __createDeck(self):
        """Command to create a new Deck"""
        cardSize = self.__getNumberInput("Enter card size ", 3, 15)
        maxNumber = self.__getNumberInput("Enter max number", pow(cardSize, 2) * 2, pow(cardSize, 2) * 4)
        numCards = self.__getNumberInput("Enter number of cards ", 3, 10000)

        self.__m_currentDeck = Deck.Deck(cardSize, numCards, maxNumber)

        self.__deckMenu()


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False

    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)

    def __saveDeck(self):
        """Command to save a deck to a file"""
        keepGoing = True
        while keepGoing:
            fileName = self.__getStringInput("Enter output file name")
            if fileName != "":
                outputStream = open(fileName, 'w')
                self.__m_currentDeck.print(outputStream)
                outputStream.close()
                print("Done!")
                keepGoing = False


