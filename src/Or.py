from src.Bit import Bit


class Or:
    def __init__(self, inA: Bit, inB: Bit):
        self.inA = inA
        self.inB = inB
        self.out = Bit()
        self.update()

    def update(self):
        self.out.value = self.inA.value or self.inB.value
