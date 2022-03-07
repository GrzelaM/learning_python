from linked_list import LinkedList
from io import StringIO
import sys

class TestLinkedList:

    def test_create_list(self):
        l = LinkedList()
        assert isinstance(l, LinkedList)

    def test_size_of_list(self):
        #given
        l = LinkedList()
        #when
        l.add_value(1)
        l.add_value(1)
        #then
        assert l.size_of_list == 2

    def test_size_of_list_2(self):
        l = LinkedList()
        assert l.size_of_list == 0

    def test_del_n_items(self):
        l = LinkedList()
        l.add_value(203)
        l.add_value(2)
        l.add_value(23)
        l.add_value(13)
        l.delete_n_elements(3)
        assert l.size_of_list == 1

    def test_print_list(self):
        printOutput = StringIO()
        sys.stdout = printOutput
        l = LinkedList()
        l.add_value(200)
        l.print_list()
        sys.stdout = sys.__stdout__
        assert printOutput.getvalue() == "200\n"

    def test_print_n_elements(self):
        printOutput = StringIO()
        sys.stdout = printOutput
        l = LinkedList()
        l.add_value(100)
        l.add_value(200)
        l.add_value(300)
        l.add_value(400)
        l.add_value(500)
        l.print_n_elements(3)
        sys.stdout = sys.__stdout__
        assert printOutput.getvalue() == "100\n200\n300\n"