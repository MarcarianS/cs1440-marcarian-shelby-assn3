# Bingo! User Manual

## To Run Bingo!

* To run the Bingo! Card Generator, open your command line interface (CLI).
* Navigate to the project directory and into the 'src' folder.
* Run the command "$ python bingo.py" (without quotations or the $) to begin the program.

## What You Should See

### Navigating the Main Menu

* When you first run "$ python bingo.py" the Main Menu will be displayed. You should see a list of commands (C and X) and a short description of each.
* The program will automatically prompt you for a command, shown in parenthesis.
* __Note:__ Unless you enter one of the provided options, you will be prompted for a command repeatedly until you enter a command that the program recognizes.
* Entering 'X' will leave the program.
* Entering 'C' will prompt you for a few numbers with the allowed range immediately following.
* Follow the prompts, and provide a card size, the maximum number you wish your cards to conatain, and the numebr of cards you wish to create.
* If you enter a number that is *not* within the displayed range, you will be reminded of the range and asked for another number, until you enter a valid number.

### Navigating the Deck Menu

* Next, the program will display the Deck menu, with options for your Deck.
* If you choose 'P', a single card of your choice will be printed to the screen.
* To determine which card to print, you will be prompted to enter the ID number of the card you wish to see. The range given corresponds to the number of cards you generated, and once again will continuously prompt you to choose a number until you provide valid input.
* If you choose 'D', the entire deck will be printed to the screen.
* If you choose 'S', the entire deck will be saved to a file of your choice.
* To determine which file to save the deck to, the program will prompt you for a file name. If that file does not yet exist, it will be created for you!
* If you choose 'X', you will be brought back to the Main Menu, and your Deck will be erased from the program.

## Troubleshooting

* The most common error you will run into with this program is when the program reads invalid input.

### What Does Invalid Input Look Like?

* Invalid input can be either a letter or character that is not in the list of commands.
* __Examples__:
	* Commands P, D, or S given to the Main Menu will be invalid. These only work for the Deck Menu.
	* Likewise, command C will be invalid in the Deck Menu.
	* Lowercase commands (p, c, etc.) are not recognized by the program. Commands must be entered exactly as displayed in the option list.
	* Any command not recognized by the program (R, !, 2) will be invalid. Commands must be entered exaclty as displayed in the option list.
	* For numeric commands, only integers withing the range provided are valid. The range is displayed in square brackets (e.g. [3,10]) and is inclusive (3 and 10 will be valid, but not 4 or 11.)

### How Do I Recover From Invalid Input?

* If you have entered invalid input, you will be prompted to enter another command.
* Read through the option list (displayed immediately after the prompt) and note that if you have not entered your input exactly as shown (e.g. no extra punctuation or characters) it will be invalid.
* To move forward at any point in the program, you must enter valid input.

## List of Commands

* C - Creates a new deck; will prompt you for input to specify the dimensions of the card.
* Numbers - Only provide numbers when prompted for numbers. These will specify dimensions of the cards.
* P - Prints a single card to the screen (You will be prompted for the number ID of the card you wish to see).
* D - Displays the entire deck to the screen.
* S - Saves the entire deck to a file (You will be prompted for a file name. If the file does not exist, it will be created for you.)
* X - From the Deck Menu, this will return you to the Main Menu and delete whatever deck you may have created. 
* X - From the Main Menu, this will exit the program.
