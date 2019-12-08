from __future__ import annotations

from tree import Node

root = Node("COM")

relations = open('second_input', 'r').readlines()


def first(a_nodes, b_nodes):
    for node in a_nodes:
        if node in b_nodes:
            return node

    return None


for relation in relations:
    center_name, orbiter_name = relation.strip().split(')')

    if not (center_node := root.find(center_name)):
        center_node = Node(center_name)
        root.add_kid(center_node)

    if not (orbiter_node := root.find(orbiter_name)):
        orbiter_node = Node(orbiter_name)

    center_node.add_kid(orbiter_node)

you_node = root.find('YOU')
santa_node = root.find('SAN')

first_common_ancestor = first(you_node.path_to_root(), santa_node.path_to_root())
print(
    you_node.distance_to(first_common_ancestor) + santa_node.distance_to(first_common_ancestor) - 2
)


# print(
#     [node.name for node in you_node.path_to_root()]
# )
# print(
#     [node.name for node in santa_node.path_to_root()]
# )

# print(
#     root.find('D').distance_to(root.find('B'))
# )


