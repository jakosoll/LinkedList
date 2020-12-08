import unittest
from linked_list import LinkedList
from linked_list import Node


class BaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()
        self.first = 'First'
        self.second = 'Second'
        self.third = 'Third'
        self.fourth = 'Fourth'

        self.list_.insert(self.first)

    def test_create_linked_list(self):
        self.assertIsInstance(self.list_, LinkedList)

    def test_head_in_linked_list(self):
        self.assertTrue(hasattr(self.list_, 'head'))

    def test_next_in_linked_list(self):
        self.assertTrue(hasattr(self.list_, 'length'))

    def test_length_list_with_two_elements(self):
        """Test: len() for Linked List"""
        self.list_.insert(self.second)
        self.assertEqual(len(self.list_), 2)

    def test_length_list_with_more_elements(self):
        self.list_.insert(self.second)
        self.list_.insert(self.third)
        self.assertEqual(len(self.list_), 3)
        self.list_.insert(self.fourth)
        self.assertEqual(len(self.list_), 4)

    def test_has_insert_method(self):
        self.assertTrue(hasattr(self.list_, 'insert'))

    def test_print(self):
        self.list_.insert(self.second)
        self.assertEqual(str(self.list_), f"[{self.second}, {self.first}]")


class InsertTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()
        self.first = 'First'
        self.second = 'Second'
        self.third = 'Third'
        self.fourth = 'Fourth'

        self.list_.insert(self.first)

    @unittest.expectedFailure
    def test_insert_not_raises_with_zero_value(self):
        self.list_.insert(0)
        self.assertEqual(self.list_.head, 0)

    def test_insert_save_first_in_head(self):
        """
        Test: insert saves value in head of list
        """
        self.assertEqual(str(self.list_[0]), self.first)

    def test_head_is_node_instance(self):
        self.assertIsInstance(self.list_.head, Node)

    def test_correct_insert_two_elem_in_list(self):
        """
        Test: we can save two element in list.
        The second elem becomes the first and has link to the first
        """
        self.list_.insert(self.second)
        self.assertEqual(str(self.list_.head), "Second")
        self.assertTrue(hasattr(self.list_.head, "next_node"))
        self.assertEqual(str(self.list_.head.next_node), self.first)

    def test_elements_in_list(self):
        """
        Test: check 'elements' in list
        """
        self.list_.insert(self.second)
        self.assertIn(self.first, self.list_)
        self.assertIn(self.second, self.list_)

    def test_elem_not_in_list(self):
        """
        Test: element not in list
        """
        self.list_.insert(self.second)
        self.assertNotIn(self.third, self.list_)


class RemoveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()
        self.first = 'First'
        self.second = 'Second'
        self.third = 'Third'
        self.fourth = 'Fourth'

    def test_raise_exception_if_list_empty(self):
        """Test: if list is empty, exception was raising"""
        with self.assertRaises(IndexError):
            self.list_.pop()

    def test_pop_remove_last_element(self):
        """Test: .pop without index return and remove last element"""
        self.list_.insert(self.first)
        self.list_.insert(self.second)  # insert element in head
        self.list_.pop()
        self.assertEqual(str(self.list_), f'[{self.second}]')


if __name__ == "__main__":
    unittest.main()
