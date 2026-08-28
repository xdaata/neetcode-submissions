class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point
        if (x, y) in self.points:
            self.points[(x, y)] += 1
        else:
            self.points[(x, y)] = 1 

    def count(self, point: List[int]) -> int:
        answ = 0
        px, py = point
        for x, y in self.points:
            if abs(px - x) == abs(py - y) and px != x and py != y:
                if (x, py) in self.points and (px, y) in self.points:
                    answ += self.points[(x, py)] * self.points[(px, y)] * self.points[(x, y)]
        return answ        
