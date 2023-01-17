
class int_code_interpreter:

    def __init__(self, mem):
        self.mem = mem
        self.rc = 0


    @staticmethod
    def _parse(instruct):
        op_code = instruct % 100

        mode = instruct // 100
        mode1 = mode % 100
        mode //= 10
        mode2 = mode % 10
        mode //= 10
        mode3 = mode % 10

        return op_code, mode1, mode2, mode3


    def _idx(self, idx, mode):
        if mode == 0:
            return self.mem[idx]
        if mode == 1:
            return idx

    
    def execute(self):
        
        mem = self.mem
        idx = self._idx
        
        #i = 0
        #while True:
        for i in range(0, len(mem), 4):
            op_code, mode1, mode2, mode3 = self._parse(mem[i])

            if op_code == 1:
                #int_code[int_code[i+3]] = sum(int_code[int_code[i+j]] for j in [1,2])
                p_1 = mem[idx(i+1, mode1)]
                p_2 = mem[idx(i+2, mode2)]
                addr = idx(i+3, mode3)
                mem[addr] = p_1+p_2
                #i+=4 # steps forward 4 steps to next opcode.
            elif op_code == 2:
                #int_code[int_code[i+3]] = reduce(lambda x, y: x*y, (int_code[int_code[i+j]] for j in [1,2]))
                p_1 = mem[idx(i+1, mode1)]
                p_2 = mem[idx(i+2, mode2)]
                addr = idx(i+3, mode3)
                mem[addr] = p_1*p_2
                #i+=4 # steps forward 4 steps to next opcode.
            if op_code == 99:
                break # Halts when encounter opcode 99.


if __name__ == '__main__':
    with open('2019/2/input.txt', encoding='utf8') as f:
        data = list(map(int, f.read().split(',')))
    
    last_state = [12, 2]
    for idx, v in enumerate(last_state):
        data[idx+1] = v
    
    icp = int_code_interpreter(data.copy())
    icp.execute()
    print('[Part 1] Answer:', icp.mem[0])

    OUTPUT = None
    for noun in range(100):
        for verb in range(100):
            icp = int_code_interpreter(data.copy())
            mem = icp.mem
            mem[1] = noun
            mem[2] = verb
            icp.execute()

            if mem[0] == 19690720:
                OUTPUT = mem[0]
                break
        if OUTPUT is not None:
            break

    print('[PART 2] Answer:', 100 * noun + verb)