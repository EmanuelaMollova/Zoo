import sys
sys.path.append('..')
sys.path.append('../../helpers')

from zoo import Zoo
import unittest


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo('Sofia Zoo', 100, 1000)

    def test_creating_invalid_zoo_raises_exception(self):
        self.assertRaises(Exception, Zoo, 'a', 5, 6)
        self.assertRaises(Exception, Zoo, 'aaa', -5, 6)
        self.assertRaises(Exception, Zoo, 'aaa', 0, 6)
        self.assertRaises(Exception, Zoo, 'aaa', 5, -1)
        self.assertRaises(Exception, Zoo, 'a', 0, -1)

    def test_creating_valid_zoo_objects(self):
        self.assertEqual('Zoo', type(Zoo('aaa', 2, 3)).__name__)

    def test_getters(self):
        self.assertEqual('Sofia Zoo', self.zoo.name)
        self.assertEqual(100, self.zoo.capacity)
        self.assertEqual(1000, self.zoo.budget)

    def test_setters(self):
        self.zoo.name = 'Varna Zoo'
        self.assertEqual('Varna Zoo', self.zoo.name)

        self.zoo.capacity = 500
        self.assertEqual(500, self.zoo.capacity)

        self.zoo.budget = 500
        self.assertEqual(500, self.zoo.budget)


if __name__ == '__main__':
    unittest.main()
