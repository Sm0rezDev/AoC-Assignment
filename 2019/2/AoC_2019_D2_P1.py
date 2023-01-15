
class int_code_interpreter:

    def __init__(self, mem):
        self.mem = mem


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
        
        i = 0
        while True:
            op_code, mode1, mode2, mode3 = self._parse(mem[i])

            if op_code == 1:
                #int_code[int_code[i+3]] = sum(int_code[int_code[i+j]] for j in [1,2])
                p1 = mem[idx(i+1, mode1)]
                p2 = mem[idx(i+2, mode2)]
                addr = idx(i+3, mode3)
                mem[addr] = p1+p2
                i+=4
            elif op_code == 2:
                #int_code[int_code[i+3]] = reduce(lambda x, y: x*y, (int_code[int_code[i+j]] for j in [1,2]))
                p1 = mem[idx(i+1, mode1)]
                p2 = mem[idx(i+2, mode2)]
                addr = idx(i+3, mode3)
                mem[addr] = p1*p2
                i+=4

            #i+=4 # steps forward 4 steps to next opcode.
            if op_code == 99:
                break # Halts when encounter opcode 99.
        return mem



if __name__ == '__main__':
    with open('2019/2/input.txt', encoding='utf8') as f:
        data = list(map(int, f.read().split(',')))
    
    last_state = [12, 2]
    for idx, v in enumerate(last_state):
        data[idx+1] = v
    
    icp = int_code_interpreter(data)
    print('Answer:', icp.execute()[0])