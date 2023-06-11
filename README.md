# othello_project
## INTRO:
In this project, we will explore the game playing of Othello using search algorithms and heuristics. Othello is a two-player strategy game played on a 8x8 board, where each player has pieces that are either black or white. The goal of the game is to have the most pieces of your color on the board at the end of the game.

Othello is a strategy board game for two players (Black and White), played on an 8 by 8 board. The game traditionally begins with four discs placed in the middle of the board as shown below. Black moves first.

Black must place a black coin on the board, in such a way that there is at least one straight (horizontal, vertical, or diagonal) occupied line between the new disc and another black disc, with one or more contiguous white pieces between them.
when 2 consecutive turns get passed or there is no place on the board for a coin to be placed the game ends and the player with the higher number of coins win

## project features:
the game has 4 modes of play:

  .player vs player 
  .player vs computer 
  .computer vs player
  .computer vs computer
  
when we choose the computer as an opponent,
we need to choose a difficulty level from 5 options.
we have five levels of difficulty arranging in an ascending order based on their difficulty as follows:

  .Beginner
  .Amateur
  .Intermediate
  .Professional
  .Master
  
due to the design the first player is always black ;so threw choosing the mood you implicitly choose the color
when we go to the portion of the playing itself , we have an 8x8 board 
each cell is either black ,white or grey if it is empty.
after calculating the possible moves the possible cells change color to blue , after choosing a move it turns temporarily into orange.
there is a score panel in the upper right corner that has the players’ names , colors and scores that gets updated after each move .
in the upper left corner there is a bar with 3 buttons
Restart: restart the game with the same configuration
Start New Game: moves us back to choose different options for the game if we want .
Start AI: for the Ai to start a move in case of Computer vs Computer.

at the end of the game a message board appears in the center of the screen announcing the winner , then the user has the option to choose from Restart and Start New Game.

## User Manual:
when the user opens the game a page with a start button appears, when the user selects the button a home page appear,it contains 4 options for choosing the play mode.

after the user choose one another panel appears beside it having options for every AI based player in the upcoming game to choose the difficulty from 5 different levels.

After the user select start a different page opens, if player A is an AI the user need to select Start AI from the upper button so the player can make the first move, if player A is human there is no need for the previous step.

when it is the user's turn to play his possible moves will be colored in blue , he needs to select one cell from them it temporarily turns into orange then it takes the players assigned color white or black.

when 2 consecutive turns get passed or there is no place on the board for a coin to be placed ; a message board appears in the center of the screen announcing the winner , then the user has the option to choose from Restart and Start New Game.

At any moment of time the user can select

Restart which restart the game with the same configuration

or Start New Game: moves us back to choose different options for the game if we want .




