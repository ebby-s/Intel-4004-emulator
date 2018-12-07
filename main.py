import sys, translator, executor, consolex

class EnhancedExecutor(executor.Executor, consolex.Consolex):
    
    def printRegs(self):
        print(' '.join([str(r) for r in self.regs]))
        print("acc=%d, cy=%d, ip=%d, dp=%d, cycles=%d" % (self.acc, self.cy, self.ip, self.dp, self.cycles))
    
    def printMemory(self, rows, cols):
        for row in range(rows):
            for col in range(cols):
                print("%X" % self.memory[row * cols + col])
            print()

    def c_3ff(self):
        self.printRegs()

    def c_3fe(self):
        self.printMemory(8, 32)

    def c_3fd(self):
        self.printMemory(4, 16)

def loadSource(fileName):
    f = open(fileName)
    lines = f.readlines()
    f.close()
    return lines

def fetchState(cpu):
    for i in range(2, len(sys.argv)):
        cpu.regs[i - 2] = int(sys.argv[i])

def main():
    try:
        src = loadSource(input("Enter filename: "))
        prg = translator.translate(src)
        cpu = EnhancedExecutor()
        fetchState(cpu)
        cpu.run(prg)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)


if __name__ == '__main__':
    while True:
        main()
        input()
