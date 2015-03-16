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