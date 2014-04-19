import sys
sys.path.append('..')

from validator import Validator
import unittest


class ValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_validate_name_returns_none_on_valid_name(self):
        self.assertEqual(None, self.validator.validate_name(2, 'aa'))
        self.assertEqual(None, self.validator.validate_name(0, 'aa'))
        self.assertEqual(None, self.validator.validate_name(1, 'a'))

    def test_validate_name_raises_exception_on_invalid_name(self):
        self.assertRaises(Exception, self.validator.validate_name, 2, 'a')
        self.assertRaises(Exception, self.validator.validate_name, 1, '')

    def test_validate_number_returns_none_on_valid_number(self):
        self.assertEqual(None, self.validator.validate_number(1, 1))
        self.assertEqual(None, self.validator.validate_number(0, 0))
        self.assertEqual(None, self.validator.validate_number(0, 10))
        self.assertEqual(None, self.validator.validate_number(0, 3.56))
        self.assertEqual(None, self.validator.validate_number(0, 0.01))

    def test_validate_number_raises_exception_on_invalid_number(self):
        self.assertRaises(Exception, self.validator.validate_number, 2, 1)
        self.assertRaises(Exception, self.validator.validate_number, 0, -1)
        self.assertRaises(Exception, self.validator.validate_number, 1, 0)
        self.assertRaises(Exception, self.validator.validate_number, 2, 1.99)

    def test_validate_number_works_with_strings(self):
        self.assertEqual(None, self.validator.validate_number(1, '1'))
        self.assertEqual(None, self.validator.validate_number(0, '0'))
        self.assertEqual(None, self.validator.validate_number(0, '10'))
        self.assertEqual(None, self.validator.validate_number(0, '0.001'))

        self.assertRaises(Exception, self.validator.validate_number, 2, '1')
        self.assertRaises(Exception, self.validator.validate_number, 0, '-1')
        self.assertRaises(Exception, self.validator.validate_number, 1, '0')
        self.assertRaises(Exception, self.validator.validate_number, 1, '0.76')

    def test_validate_returns_none_on_valid_parameter(self):
        lambda_function = lambda x: x < 10
        self.assertEqual(None, self.validator.validate(lambda_function, 2, ''))

        lambda_function = lambda x: x ** 3 == 8
        self.assertEqual(None, self.validator.validate(lambda_function, 2, ''))

    def test_validate_raises_exception_on_invalid_parameter(self):
        lf = lambda x: x < 10
        self.assertRaises(Exception, self.validator.validate, lf, 20, '')

        lf = lambda x: x ** 3 == 8
        self.assertRaises(Exception, self.validator.validate, lf, 20, '')


if __name__ == '__main__':
    unittest.main()
