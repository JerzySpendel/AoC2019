from __future__ import annotations

import typing


class Node:
    kids: typing.Optional[typing.List[Node]] = None
    parent: typing.Optional[Node] = None

    def __init__(self, name, parent=None):
        self.name = name
        self.kids = []
        self.parent = parent

    def find(self, name):
        if self.name == name:
            return self

        for kid in self.kids:
            if kid.name == name:
                return kid

        for kid in self.kids:
            if node := kid.find(name):
                return node

        return None

    def change_parent(self, new_parent: Node):
        if old_parent := self.parent:
            old_parent.kids.remove(self)

        self.parent = new_parent

    def add_kid(self, node: Node):
        """
        Single responsibility mildly violated here :<
        """
        node.change_parent(self)
        self.kids.append(node)

    def get_all(self) -> typing.List[Node]:
        nodes = []

        for node in self.kids:
            nodes.append(node)
            nodes += node.get_all()

        return nodes

    def distance_to(self, node) -> typing.Optional[int]:
        if node == self:
            return 0

        return 1 + self.parent.distance_to(node)

    def path_to_root(self) -> typing.List[Node]:
        if self.parent is None:
            return []

        return [self.parent] + self.parent.path_to_root()

    def path_to_root_length(self, length=0) -> int:
        if self.parent is None:
            return length

        return self.parent.path_to_root_length(length + 1)
