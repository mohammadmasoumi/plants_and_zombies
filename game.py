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
        return "-".join([str(content) for content in self._contents]).center(10)


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
                row.append(cell)

            self._board.append(row)

    def print_board(self):
        boarder = "".join(["-" * (11 * self._width + 1)])
        print(boarder)

        for x in range(self._length):
            row = "|" + "|".join([str(cell).ljust(10) for cell in self._board[x]]) + "|"
            print(row)
            print(boarder)

    def remove_content(self, x, y, obj):
        self._board[x][y].remove_content(obj)

    def add_content(self, x, y, obj):
        self._board[x][y].add_content(obj)

    def move_content(self, old_x, old_y, new_x, new_y, obj):
        self.remove_content(old_x, old_y, obj)
        self.add_content(new_x, new_y, obj)


class Obj:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
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

    def __str__(self):
        return "B"


class Plant(Obj):

    def __init__(self, x, y, hp) -> None:
        self._hp = hp
        super(Plant, self).__init__(x, y)

    def plant(self, map):
        map.add_content(self._x, self._y, self)

    def __str__(self):
        return f"P: ({self._x}, {self._y})"


class ArmoredPlant(Plant):

    def __init__(self, x, y, hp, attack_speed, attack_power):
        self._attack_power = attack_power
        self._attack_speed = attack_speed

        super(ArmoredPlant, self).__init__(x, y, hp)

    def shoot(self, map):
        bullet = Bullet(self._x, self._y, self._attack_power, self._attack_speed)
        map.add_content(bullet.x, bullet.y, bullet)


class SunFlower(Plant):

    def __init__(self, x, y, hp, sun_rate) -> None:
        self._x = x
        self._y = y
        self._hp = hp
        self._sun_rate = sun_rate
        super(SunFlower, self).__init__(x, y, hp)

    def __str__(self):
        return f"SF"


class WeakPlant(ArmoredPlant):

    def __init__(self, x, y, hp, attack_speed, attack_power) -> None:
        super(WeakPlant, self).__init__(x, y, hp, attack_speed, attack_power)

    def __str__(self):
        return f"WP"


class StrongPlant(ArmoredPlant):

    def __init__(self, x, y, hp, attack_speed, attack_power) -> None:
        super(StrongPlant, self).__init__(x, y, hp, attack_speed, attack_power)

    def __str__(self):
        return f"SP"


class Zombie(Movable):

    def __init__(self, x, y, hp, speed, attack_power, attack_speed) -> None:
        self._hp = hp
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        super(Zombie, self).__init__(x, y, speed)

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

        speed = 1
        attack_power = 10
        attack_speed = 5

        super(WeakZombie, self).__init__(x, y, hp, speed, attack_power, attack_speed)

    def move(self, map):
        pass

    def attack(self, map):
        pass

    def __str__(self):
        return "WZ"


class StrongZombie(Zombie):

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

        speed = 1
        attack_power = 10
        attack_speed = 5

        super(StrongZombie, self).__init__(x, y, hp, speed, attack_power, attack_speed)

    def move(self, map):
        pass

    def attack(self, map):
        pass

    def __str__(self):
        return "SZ"


class Engine:

    def __init__(self) -> None:
        pass

    def run(self):
        # map
        map = Map(5, 10)
        map.initialize()

        week_plant = WeakPlant(0, 0, 100, 20, 2)
        week_plant.plant(map)
        week_plant.shoot(map)

        map.print_board()


if __name__ == '__main__':
    engine = Engine()
    engine.run()
