from .data.Data import Data

class StyleBase(Data):
    def __init__(self, grp="wg"):
        super().__init__(grp)

    def bd(self): return self.GET_VAL("bd")
    def x_ico(self): return self.GET_VAL("x_ico")
    def X_ICO(self): return self.GET_VAL("X_ICO")
