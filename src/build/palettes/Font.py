from .data.Data import Data

class Font(Data):
    def __init__(self, grp="font"):
        super().__init__(grp)

    def h1(self): return self.GET_VAL("h1")
    def h2(self): return self.GET_VAL("h2")
    def h3(self): return self.GET_VAL("h3")
    def h4(self): return self.GET_VAL("h4")
    def h5(self): return self.GET_VAL("h5")
