import time
import os
import random
import keyboard
import main

exitFlag = 0  #


def game(field, character, point, timer, speedIncrement):
    """
    Creates string to print where the player
    and points are located in the correct posistion

    Also reads if player and point are in the location
    and adds 1 to the player score then generated random
    respawn for the point
    """
    global exitFlag
    while True:
        string = ""

        for j in range(field.y_size):
            for i in range(field.x_size):
                if i == round(character.x_pos) - 1 and j == round(character.y_pos) - 1:
                    string += "X"
                elif i == round(point.x_pos) - 1 and j == round(point.y_pos) - 1:
                    string += "O"
                else:
                    string += field.symbol

            string += "\n"

        print(string)
        print(f"Time: {timer.length}\n\n")
        print(f"Score: {character.score}")
        print("Press 'escape' to exit")
        time.sleep(0.0001)
        os.system("cls")

        if point.x_pos == round(character.x_pos) and point.y_pos == round(
            character.y_pos
        ):
            character.score += 1
            point.x_pos = random.randrange(1, field.x_size - 1)
            point.y_pos = random.randrange(1, field.y_size - 1)
            character.speed += speedIncrement
            os.system("cls")
            print("SCORE!")
            time.sleep(1)
            os.system("cls")

        if exitFlag == 1:
            print("EXITING")
            break


def timer(timer):
    global exitFlag
    for i in range(timer.length):
        time.sleep(1)
        timer.length -= 1
    exitFlag = 1


def exitGame(character, filePath, newName, timeLength):
    global exitFlag
    while True and exitFlag == 0:
        if keyboard.is_pressed("escape"):
            exitFlag = 1
            break
        time.sleep(0.001)

    time.sleep(0.1)
    with open(filePath) as file:
        entry = file.read()
    file.close()

    index = []
    j = 0
    for i in entry:
        if i == ":":
            index.append(j)
        j += 1

    name = entry[0 : index[0]]
    highscore = int(entry[index[0] + 1 : index[1]])
    scoreSec = int(entry[index[1] + 1 :])

    print(
        f"Curent highscore is {highscore} set by {name} with a score per second of {scoreSec}"
    )
    if character.score > highscore:
        print("NEW HIGHSCORE SET!!!")
        # newName = input("Please enter your name.\n")
        print(f"New highscore: {character.score}")
        with open(filePath, "w") as file:
            file.write(
                f"{newName}: {str(character.score)}: {str(character.score/timeLength)}"
            )
    else:
        print("No new highscore set")


def startGame():
    print(
        "\nWelcome to the Command Line Game\nThe goal is to move your charater to collect the most amount of points before the time runs out\n"
    )
    name = input("Please enter your name: ")
    charaterSymbol = input("Enter the symbol to represent your character: ")
    pointSymbol = input("Enter the symbol to represent the point: ")
    timeLimit = int(input("Enter the time limit: "))
    input("\nPress 'ENTER' to start")

    return name, charaterSymbol, pointSymbol, timeLimit


if __name__ == "__main__":
    main.main()
