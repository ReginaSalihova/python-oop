class BaseObject:
    def __init__(self, x, y, z):
        self.coordinates = [x, y, z]

    def get_coordinates(self):
        return self.coordinates


class Block(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def shatter(self):
        self.coordinates = [None, None, None]


class Entity(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def move(self, x, y, z):
        self.coordinates = [x, y, z]


class Thing(BaseObject):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
