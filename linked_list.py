from __future__ import annotations


class Node:
    def __init__(self, value, next_node: Node = None):
        self.value = value
        self.next_node = next_node

    def __repr__(self) -> None:
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, value) -> None:
        if self.head:
            new_node = Node(value, self.head)
            self.head = new_node
        else:
            self.head = Node(value)
        self.length += 1

    def __contains__(self, item):
        node = self.head
        while node:
            if node.value == item:
                return True
            node = node.next_node
        return False

    def __len__(self):
        return self.length

