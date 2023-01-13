from math import floor

def operation(mass):
    res = floor(int(mass)/3) - 2
    return res
    

def module_fuel(_input):
    return [floor(int(x) / 3) - 2 for x in _input.splitlines()]


def fuel_need(_input):
    totalFuel = []
    for fuel in _input:
        _fuel_need = fuel
        totalFuel.append(_fuel_need)
        while(True):
            _fuel_need = operation(_fuel_need)
            if _fuel_need <= 0:
                break
            else:
                totalFuel.append(_fuel_need)
    return totalFuel

if __name__ == '__main__':
    with open('2019/1/input.txt') as f:
        data = f.read()

    print('Answer: ', sum(fuel_need(module_fuel(data))))

# Answer:  4994898
