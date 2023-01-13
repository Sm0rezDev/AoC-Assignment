from math import floor

def required_fuel(_input):
    return [floor(int(mass)/3)-2 for mass in _input.splitlines()]


if __name__ == '__main__':
    with open('2019/1/input.txt') as f:
        data = f.read()

    print(sum(required_fuel(data)))
    
    # [RESULTS]: 3331849