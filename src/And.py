from src.Bit import Bit


class And:
    def __init__(self, inA: Bit, inB: Bit):
        self.inA = inA
        self.inB = inB
        self.out = Bit()
        self.update()
        
    def update(self):
        self.out.value = self.inA.value and self.inB.value
        
        
