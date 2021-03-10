*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions

create a deck of bingo cards, with number of cards based on user input and
size based on user input.
Design a user friendly manual and user interface. Manual will give instructions 
on how to use each command. User interface will promt for those commands , 
looping until the user gives valid input.
The cards can't have the same number on them twice, and each card must be kept 
according to its number so it can be called on again.
The user must be able to print the deck ou tto the screen or a file, or a select 
card to the screen.

# 1.  System Analysis

Main menu:
The user is presented with options 
C will create a deck
X will exit the program

another menu from C
enter card size
maximum number present on card
number of cards generated

new menu
P print a card
	Must provide the number id of the card 
	menu PDSX is displayed again
D display the whole deck
S save the deck to a file
	Must provide a file name
	will notify the user when finished
X
	deck is no longer remmebered in the program
	takes you back tot the main menu

##User Interface Class
###Run()
* Input: nothing
* internal data
-print welcome message
-create menu object (local) with the header Main
-add the C option to the list of display options
-while we keep going, if the user enters C move on
-if keep going is false, close the program (sys.exit(1)?)
* output: prints welcome message, returns nothing

###__createDeck()
* Input: nothing
* internal Data:
-prompt the user for card size, max number on card, and 
number of cards
-for i in number of cards given, create a card object with 
the user in put and i as idnum
-create a deck object with input from user. deck needs to 
be able to access the card objects
-call __deck menu to display the deck menu
* Output: Nothing

###__deckMenu()
* Input: nothing
* Intternal Data: 
-create a menu object header Deck
-add the print, display, and save options to the menu options
-print out the apporpriate response based on the user input 
command.
* Output: prints menu to user through other methods

###__printCard()
* Input: nothing
* INternal Data: 
-call __getnumberinpout to determine which index to print
* Output: calls a print method, returns nothing

###__saveDeck()
* INput: nothing
* Internal Data: 
-get the file name as a string from the user
-if no file name is given, display the menu again
-if there is a filename given, open file as "write"
-prints the current deck to the file 
-close the file
-tels the user it is done
* Output: prints the deck to a file, returns nothing

###__getNumberInput(desc, int, numOfCards)
* Input:  a string descriptor of what is beign returned, a 
number, and the number of cards in the deck.
* Internal Data: 
-print the description to prompt the user for input
-if the number input by the user is smaller than the
number of cards given, return that id
-if its out of range (too big or less than 1) have the user
try again
-NOT SURE WHAT SECOND ARGUMENT IS YET
* Output: returns n integer, the id of the card to print

###__getStringInput(desc)
* input: string to prompt the user for input of a file name
* INternal Data: 
-use the desc to prompt the user for a  file name
-return that string
* Outptu: string ( a file name)


##Card Class
###getId()
* INput: nothing
* internal Data: 
-return the idnum
* Ouput: idnum of the card

###getSize()
* Input: nothing
* internal Data: 
-return the card size (one dimension of the card)
* Output: return size of the card

###print(file)
* Input: optional name of a file (f not given, sys.out)
* internal Data: 
-print the current card id to the file specified
-coe in the formatting for the card here
-if size is odd, add a free space
* Output: prints a card to the file given


##Deck Class
###getCrdCount()
* input: npthing
* internal data: 
-return the cardcount variable
* output: return cardCount

###getCard(n)
* Input: the card object that the user wants to print out
* Internal Data: 
-card is initially none
-the number given is decreaseed by one to account for the 
list index
-if the number given is in the proper range, the card object
is taken from m cards, a list of the card objects in deck
-card is returned
* Output: returns card object to print out

###print(file, index)
* Input: name of a file in string format, index of card to
print
* internal Data: 
-if indx is default, print out every card 
-assign card object to variable c
-call print on c
-print a new space
-if indx is not default, print only the specified card


##Menu Class

###addOption(command, description)
* Input: command (a single uppercase letter that represents a
command) and a descripton (what the command does)
* INternal Data: 
-if the fields are not left empty, add the tuple (comm,desc)
to the list of menu options(only availible to specific menu
object)
-add one to the menu options count
* Output: nothing

###__isValidComand(command)
* Input: command (single uppercase letter)
* Internal Data: 
-set variable isValid to false
-if user selected X, its valid
-if not, check the command against the list of options.
-if the command is in that list, its valid
-return the value of isvalid (boolean)
* Output: boolean is valid

###getOption(optionIndex)
* Input: index integer, what option you want to test.
* Internal Data: 
-initialize the option to none value
-if option index is in the proper range, the option is set
to that index in the list of objects
-whether it's none or a value, option is returned
* Output: returns whatever option ends up as. can be none

###getHeader()
* Input: nothing
* INternal Data:
-return the header string for this menu object
* Output: header string returned

###getOptionCount()
* Input: nothing
* INternal Data:
-return the size of the option count for this menu object
* Output: option count as an integer is returned

###show()
* input: nothing
* INterna data:
-intialize a command and keepgoing variables to empty string
and true
-while that keepgoing var is true, set local option list to
and empty string, print a newline and the header
-for the length of the menu objects option count, local 
option is ith entry of the self option list.
-if getting the option didn't return none, print the command
and its desc.
-add that command and x to the local command optionlist
-print the prompt for a command
-if the input is not in the command list (call isvalid)
-once a valid command is given, return that command
* Ouput: prints options to user and returns command given.

##Menu Optoion CLass

##Number Set Class
		
# 2.  Functional Examples

**Design a process for obtaining the output from the input.  Consider both *good*
and *bad* inputs.  Find or create examples of both kinds of input.**

**Work out problem examples on paper, on a whiteboard or some other medium that
is *not* your computer.  It is a mistake to begin writing executable code
before you thoroughly understand what form the algorithm(s) must take.**

**Instead, describe components of the system in *"pseudocode"*.  Expect to make
lots of mistakes at this point.  You will find that it is much easier to throw
away pseudocode than real code.**

**Manually work through several examples that illustrate the program's overall
purpose, as well as the purpose of each component of the finished system.  You
will converge on a correct solution much faster if you feel comfortable making
mistakes as you go.**

**This phase involves the use of many levels of abstraction to decompose the
problem into manageable components, and design strategies for implementing each
component.  Components may be functions, modules or classes.**


# 3.  Function Template

**Combine the function stubs written in step #2 with pseudocode from step #3.
Comment out the pseudocode, leaving a valid program that compiles/runs without
errors.  At this stage your program doesn't quite work, but it also doesn't
crash.**


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
