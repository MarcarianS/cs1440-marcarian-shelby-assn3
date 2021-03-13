
# 0.  From Problem Analysis to Data Definitions

create a deck of bingo cards, with number of cards based on user input and\
size based on user input.\
Design a user friendly manual and user interface. Manual will give instructions \
on how to use each command. User interface will promt for those commands , \
looping until the user gives valid input.\
The cards can't have the same number on them twice, and each card must be kept \
according to its number so it can be called on again.\
The user must be able to print the deck ou tto the screen or a file, or a select \
card to the screen.\

# 1.  System Analysis

Main menu:\
The user is presented with options \
C will create a deck\
X will exit the program

another menu from C\
enter card size\
maximum number present on card\
number of cards generated

new menu\
P print a card\
	Must provide the number id of the card \
	menu PDSX is displayed again\
D display the whole deck\
S save the deck to a file\
	Must provide a file name\
	will notify the user when finished\
X\
	deck is no longer remmebered in the program\
	takes you back tot the main menu

## User Interface Class
### Run()
* Input: nothing
* internal data
	- print welcome message
	- create menu object (local) with the header Main
	- add the C option to the list of display options
	- while we keep going, if the user enters C move on
	- if keep going is false, close the program (sys.exit(1)?)
* output: prints welcome message, returns nothing

### __createDeck()
* Input: nothing
* internal Data:
	- call getNumberInput() for card size, max number on card, and 
number of cards
	- create a deck object with input from user. deck needs to 
be able to access the card objects
	- call __deck menu to display the deck menu
* Output: Nothing
* Function Stub: 
cardSize = getNumberInput("enter card size", 3, 15)\
max number = getnumberinput("enter max", cardSize x cardsize x 2, cardsize x cardsize x 4)\
numCards = getnumebrinput("enter num of cards", 3, 10_000)\
\
m_currentdeck = Deck.Deck(cardSize, numCards, maxNumber)\
\
call __deckMenu()\

### __deckMenu()
* Input: nothing
* Intternal Data: 
	- create a menu object header Deck
	- add the print, display, and save options to the menu options
	- print out the apporpriate response based on the user input 
command.
* Output: prints menu to user through other methods

### __printCard()
* Input: nothing
* INternal Data: 
	- call __getnumberinpout to determine which index to print
* Output: calls a print method, returns nothing

### __saveDeck()
* INput: nothing
* Internal Data: 
	- get the file name as a string from the user
	- if no file name is given, display the menu again
	- if there is a filename given, open file as "write"
	- prints the current deck to the file 
	- close the file
	- tels the user it is done
* Output: prints the deck to a file, returns nothing

### __getNumberInput(desc, min, max)
* Input:  a string descriptor of what is beign returned, a 
number, and the number of cards in the deck.
* Internal Data: 
	- print the description to prompt the user for input
	- if the number input by the user is smaller than the
number of cards given, return that id
	- if its out of range (too big or less than 1) have the user
try again
	- use the second argument as a minimum that can be returned
* Output: returns n integer, the id of the card to print
* Function Stub: 
notValid = true\
while notValid\
print(f"{desc} [{min} - {max}")\
number = input()\
if min <= number <= max\
return number, notValid = false
if not in correct range\
print(f"please input number in the range [{min} - {max}\n")\


### __getStringInput(desc)
* input: string to prompt the user for input of a file name
* INternal Data: 
	- use the desc to prompt the user for a  file name
	- return that string
* Outptu: string ( a file name)
* Function Stub:
print(f"{desc}")\
return input()

## Card Class
### getId()
* INput: nothing
* internal Data: 
	- return the idnum
* Ouput: idnum of the card

### getSize()
* Input: nothing
* internal Data: 
	- return the card size (one dimension of the card)
* Output: return size of the card

### print(file)
* Input: optional name of a file (f not given, sys.out)
* internal Data: 
	- if size is odd, call CardPrinter.printOdd()
	- if even, CardPrinter.printEven()
* Output: prints a card to the file given


## CardPrinter Class

### printEven()
* Input: nothing
* internal Data:
	- to print the top border, print the following pattern 
	- cardString = the first +
	- for i in size string+= "-----+"
	- string+= "\n"
	- To print the rest of the card:
	- for i in 0 - size
	- string += "|"
	- for j in 1 - size-1 string+= (" numberset(i *size + j)|")
	- string+= "\n"
	- Make sure the entry from number set is centered
* Output: returns String containing card info to be printed
* Function Stub: 
Follow internal Data above\

### printOdd()
* Input: nothing
* Internal Data: 
	- free space will be (size/2 + 1)^2
	- follow layout for even card, checking that each iteration is not the free space


## Deck Class
### Deck(cardSize, carDCount, numberMax)
* Input: cardsize, card count, number max, all integers
* Internal Data: 
	- initialize self variables
* Oupput: nothing
* function Stub:
self.cardSize = cardSize\
self.cardCount = cardCount\
self.numberMax = numberMax\
self.__m_cards = []

### createDeck()
* Input: dimensions of the card, all integers
* internal Data: 
	- loop over the cardcount, creating a card object for each
	- append the cards to m_cards[]
	- Return the list of cards
* Output: returns the list of cards
* Function Stub: 
for i in cardCount\
card = Card.Card(i, self.cardSize, NumberSet.createDeck(self.Size, self.max)\
m_cards.apend(card)\
return m_cards\


### getCrdCount()
* input: npthing
* internal data: 
	- return the cardcount variable
* output: return cardCount

### getCard(n)
* Input: the card object that the user wants to print out
* Internal Data: 
	- card is initially none
	- the number given is decreaseed by one to account for the 
list index
	- if the number given is in the proper range, the card object
is taken from m cards, a list of the card objects in deck
	- card is returned
* Output: returns card object to print out

### print(file, index)
* Input: name of a file in string format, index of card to
print
* internal Data: 
	- if indx is default, print out every card 
	- assign card object to variable c
	- call print on c
	- print a new space
	- if indx is not default, print only the specified card


## Menu Class

### addOption(command, description)
* Input: command (a single uppercase letter that represents a
command) and a descripton (what the command does)
* INternal Data: 
	- if the fields are not left empty, add the tuple (comm,desc)
to the list of menu options(only availible to specific menu
object)
	- add one to the menu options count
* Output: nothing

### __isValidComand(command)
* Input: command (single uppercase letter)
* Internal Data: 
	- set variable isValid to false
	- if user selected X, its valid
	- if not, check the command against the list of options.
	- if the command is in that list, its valid
	- return the value of isvalid (boolean)
* Output: boolean is valid

### getOption(optionIndex)
* Input: index integer, what option you want to test.
* Internal Data: 
	- initialize the option to none value
	- if option index is in the proper range, the option is set
to that index in the list of objects
	- whether it's none or a value, option is returned
* Output: returns whatever option ends up as. can be none

### getHeader()
* Input: nothing
* INternal Data:
	- return the header string for this menu object
* Output: header string returned

### getOptionCount()
* Input: nothing
* INternal Data:
	- return the size of the option count for this menu object
* Output: option count as an integer is returned

### show()
* input: nothing
* INterna data:
	- intialize a command and keepgoing variables to empty string
and true
	- while that keepgoing var is true, set local option list to
and empty string, print a newline and the header
	- for the length of the menu objects option count, local 
option is ith entry of the self option list.
	- if getting the option didn't return none, print the command
and its desc.
	- add that command and x to the local command optionlist
	- print the prompt for a command
	- if the input is not in the command list (call isvalid)
	- once a valid command is given, return that command
* Ouput: prints options to user and returns command given.

## Menu Optoion CLass

### getCommand()
* Input: nothing
* Interal Data: 
	- return the command given to the menu option object
* Output: returns single character command

### getDescription()
* Input: nothing
* Interal Data:
	- return the description given to the menu option object
* Output: returns string of the description for the menu option

## Number Set Class

### NumberSet(size, max)
- self.size = size
- self.max = max
- self.numberList = []
- self.getNextCounter = 0
### getSize()
* INput: nothing
* internal data: 
	- the number set is all of the numbers present on the card		
	- getsize from Card, square it
* Output: returns the number of numbers that can be in the NS
* Function Stub : 
return self.size^2\

### get(index)
* input: index, the number entry that you want the val of
* Internal Data: 
	- call CreateSet to get the list of random numebrs
	- get the indexth entry from what createSet returns
return that value
* Output: returns the value of the indexth entry of a card
* Function stub:
numberSet = createSet(self.size, self.max)\
return numberset[index]\

### randomize()
* Input: nothing
* internal Data: 
	- use random.shuffle(list) to shuffle the list
* OUtput: nothing
* Function Stub: 
return random.shuffle(numberSet)

### getNext()
* intput: nothing
* internal data: 
	- keep track of how many times its been called
	- the number of times it's been called is the index of the set 
to return
	- add a self. variable to the constructor and increase by one 
every time getNext is called
	- if that count goes above size^2, return none
* OUtput: an integer until the list is exhausted; then None
* Function Stub: 
counter += 1\
if counter >maxNumber, return None\
else, return counter - 1 entry from numberSet list

### createSet()
* input: size, the size of the card/set to create, max, the
biggest number to create
* internal data:
	- fill numberlist with values from 1 to max val + 1
	- randomize the set
	- return the values at index from 1 to setSize (size squared)
* output: a list of random numbers
* Function Stub: 
for i in range(max + 1)\
numberList.append(i)\
self.randomize(numberList)\
return numberList[0:size^2 + 1]\

# 2.  Functional Examples

## User Interface Class

### __createDeck()
```cardSize = getNumberInput("Enter card size ", 3, 15)
maxNumber = gerNumberInput("Enter max number ", cardSize * cardSIze * 2, cardSize * cardSize * 4)
numCards = getNumberInput("Enter number of cards ", 3, 10000)

m_currentDeck = Deck.Deck(cardSize, numCards, maxNumber)

__deckMenu()``

### __getNumberInput(description, min, max)
```notValid = True
while notValid:
	print(f"{descripction} [{min} {max}]")
	number = input()
	if min <= number <= max
		notValid = false
		return number
	print(f"Please input a number in the range [{min} - {max}]")```

### __getStringInput(description)
```print(f"{description}")
return input()```


## Card Class

### Card(idnum, cardSize, numberSet)
```
self.__idnum = idnum
self.__cardSize = cardSize
self.__numberSet = numberSet
```

### print(file)
```if self.cardSize % 2 == 0
	print(CardPrinter.printEven(self.cardSize), file=file)
else
	print(CardPrinter.printOdd(self.cardSize), file=file)```


## Card Printer Class

### Card(idnum, cardSize, numberSet)
```
self.__idnum = idnum
self.__cardSize = cardSize
self.__numberSet = numberSet
```
### printEven(cardSize)
```cardString = "+"
for i in cardSize
	cardString += "-----+"
cardString += "\n"
for i in range(0, cardSize)
	cardString ++ "| "
	for j in range(1, cardSize - 1)
		cardString += str("{:^5}".format(numberSet[i * cardSize + j]))
		cardString += "|"
	cardString ++ "\n"
return cardString		
```

### printOdd(cardSize)
```cardString = "+"
for i in cardSize
        cardString += "-----+"
cardString += "\n"
for i in range(0, cardSize)
        cardString ++ "| "
        for j in range(1, cardSize - 1)
		if numberSet[i * cardSize + j] == (cardSize / 2 + 1) ^ 2
			cardString += "{:^5}".format("FREE")
		else
                	cardString += str("{:^5}".format(numberSet[i * cardSize + j]))
                cardString += "|"
        cardString += "\n"
return cardString
```

## Deck Class
### Deck(cardSize, cardCount, numberMax)
```
self.cardSize = cardSize
self.cardCount = cardCount
self.numberMax = numberMax
self.__m_cards = createDeck()
```

### createDeck()
```
cards = []
for i in range(cardcount)
	card = Card.Card(i, self.cardSize, NumberSet.NumberSet(self.size, self.max))
	cards.append(card)
return cards
```


## Number Set Class
### NumberSet(cardSize, max)
```
self.__cardSize = cardSize
self.__max = max
self.numberSet = createSet()
self.__getNextCounter = 0
```
### get(index)
```
return self.numberSet[index]
```

### randomize(setToRandomize)
```
return random.shuffle(setToRandomize)
```

### getNext()
```
self.__counter += 1
if self.__counter > maxNumber
	return None
return self.numberSet[counter - 1]
```

### createSet()
```
aNumberSet = list(range(1, max + 1)
randomize(aNumberSet)
return aNumberSet[0:self.__cardSize^2 + 1]
```
# 3.  Function Template



# 4.  Implementation



# 5.  Testing

