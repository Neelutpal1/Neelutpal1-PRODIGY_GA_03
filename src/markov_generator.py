import random

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.model = {}

    def train(self, text):
        for i in range(len(text) - self.order):
            prefix = text[i:i+self.order]
            suffix = text[i+self.order]
            if prefix not in self.model:
                self.model[prefix] = []
            self.model[prefix].append(suffix)

    def generate(self, length=100):
        start = random.choice(list(self.model.keys()))
        result = start
        for _ in range(length):
            prefix = result[-self.order:]
            next_char = random.choice(self.model.get(prefix, ' '))
            result += next_char
        return result
