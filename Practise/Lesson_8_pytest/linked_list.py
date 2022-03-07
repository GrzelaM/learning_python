class Node:

    def __init__(self, x_value, next_node=None):
        self.x_value = x_value
        self.next_node = next_node

class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size_of_list = 0

    def get_list_size(self):
        return print(f"Rozmiar listy wynosi: {self.size_of_list}")

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

