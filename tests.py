import unittest
from linked_list import LinkedList
from linked_list import Node


class LinkedListTest(unittest.TestCase):
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

    def test_has_insert_method(self):
        self.assertTrue(hasattr(self.list_, 'insert'))

    def test_insert_save_first_in_head(self):
        self.assertEqual(str(self.list_.head), "First")

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
        Test: we can check 'elem' in list
        """
        self.list_.insert(self.second)
        self.assertIn(self.first, self.list_)
        self.assertIn(self.second, self.list_)

    def test_elem_not_in_list(self):
        self.list_.insert(self.second)
        self.assertNotIn(self.third, self.list_)


if __name__ == "__main__":
    unittest.main()

