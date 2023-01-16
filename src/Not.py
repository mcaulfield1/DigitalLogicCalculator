from src.Bit import Bit


class Not:
    def __init__(self, inA: Bit):
        self.inA = inA
        self.out = Bit()
        self.update()

    def update(self):
        self.out.value = not(self.inA.value)
