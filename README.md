# Simple command line game

**Goal:**
The goal is to capture the most points before the time runs out.

**How to play:**
Your player is identified by the `X` and the point by `O`. Your player and 1 point are placed into a field where they are able to move around. Your player is controlled by the arrow keys and the point moves around the field randomly. To score a point, your player must occupy the same spot as the point. Once the point has been captured, it will spawn randomly again and the player speed will slightly increase. Once the timer runs out, if you set a new highscore, it will ask you to enter your name to store your name and cooresponding score.

**How it works:**
This game is based on the idea of threading in python to create and run code simultaneously. There are 5 active threads in this game as explained below. All threads except for the `exitThread` are daemonic, meaning once the `exitThread` is closed, the others will close with it. 
1. `exitThread`: Looking to see if the escape key is pressed. If pressed, activate the exit flag causing all threads to end.
2. `gameThread`: Printing the game graphics to the terminal and updating the image depending on the player/point location along with time remaining.
3. `timerThread`: Subtracting 1 off the starting time and updating the timer object .time attribute.
4. `playerMovementThread`: Looking to see if the arrow keys are being pressed and update the  player x_pos and y_pos accordingly.
4. `pointMovementThread`: Randomly generating a number 0-3 every 1 second to determine the direction of travel. The point object's x_pos and y_pos are updated for everymovement.

There are also 4 types of objects used in this game; `Field`, `Player`, `Point`, and `Timer`. The `Field` object has attributes to determine the size of the playing field along with the blank space character. Both the `Player` and `Point` have attributes to determine thier location and the symbol they are represented by along with the speed of the character. The `Timer` is an object that has a single attribute which is the remaining length of time.

The highscore is stored in a simple `.txt` file. After the game is completed, the file is opened and the previous highscore is read. If the current score is greater, the player can input thier name where it is written back into the `highscore.txt` file.