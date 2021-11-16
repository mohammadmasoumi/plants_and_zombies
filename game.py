from enum import IntEnum


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
    
    def move_content(self, x, y, obj):
        pre_x = obj.x
        pre_y = obj.y
        
        self.add_content(x, y, obj)
        self.remove_content(pre_x, pre_y, obj)
            

class Bullet:

    def __init__(self, x, y, damage, speed) -> None:
        self._x = x
        self._y = y
        self._damage = damage
        self._speed = speed 
    
    def move(self, map) -> None:
        pass


class Movable:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def move(self, direction):
        if direction == DirectionChoices.LEFT.value:
            self._x -= 1
        elif direction == DirectionChoices.RIGHT.value:
            self._x += 1
        elif direction == DirectionChoices.UP.value:
            self._y -= 1
        else:
            self._y += 1
        

class Plant:

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

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

    def shoot(self):
        pass

    def __str__(self):
        return f"SF: ({self._x}, {self._y})"


def WeakPlant(Plant):

    def __init__(self, x, y, hp, attack_power, attack_speed) -> None:
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        super(Plant, self).__init__(x, y, hp)

    def shoot(self):
        pass

    def __str__(self):
        return f"WP: ({self._x}, {self._y})"


def StrongPlant(Plant):

    def __init__(self, x, y, hp, attack_power, attack_speed) -> None:
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        super(Plant, self).__init__(x, y, hp)

    def shoot(self):
        pass

    def __str__(self):
        return f"SP: ({self._x}, {self._y})"


class Zombie:

    def __init__(self, x, y, hp, attack_power, attack_speed, movement_speed) -> None:
        self._x = x
        self._y = y
        self._hp = hp
        self._attack_power = attack_power
        self._attack_speed = attack_speed
        self._movement_speed = movement_speed

    def get_hp(self):
        return self._hp

    def set_hp(self, hp):
        self._hp = hp

    def move(self, x, y):
        self._x = x
        self._y = y
        
    def attack(self, map):
        pass


class WeakZombie(Zombie):

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

        attack_power  = 10
        attack_speed = 5
        movement_speed = 5

        super(Zombie, self).__init__(x, y, hp, attack_power, attack_speed, movement_speed)


    def move(self, map):
        pass

    def attack(self, map):
        pass


class StrongZombie(Zombie):

    def __init__(self, x, y, hp) -> None:
        self._x = x
        self._y = y
        self._hp = hp

        attack_power  = 10
        attack_speed = 5
        movement_speed = 5

        super(Zombie, self).__init__(x, y, hp, attack_power, attack_speed, movement_speed)


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

        