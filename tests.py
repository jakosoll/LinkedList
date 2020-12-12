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

    def test_insert_not_raises_with_zero_value(self):
        self.list_.insert(0)
        self.assertIn(0, self.list_)

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
        self.list_.append(self.second)  # insert element in end
        self.list_.pop()
        self.assertEqual(str(self.list_), f'[{self.first}]')

    def test_pop_remove_first_element_by_zero_index(self):
        """Test: .pop with index return and remove element by index"""
        self.list_.insert(self.third)
        self.list_.insert(self.second)
        self.list_.insert(self.first)  # 0
        first = self.list_.pop(0)
        self.assertNotIn(self.first, self.list_)
        self.assertEqual(self.first, first)

    def test_length_after_pop_value(self):
        self.list_.insert(self.second)
        self.list_.insert(self.third)
        self.list_.pop(0)
        self.assertEqual(1, len(self.list_))

    def test_remove_element_by_first_and_last(self):
        self.list_.insert(self.first)
        self.list_.append(self.second)
        self.list_.append(self.third)
        second = self.list_.pop(1)

        self.assertNotIn(self.second, self.list_)
        self.assertEqual(second, self.second)

        self.list_.pop()
        self.assertNotIn(self.third, self.list_)


class TestAppend(unittest.TestCase):
    def setUp(self) -> None:
        self.list_ = LinkedList()
        self.first = 'First'
        self.second = 'Second'
        self.third = 'Third'
        self.fourth = 'Fourth'

    def test_append_add_element_at_end_of_list(self):
        """Test: .append adds element at end of list"""
        self.list_.insert(self.first)
        self.list_.append(self.second)
        self.assertIn(self.second, self.list_)
        self.assertEqual(str(self.list_), f'[{self.first}, {self.second}]')

    def test_length_after_append_element(self):
        """Test: length of list change after append element"""
        self.list_.insert(self.first)
        self.assertEqual(len(self.list_), 1)
        self.list_.append(self.second)
        self.assertEqual(len(self.list_), 2)

    def test_append_element_in_empty_list(self):
        """Test: .append can add elements to end of list
        when list is empty"""
        self.list_.append(self.first)
        self.assertEqual(len(self.list_), 1)
        self.assertEqual(str(self.list_), f'[{self.first}]')


if __name__ == "__main__":
    unittest.main()
