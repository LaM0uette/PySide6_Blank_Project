from .data.Data import Data

class Dim(Data):
    def __init__(self, grp="dimension"):
        super().__init__(grp)

    def h0(self): return self.GET_VAL("h0")
    def h1(self): return self.GET_VAL("h1")
    def h2(self): return self.GET_VAL("h2")
    def h3(self): return self.GET_VAL("h3")
    def h4(self): return self.GET_VAL("h4")
    def h5(self): return self.GET_VAL("h5")
    def h6(self): return self.GET_VAL("h6")
    def h7(self): return self.GET_VAL("h7")
    def h8(self): return self.GET_VAL("h8")
    def h9(self): return self.GET_VAL("h9")
    def h10(self): return self.GET_VAL("h10")

