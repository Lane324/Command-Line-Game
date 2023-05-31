from threading import Thread
import movement
import game
import objects


def main():
    field = objects.Field(x_size=10, y_size=5, symbol="-")
    character = objects.Character(x_pos=5, y_pos=5, symbol="0", speed=0.1)
    point = objects.Point(x_pos=1, y_pos=1, symbol="X")
    timer = objects.Timer(length=30)
    speedIncrement = 0.015

    exitThread = Thread(target=game.exitGame, args=(character, "highscore.txt"))
    gameThread = Thread(
        target=game.game,
        args=(field, character, point, timer, speedIncrement),
        daemon=True,
    )
    timerThread = Thread(target=game.timer, args=(timer,), daemon=True)
    playerMovementThread = Thread(
        target=movement.move_player, args=(character, field), daemon=True
    )
    pointMovementThread = Thread(
        target=movement.move_point, args=(point, field), daemon=True
    )

    exitThread.start()
    gameThread.start()
    timerThread.start()
    playerMovementThread.start()
    pointMovementThread.start()


if __name__ == "__main__":
    main()
