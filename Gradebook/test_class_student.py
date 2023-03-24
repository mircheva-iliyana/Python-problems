import unittest
from class_student import Student


class TestStudent(unittest.TestCase):

    def test_student_str(self):
        s = Student("John Doe", 20, "Computer Science", {"Math": 90, "History": 80})
        self.assertEqual(str(s), "John Doe, 20, Computer Science, {'Math': 90, 'History': 80}")

    def test_student_init(self):
        s = Student("Jane Doe", 18, "English")
        self.assertEqual(s.name, "Jane Doe")
        self.assertEqual(s.age, 18)
        self.assertEqual(s.major, "English")
        self.assertEqual(s.subjects, {})


if __name__ == '__main__':
    unittest.main()