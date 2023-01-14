
from functools import reduce


def int_process(int_code):
    i = 0
    while True:
        if int_code[i] == 1:
            int_code[int_code[i+3]] = sum(
                int_code[int_code[i+j]] for j in [1,2])
        elif int_code[i] == 2:
            int_code[int_code[i+3]] = reduce(
                lambda x, y: x*y, (int_code[int_code[i+j]] for j in [1,2]))

        i+=4 # steps forward 4 steps to next opcode.
        if int_code[i] == 99:
            break # Halts when encounter opcode 99.
    return int_code



if __name__ == '__main__':
    pass
