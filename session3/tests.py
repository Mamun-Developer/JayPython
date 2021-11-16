from unittest import TestCase
from session3.task2 import print_multiplication_table_using_for_loop, print_multiplication_table_using_while_loop, \
    addition


class TestTask2(TestCase):
    def test_print_multiplication_table_using_for_loop(self):
        self.assertEqual(print_multiplication_table_using_for_loop(1), None)
        self.assertEqual(print_multiplication_table_using_for_loop(5), None)
        self.assertEqual(print_multiplication_table_using_for_loop(12), None)

    def test_print_multiplication_table_using_while_loop(self):
        self.assertEqual(print_multiplication_table_using_while_loop(1), None)
        self.assertEqual(print_multiplication_table_using_while_loop(5), None)
        self.assertEqual(print_multiplication_table_using_while_loop(12), None)

    def test_addition(self):
        self.assertEqual(3, addition(1, 2))
        self.assertEqual(13, addition(10, 3))
        self.assertEqual(0, addition(1, -1))
