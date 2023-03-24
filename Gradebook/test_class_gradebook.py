import unittest
from class_gradebook import Gradebook
from class_messages import Messages


class TestGradebook(unittest.TestCase):

    def setUp(self):
        self.gradebook = Gradebook()

    def test_gradebook_init(self):
        self.assertEqual(self.gradebook.gradebook, {})

    def test_add_student(self):
        # Test adding a student with valid input
        result = self.gradebook.add_student('Alice', 21, 'Computer Science')
        self.assertEqual(result, Messages.STUDENT_ADDED_SUCCESSFULLY)
        self.assertIn('Alice', self.gradebook.gradebook.keys())

        # Test adding a student with a duplicate name
        result = self.gradebook.add_student('Alice', 22, 'Mathematics')
        self.assertEqual(result, Messages.STUDENT_ALREADY_EXISTS)

        # Test adding a student with an invalid name
        result = self.gradebook.add_student('', 20, 'English')
        self.assertEqual(result, Messages.INVALID_NAME)

        # Test adding a student with age not added
        result = self.gradebook.add_student('Bob', '', 'History')
        self.assertEqual(result, Messages.AGE_NOT_ADDED)

        # Test adding a student with major not added
        result = self.gradebook.add_student('Charlie', 19, '')
        self.assertEqual(result, Messages.MAJOR_NOT_ADDED)


if __name__ == '__main__':
    unittest.main()
