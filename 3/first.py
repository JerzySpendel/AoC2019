from __future__ import annotations

import heapq
import typing

data = open('input', 'r').readlines()
wires = [wire_data.split(',') for wire_data in data]


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @property
    def manhattan(self):
        return abs(self.x) + abs(self.y)

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"<Point x: {self.x}, y: {self.y}>"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return hash(self) == hash(other)


def wire_data_to_points(wire_data: typing.List[str]):
    points = [Point(0, 0)]
    for instruction in wire_data:
        last_point = points[-1]
        points += generate_points(last_point, instruction)

    return points


def generate_points(starting_point: Point, instruction):
    direction = instruction[0]
    direction_value = int(instruction[1:])

    if direction == 'U':
        dp = Point(0, 1)
    elif direction == 'D':
        dp = Point(0, -1)
    elif direction == 'R':
        dp = Point(1, 0)
    else:
        dp = Point(-1, 0)

    new_points = [starting_point + dp]

    for _ in range(2, direction_value + 1):
        new_points.append(new_points[-1] + dp)

    return new_points


points_1 = wire_data_to_points(wires[0])
points_2 = wire_data_to_points(wires[1])

intersections = set(points_1) & set(points_2)

print(intersections)

print(
    heapq.nsmallest(3, intersections, key=lambda obj: obj.manhattan)
)


