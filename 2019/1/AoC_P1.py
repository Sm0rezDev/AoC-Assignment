import unittest
import math

def ProcessInput(_input):
    return [math.floor(int(mass)/3)-2 for mass in _input.splitlines()]


class TestProcessInput(unittest.TestCase):
    sample = "12\n14\n1969\n100756"

    def test_ProcessInput(self):
        result = [2, 2, 654, 33583]
        self.assertEqual(ProcessInput(self.sample), result)


if __name__ == '__main__':
    with open('2019/1/input.data') as f:
        data = f.read()

    print(sum(ProcessInput(data)))


"""
[TEST]

test_ProcessInput (2019.1.AoC_P1.TestProcessInput) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK


[RESULTS]: 3331849
"""
    