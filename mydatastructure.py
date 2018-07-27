import zlib

words = b'fuqiangmingzhuwenminghexie'

print(len(words))
words_comp = zlib.compress(words)
print(len(words_comp))


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()   # automatically validate the embedded tests

import unittest


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        # self.assertRaises()
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


# unittest.main()  # Calling from the command line invokes all tests


import tensorflow
import pprint

dir_tf = dir(tensorflow)
print(dir_tf)
pprint.pprint(dir_tf)