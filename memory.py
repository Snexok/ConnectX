from collections import deque
from random import sample

class Memory():
    def __init__(self, batch_size):
        self.memory = deque(maxlen=batch_size)
    def memorize(self, state):
        self.memory.append(state)
    def sample(self, batch_size):
        return sample(self.memory, batch_size)
    def __len__(self):
        return len(self.memory)
    def __eq__(self, other):
        if len(self.memory) == other:
            return True
        return False
    def __str__(self):
        return str(self.memory) 