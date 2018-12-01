import numpy as np

StateMachine = {
    'A': {
        0: {'val': 1, 'direction': 'r', 'next':'B'},
        1: {'val': 0, 'direction': 'l', 'next':'B'}
    },
    'B': {
        0: {'val': 1, 'direction': 'l', 'next':'C'},
        1: {'val': 0, 'direction': 'r', 'next':'E'}
    },
    'C': {
        0: {'val': 1, 'direction': 'r', 'next':'E'},
        1: {'val': 0, 'direction': 'l', 'next':'D'}
    },
    'D': {
        0: {'val': 1, 'direction': 'l', 'next':'A'},
        1: {'val': 1, 'direction': 'l', 'next':'A'}
    },
    'E': {
        0: {'val': 0, 'direction': 'r', 'next':'A'},
        1: {'val': 0, 'direction': 'r', 'next':'F'}
    },
    'F': {
        0: {'val': 1, 'direction': 'r', 'next':'E'},
        1: {'val': 1, 'direction': 'r', 'next':'A'}
    }
}

class TuringMachine(object):
    def __init__(self,initial_state ):
        self.tape= np.zeros(128)
        self.cursor = int(len(self.tape)/2)
        self.state=initial_state

    def curr_val(self):
        return self.tape[self.cursor]

    def set_curr_val(self,val):
        self.tape[self.cursor] = val

    def grow_tape(self,direction):
        if direction == 'r':
            self.tape = np.append(self.tape, np.zeros(128))
        else:
            self.tape = np.insert(self.tape,0,np.zeros(128), axis=0)
            self.cursor += 128

    def move(self,direction):
        if direction == 'l':
            if self.cursor == 0:
                self.grow_tape('l')
            self.cursor -= 1
        else:
            if self.cursor == len(self.tape):
                self.grow_tape('r')
            self.cursor += 1

    def dchecksum(self):
        return np.count_nonzero(self.tape)

tm = TuringMachine('A')
steps = 12683008

for i in range(steps):
    rule = StateMachine[tm.state]
    curr_val = tm.curr_val()
    new_val = rule[curr_val]['val']
    next_state = rule[curr_val]['next']
    direction = rule[curr_val]['direction']

    tm.set_curr_val(new_val)
    tm.state = next_state
    tm.move(direction)
    print(" Tape Length:", len(tm.tape), "Cursor:", tm.cursor, "progress:", int((i/steps) * 100),"%", "\r", end='')

print()
print("Checksum:", tm.dchecksum())

