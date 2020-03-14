# Snake-Game
This is a replication of the popular online snake game and was created after my first semester of programming at the University of Sydney. The player begins the game with an original body size of 5 body parts. As the game progresses and the player's snake eats more apples, the score in the top left corner increases and reflects the increase in size of the player's snake. The game ends when either the player's snake runs into a segment of its body or the player attempts to exceed the game's boundaries.
## Apple (Seed) Placement
The apple that the snake must reach in order to grow in size is randomly placed in the map after it has been eaten. A collision detection ensures that the apple does not appear on a space where the snake is already at. When the snake reaches the same square as the apple, the apple must be removed and redrawn at another pseudo-random position.

## Pause Function
The pause function can be accessed during the game after the player has started. This is done by pressing the 'p' button which will freeze the snake's position and maintain the game's position. The player is then prompted with two options which are to either resume or quit the game. Another way of resuming the game is for the user to press the 'p' button again.

## Crashing Function
At the conclusion of the game, the player is given two choices which are to either start a new game or quit the game. Pressing the "Play Again! option will reset the game in the main function and create new Objects.
