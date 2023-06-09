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


arr = LinkedList()
[arr.append(i) for i in range(1, 10)]
arr.print_list()

