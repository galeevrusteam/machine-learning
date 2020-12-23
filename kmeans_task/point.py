class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.values()))

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y

    def __str__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
