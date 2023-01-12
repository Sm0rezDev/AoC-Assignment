from math import floor

def required_fuel(_input):
    return [floor(int(mass)/3)-2 for mass in _input.splitlines()]
