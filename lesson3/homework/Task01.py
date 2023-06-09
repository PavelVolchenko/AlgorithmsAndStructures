from dataclasses import dataclass

@dataclass
class Node:
    data: object = None
    next: object = None

@dataclass
class LinkedList:
    head: object = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse_list(self, tail=None):
        current = self.head
        while current:
            temp, current.next, tail = current.next, tail, current
            current = temp
        self.head = tail


arr = LinkedList()
[arr.append(i) for i in range(1, 10)]

arr.print_list()
arr.reverse_list()
arr.print_list()
