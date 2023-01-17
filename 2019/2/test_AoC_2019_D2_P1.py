from AoC_2019_D2_P1 import int_code_interpreter

# Test part 1
table_part_1 = [
    {
        'Test': [1, 0, 0, 0, 99],
        'Expected': [2, 0, 0, 0, 99]
    },
    {
        'Test': [2, 3, 0, 3, 99],
        'Expected': [2, 3, 0, 6, 99]
    },
    {
        'Test': [2, 4, 4, 5, 99, 0],
        'Expected': [2, 4, 4, 5, 99, 9801]
    },
    {
        'Test': [1, 1, 1, 4, 99, 5, 6, 0, 99],
        'Expected': [30, 1, 1, 4, 2, 5, 6, 0, 99]
    },
]

def test_part_1():
    for v in table_part_1:
        icp = int_code_interpreter(v['Test'])
        icp.execute()
        assert icp.mem == v['Expected']


from time import sleep

def test_part_2():
    with open('2019/2/input.txt', encoding='utf8') as f:
        data = list(map(int, f.read().split(',')))

    output = None
    for noun in range(100):
        for verb in range(100):
            icp = int_code_interpreter(data.copy())
            mem = icp.mem
            mem[1] = noun
            mem[2] = verb
            icp.execute()

            if mem[0] == 19690720:
                output = mem[0]
                break
        if output is not None:
            break
    assert output == 19690720
            