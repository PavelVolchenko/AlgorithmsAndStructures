class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def reverse_list(self):
        tail = None
        current = self.head
        while current:
            temp = current.next
            current.next = tail
            tail = current
            current = temp
        self.head = tail


arr = LinkedList()
[arr.append(i) for i in range(1, 10)]

arr.print_list()
arr.reverse_list()
arr.print_list()
