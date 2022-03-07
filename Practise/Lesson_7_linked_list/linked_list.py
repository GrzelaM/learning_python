class Node:

    def __init__(self, x_value, next_node=None):
        self.x_value = x_value
        self.next_node = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size_of_list = 0

    def add_value(self, x_value):
        newNode = Node(x_value)

        if self.head:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = newNode
        else:
            self.head = newNode

        self.size_of_list += 1


    def print_list(self):
        if self.size_of_list == 0:
            print("Lista nie posiada żadnych elementów")
        else:
            pointer_to_node = self.head
            while pointer_to_node:
                print(pointer_to_node.x_value)
                pointer_to_node = pointer_to_node.next_node

    def print_n_elements(self, n):
        if n > self.size_of_list:
            print("Chcesz wypisać więcej elementów, niż posiada lista")
        else:
            pointer_to_node = self.head
            for i in range(n):
                print(pointer_to_node.x_value)
                pointer_to_node = pointer_to_node.next_node

    def delete_n_elements(self, n):
        if n > self.size_of_list:
            print("Chcesz usunąć więcej elementów, niż posiada lista")
        else:
            pointer_to_node = self.head
            for i in range(n):
                pointer_to_node = pointer_to_node.next_node
            self.head = pointer_to_node

        self.size_of_list -= n

l = LinkedList()
l.add_value(1)
l.add_value(2)
l.add_value(3)
l.add_value(4)
l.add_value(5)
l.print_list()
print("X"*100)
l.print_n_elements(3)
print("X"*100)
l.delete_n_elements(2)
l.print_list()
