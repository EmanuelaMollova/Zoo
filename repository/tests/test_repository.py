import sys
sys.path.append('..')

from repository import Repository
import unittest


class RepositoryTest(unittest.TestCase):

    def setUp(self):
        self.r = Repository('../../database/zoos_test_database.db')

    def test_is_name_used(self):
        self.assertTrue(self.r.is_name_used('species', 'lion'))
        self.assertTrue(not self.r.is_name_used('species', 'dog'))

        self.assertTrue(self.r.is_name_used('zoos', 'Zoo Sofia'))
        self.assertTrue(not self.r.is_name_used('zoos', 'My Awesome Zoo'))

        self.assertTrue(self.r.is_name_used('animals', 'Hippi'))
        self.assertTrue(not self.r.is_name_used('animals', 'Im Bad At Naming'))


if __name__ == '__main__':
    unittest.main()
