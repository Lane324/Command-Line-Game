import keyboard
import random
import time
import main


def move_player(character, field):
    """
    Take in arrow key press and increment
    X or Y position
    """
    increment = character.speed
    while True:
        try:
            if keyboard.is_pressed("left arrow") and character.x_pos > (
                0 + increment + 1
            ):
                character.x_pos -= increment
            if keyboard.is_pressed("right arrow") and character.x_pos < (
                field.x_size - increment
            ):
                character.x_pos += increment
            if keyboard.is_pressed("down arrow") and character.y_pos < (
                field.y_size - increment
            ):
                character.y_pos += increment
            if keyboard.is_pressed("up arrow") and character.y_pos > (
                0 + increment + 1
            ):
                character.y_pos -= increment

            time.sleep(0.0001)
        except:
            pass


def move_point(point, field):
    """
    Generate 2 random numbers cooresponding to X and Y movement

    If num1 = 0 move left
    If num1 = 1 move right
    If num2 = 0 move up
    If num2 = 1 move down
    """

    while True:
        num1 = random.randrange(2)
        num2 = random.randrange(2)
        try:
            if num1 == 0 and point.x_pos > 1:
                point.x_pos -= 1
            if num1 == 1 and point.x_pos < field.x_size:
                point.x_pos += 1
            if num2 == 0 and point.y_pos > 1:
                point.y_pos -= 1
            if num2 == 1 and point.y_pos < field.y_size:
                point.y_pos += 1

            time.sleep(1)
        except:
            pass


if __name__ == "__main__":
    main.main()
