from enum import IntEnum
from time import sleep


class DirectionChoices(IntEnum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Cell:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._contents = []

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def add_content(self, obj):
        self._contents.append(obj)

    def remove_content(self, obj):
        self._contents.remove(obj)

    def __str__(self):
        return "".join([str(content) for content in self._contents])


class Map:

    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width
        self._board = []

    def get_width(self):
        return self._width

    def get_height(self):
        return self._length

    def initialize(self, file_name=None):
        for x in range(self._length):
            row = []
            for y in range(self._width):
                cell = Cell(x=x, y=y)
                cell.add_content("*")
                row.append(cell)

            self._board.append(row)

    def print_board(self):
        boarder = "".join(["-" * (4 * self._width + 1)])
        print(boarder)
        for x in range(self._length):
            row = "| " + " | ".join([str(cell) for cell in self._board[x]]) + " |"
            print(row)
            print(boarder)

    def remove_content(self, x, y, obj):
        self._board[x][y].remove_content(obj)

    def add_content(self, x, y, obj):
        self._board[x][y].add_content(obj)

    def move_content(self, old_x, old_y , new_x, new_y, obj):
        self.remove_content(old_x, old_y, obj)
        self.add_content(new_x, new_y, obj)


class Obj:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Movable(Obj):

    def __init__(self, x, y, speed) -> None:
        self._speed = speed
        super(Movable, self).__init__(x, y)

    def _move(self, map: Map, direction: int):
        prev_x = self._x
        prev_y = self._y

        if direction == DirectionChoices.LEFT.value:
            new_x = prev_x - self._speed
            new_y = prev_y

        elif direction == DirectionChoices.RIGHT.value:
            new_x = self._x + self._speed
            new_y = self._y

        elif direction == DirectionChoices.UP.value:
            new_x = self._x
            new_y = self._y - self._speed

        else:
            new_x = self._x
            new_y = self._y + self._speed

        # destroy obj when it reaches to the end of map
        if new_x < 0 or new_y < 0 or map.get_width() < new_x or map.get_height() < new_y:
            map.remove_content(prev_x, prev_y, self)
        else:
            map.move_content(prev_x, prev_y, new_x, new_y, self)
            self._x = new_x
            self._y = new_y

    def move_right(self, map: Map):
        self._move(map, DirectionChoices.RIGHT.value)

    def move_left(self, map: Map):
        self._move(map, DirectionChoices.LEFT.value)

    def move_up(self, map: Map):
        self._move(map, DirectionChoices.UP.value)

    def move_down(self, map: Map):
        self._move(map, DirectionChoices.DOWN.value)


class Bullet(Movable):

    def __init__(self, x, y, damage, speed) -> None:
        self._damage = damage
        super(Bullet, self).__init__(x, y, speed)

    def move(self, map) -> None:
        self.move_right(map)


class Plant(Obj):

    def __init__(self, x, y, hp) -> None:
        self._hp = hp
        super(Plant, self).__init__(x, y)

    def shoot(self):
        pass

    def __str__(self):
        return f"P: ({self._x}, {self._y})"


class SunFlower(Plant):

    def __init__(self, x, y, hp, sun_rate) -> None:
        self._x = x
        self._y = y
        self._hp = hp
        self._sun_rate = sun_rate
        super(SunFlower, self).__init__(x, y, hp)

    def shoot(self):
        pass

    def __str__(self):
        return f"SF: ({self._x}, {self._y})"


class WeakPlant(Plant):

    def __init__(self, x, y, hp, attack_power, attack_speed) -> None:
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        super(WeakPlant, self).__init__(x, y, hp)

    def shoot(self):
        pass

    def __str__(self):
        return f"WP: ({self._x}, {self._y})"


class StrongPlant(Plant):

    def __init__(self, x, y, hp, attack_power, attack_speed) -> None:
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        super(StrongPlant, self).__init__(x, y, hp)

    def shoot(self):
        pass

    def __str__(self):
        return f"SP: ({self._x}, {self._y})"


class Zombie(Movable):

    def __init__(self, x, y, hp, attack_power, attack_speed, movement_speed) -> None:
        self._hp = hp
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        self._movement_speed = movement_speed
        super(Zombie, self).__init__(x, y)

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def move(self, map):
        pass

    def attack(self, map):
        pass


class WeakZombie(Zombie):

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

        attack_power = 10
        attack_speed = 5
        movement_speed = 5

        super(WeakZombie, self).__init__(x, y, hp, attack_power, attack_speed, movement_speed)

    def move(self, map):
        pass

    def attack(self, map):
        pass


class StrongZombie(Zombie):

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

        attack_power = 10
        attack_speed = 5
        movement_speed = 5

        super(StrongZombie, self).__init__(x, y, hp, attack_power, attack_speed, movement_speed)

    def move(self, map):
        pass

    def attack(self, map):
        pass


class Engine:

    def __init__(self) -> None:
        pass

    def run(self):
        # map
        map = Map(5, 10)
        map.initialize()
        map.print_board()

        weak_plant = WeakPlant(0, 0, 100, 20, 2)
