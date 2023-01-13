import unittest
from .AoC_P2 import module_fuel, fuel_need


class TestProcessInput(unittest.TestCase):
    def setUp(self):
        self.sample = '12\n14\n1969\n100756'
        self.fuel = module_fuel(self.sample)
    
    
    def test_module_fuel(self):
        self.assertEqual(module_fuel(self.sample), [2, 2, 654, 33583])


    def test_fuel_need(self):
        self.assertEqual(fuel_need(self.fuel), [
            2, 2,
            654, 216, 70, 21, 5,
            33583, 11192, 3728, 1240, 411, 135, 43, 12, 2
            ])

"""
test_fuel_need (2019.1.test_AoC_2019_D1_P2.TestProcessInput) ... ok
test_module_fuel (2019.1.test_AoC_2019_D1_P2.TestProcessInput) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
"""

