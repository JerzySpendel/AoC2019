from __future__ import annotations
import math
from decimal import Decimal as D


def sgn(x):
    return 1 if x >= 0 else -1


class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"<Point x: {self.x}, y: {self.y}>"

    def distance(self, p: Point):
        return ( (self.x - p.x) ** 2 + (self.y - p.y)**2 )**(1/2)


class LinearEquation:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2

    def point_matches(self, p3: Point) -> bool:
        return math.isclose(
            (D(self.p1.y) - D(self.p2.y)) * (D(self.p1.x) - D(p3.x)),
            (D(self.p1.y) - D(p3.y)) * (D(self.p1.x) - D(self.p2.x)),
            rel_tol=D('0.000001')
        )

    def __repr__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        return LinearEquation(*args, **kwargs)


asteroids = []
data = open('input', 'r').readlines()

for y, line in enumerate(data):
    line = line.strip()

    for x, value in enumerate(line):
        if value == '#':

            asteroids.append(
                Point(x, y)
            )

print(asteroids)

counter = {}

for index, fixed_asteroid in enumerate(asteroids):
    counter[fixed_asteroid] = 0
    print(index / len(asteroids)) # Progress bar, converges to 1

    for incrementing_asteroid in asteroids:
        should_increment = True

        if incrementing_asteroid is fixed_asteroid:
            continue

        le: LinearEquation = LinearEquation.create(fixed_asteroid, incrementing_asteroid)

        for other_asteroid in asteroids:

            if other_asteroid in [fixed_asteroid, incrementing_asteroid]:
                continue

            if le.point_matches(other_asteroid) and fixed_asteroid.distance(other_asteroid) < fixed_asteroid.distance(incrementing_asteroid) \
                    and sgn(fixed_asteroid.x - incrementing_asteroid.x) == sgn(fixed_asteroid.x - other_asteroid.x):
                should_increment = False
                break

        if should_increment:
            counter[fixed_asteroid] += 1



print(max(counter.values()))


