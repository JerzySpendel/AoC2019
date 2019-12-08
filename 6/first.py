from __future__ import annotations

from tree import Node

root = Node("COM")

relations = open('input', 'r').readlines()
for relation in relations:
    center_name, orbiter_name = relation.strip().split(')')

    if not (center_node := root.find(center_name)):
        center_node = Node(center_name)
        root.add_kid(center_node)

    if not (orbiter_node := root.find(orbiter_name)):
        orbiter_node = Node(orbiter_name)

    center_node.add_kid(orbiter_node)


print('Done!')

summarum = 0
for node in root.get_all():
    summarum += node.path_to_root_length()
print(summarum)
