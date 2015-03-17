#Blackjack game using Python
This blackjack game was built using Python.


Roadblocks:
-	I created my game using the blackjack table background image, but I do not know how to make the
game work without it. I cannot use the background image because I do not have permission from its
owners. The game background defaults to all black but the background does not 
blit anymore. The game still works, but whenever I click 'hit' or 'stay' the text overlaps,
creating a messy-looking game.

-	I have not finished the game logic. As of now, the player wins if he breaches the 21-point
cap. The dealer wins if he has over 18 points. I plan on creating two helper functions that will
hold certain conditionals that compares both sets of points and determines the winner.

-	Python unit tests. I have done a bit of research but have not gotten around to implementing
Python's built in testing.



Test Spikes:
-	The hardest part was remembering to identify what were methods and what were variables. When
I first started developing I had no idea why the program wouldn't run (I usually don't know why
my programs run, but I was more confused with Python). Turns out I had to pass 'self' as an argument
to every method. It was a bit of a drag, but I developed a habit of doing it in Python.

Prerequisites:
-	Have Python installed
-	Have Pygame installed
-	Run the Python file(s) through Powershell

Flaws within my game:
-	I learned as much as I could about Python unit testing within the hour that I had. It is similar
to Ruby's unit testing but I was not able to grasp the syntax within the deadline. At the bottom
of testing.py's file, you will see class MyTest. The comments are what I was trying to accomplish.
You will see syntax similar to Ruby's unit test, with the expected and desired outcomes displayed.
In addition, I was able to print out a few lines using the unit tests--for whatever it's worth.

-	Ruby has 'require_relative', which imports the file I want to test. I wasn't able to figure out
how to do this in Python, so I had to settle for including the unit tests within the same file.

- There are no card graphics within this version, but in compensation, the game's logic works well.
