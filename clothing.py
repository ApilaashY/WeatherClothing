class Clothing:
    def __init__(self, name, points, typeof):
        self.name = name
        self.points = points
        self.type = typeof
    def __str__(self) -> str:
        return f"{self.name}: {self.points} points"