from src.Bit import Bit
from src.And import And
from src.Not import Not


class Nand:
    def __init__(self, inA: Bit, inB: Bit):
        self.inA = inA
        self.inB = inB
        self.And = And(inA, inB)
        self.Not = Not(self.And.out)
        self.out = self.Not.out
        self.update()

    def update(self):
        self.out.value = self.Not.out.value

