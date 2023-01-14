from AoC_2019_D2_P1 import int_process

int_code = [
    [1, 0, 0, 0, 99],
    [2, 3, 0, 3, 99],
    [2, 4, 4, 5, 99, 0],
    [1, 1, 1, 4, 99, 5, 6, 0, 99]
]


def test_one():
    assert int_process(int_code[0]) == [2, 0, 0, 0, 99]

def test_two():
    assert int_process(int_code[1]) == [2, 3, 0, 6, 99]

def test_three():
    assert int_process(int_code[2]) == [2, 4, 4, 5, 99, 9801]

def test_four():
    assert int_process(int_code[3]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

