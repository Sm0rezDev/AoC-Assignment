import unittest
from .AoC_P1 import required_fuel

class TestProcessInput(unittest.TestCase):
    sample = '12\n14\n1969\n100756'

    def test_required_fuel(self):
        result = [2, 2, 654, 33583]
        self.assertEqual(required_fuel(self.sample), result)

"""
test_required_fuel (2019.1.test_AoC_P1.TestProcessInput) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""