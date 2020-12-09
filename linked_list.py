from __future__ import annotations


class Node:
    def __init__(self, value, prev_node: Node = None, next_node: Node = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node
        # TODO: Implement self.prev_node for correct .pop() by index

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, value) -> None:
        if self.head:
            new_node = Node(value, next_node=self.head)
            self.head.prev_node = new_node
            self.head = new_node
        else:
            self.head = self.tail = Node(value)
        self.length += 1

    def append(self, value) -> None:
        if self.tail:
            new_node = Node(value)
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = self.tail = Node(value)
        self.length += 1

    def __contains__(self, item) -> bool:
        node = self.head
        while node:
            if node.value == item:
                return True
            node = node.next_node
        return False

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        node = self.head
        result = ""
        while node:
            result += str(node.value) + ", "
            node = node.next_node

        result = result.strip(", ")
        return "[" + result + "]"

    def __getitem__(self, item):
        if item > len(self) - 1 or item < len(self) - 1:
            raise IndexError(f"Index error, {item} not in LinkedList")
        node = self.head
        counter = 0
        while node:
            if item == counter:
                return node
            counter += 1
            node = node.next_node

    def pop(self, index: int = None):
        """
        The method removes object from Linked List. If it have used without index,
        the method removes item from end and returns value.
        O(n)
        """
        if not index:
            index = len(self) - 1
        if not self.head:
            raise IndexError("Linked List is empty")
        node = self.head
        prev_node = node
        counter = 0
        while node:
            if counter == index:
                prev_node.next_node = node.next_node
                self.length -= 1
                return node.value
            counter += 1
            prev_node = node
            node = node.next_node
        raise IndexError("Index out of range")
