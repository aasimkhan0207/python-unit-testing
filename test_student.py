import unittest
from unittest.mock import patch
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.std_1 = Student('asim', 'khan', 90)
        self.std_2 = Student('yash', 'sharma', 100)

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        print('test_email')
        self.assertEqual(self.std_1.email, 'asim.khan@email.com')
        self.assertEqual(self.std_2.email, 'yash.sharma@email.com')


    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.std_1.fullname, 'asim khan')
        self.assertEqual(self.std_2.fullname, 'yash sharma')

        self.std_1.first = 'kabir'
        self.std_2.first = 'mohit'

        self.assertEqual(self.std_1.fullname, 'kabir khan')
        self.assertEqual(self.std_2.fullname, 'mohit sharma')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.std_1.apply_raise()
        self.std_2.apply_raise()

        self.assertEqual(self.std_1.score, 94)
        self.assertEqual(self.std_2.score, 105.0)



if __name__ == '__main__':
    unittest.main()
