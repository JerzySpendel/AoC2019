import typing
from __future__ import annotations


data = open('input', 'r').readlines()
wires = [wire_data.split(',') for wire_data in data]


def wire_data_to_points(wire_data, points=None):
    """
    Transforms data about one wire to list of 2-item tuples that represents points that the wire go through
    """
    points = points or []

    if not wire_data:
        return points

    instruction = wire_data[0][0]
    instruction_value = int(wire_data[0][1:])

    if not points:
        current_point = 0, 0
    else:
        current_point = points[-1]

    if instruction == 'U':
        new_point = (current_point[0], current_point[1] + instruction_value)
    elif instruction == 'R':
        new_point = (current_point[0] + instruction_value, current_point[1])
    elif instruction == 'L':
        new_point = (current_point[0] - instruction_value, current_point[1])
    elif instruction == 'D':
        new_point = (current_point[0], current_point[1] - instruction_value)

    return wire_data_to_points(wire_data[1:], points + [new_point])


def get_intersections(wire_1: typing.List[typing.Tuple[int, int]], wire_2: typing.List[typing.Tuple[int, int]]):
    pass


points_from_wire_1 = wire_data_to_points(wires[0])
points_from_wire_2 = wire_data_to_points(wires[1])

intersections = set(points_from_wire_1) & set(points_from_wire_2)
print(intersections)
