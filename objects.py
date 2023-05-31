import main


class Field:
    def __init__(self, x_size=None, y_size=None, symbol=""):
        self.x_size = x_size
        self.y_size = y_size
        self.symbol = symbol


class Character:
    def __init__(self, x_pos, y_pos, symbol, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.symbol = symbol
        self.score = 0
        self.speed = speed


class Point:
    def __init__(self, x_pos, y_pos, symbol):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.symbol = symbol


class Timer:
    def __init__(self, length):
        self.length = length


if __name__ == "__main__":
    main.main()
