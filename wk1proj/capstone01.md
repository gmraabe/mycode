# Capstone 01
## Lab Objective
The objective of this homework is to create a program that utilizes the skills you learned this week. You’re encouraged to incorporate any of the skills you learned this week, and welcome to experiment / learn some new ones!

Copying and pasting an entire solution isn’t the point, but you can certainly google and lift code snippets from the internet.

Try to have your “homework” uploaded to github.com//mycode/wk1proj/ by the EoD Monday May, 28 (I’d like to review progress)

## Procedure
Please choose at least one project to complete (or make up your own… contact the instructor if you’re unsure if it’s a solid idea). Advanced students, feel feel to explore an advanced library with the Python Package Index. It’d be great if you make up something you can teach us: sockets, email, apis, signal handling, netmiko, paramiko. All valid things to think about.

If you get a program working, besure to spend time IMPROVING it. The fastest way to a success on this, is to ask for pointers from the instructor (i.e. code review). If not in class, email the instructor, and ask them to check your Github repo, or remote desktop environment.

Create & work from the directory, mkdir ~/mycode/wk1proj/

Frequently perform: git add ~/mycode/* , git commit -m ‘message here’, git push origin master

Good luck!

### Inventory Tracker
Create a program that assumes inventory.txt will be local to where it was launched
Each line in inventory.txt contains a real world thing and the location of that real world thing (think room, or short description, or gps coordinates)
Create two functions callable by the user from a repeating menu:
1) create an new entry in inventory.txt
2) search inventory.txt for an entry, and if an entry is found, the user should be given the option of removing that entry from inventory.txt
Feel free to make your own additional features!

### Board Game Simulator
A complex boardgame would be a massive undertaking, but a simple one might be… simple.

When the program runs, it will ask for the number of players (you choose how many)

When it’s a player’s turn, randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.)

The program will print what that number is, and advance a player that many spaces on a ‘board’. You can display the board, or just indicate “where” the the player is. For example. Player1: @space 23 Player2: @space 15 Player3: @space 12

Concepts to think about

classes / objects
Random
Integer
Print
While Loops

### Let’s Play MAD LIBS!
Ever play Mad Libs? If not, the idea is simple. The user is asked for a series of words.

Enter a Noun:
Enter a verb:
Enter a adverb:
Enter a verb: … and so on…
The input is fed into a pre-made story template & the full story is printed to the screen, which promises to be MAD!

The longer / more story templates you have, the better it will be.

Concepts to think about

Strings
Variables
Concatenation
Print

### Text Based Adventures!
A personal favorite, complete a text game
Minimum –> Allow the users to move through rooms based on user input and get descriptions of each room (3 or 4 rooms is plenty)
To create this, you’ll need to establish the directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the rooms that tell the user, “You can’t move further in this direction.”
Try modeling the TLG office… or hallway & breakroom :)
This will get more difficult the more complex you make the game, so don’t reach for the moon. Don’t make your first game miss the release date! Gamers are waiting!!

Concepts to think about

Strings
Variables
Input/Output
If/Else Statements
Print
List
Integers

### Guess the Number
Use the random module in Python.
The program will first randomly generate a number unknown to the user. The user needs to guess (input) the number.
If the user’s guess is wrong, the program should return some sort of indication as to how wrong (high or low)
Use functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.

Concepts to think about

### Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements
Hangman - (surprisingly difficult)
Don’t need any ascii art. Although, that’d be kinda cool.
“guess the word” game
User needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use.
Use a function to check if the user has actually inputted a single letter, to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.
pull the word to guess against from a pre-made list (no need to be fancy here)

Concepts to think about

Random
Variables
Boolean
Input and Output
Integer
Char
String
Length
Print
