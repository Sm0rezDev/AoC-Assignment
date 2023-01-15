from AoC_2019_D2_P1 import int_code_interpreter

table = [
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

def test_int_code():
    for v in table:
        icp = int_code_interpreter(v['Test'])
        assert icp.execute() == v['Expected']