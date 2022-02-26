from .Data import Data

class Rgb(Data):
    def __init__(self):
        super().__init__()

    def th1(self): return self.TH("th1")
    def th2(self): return self.TH("th2")
    def th3(self): return self.TH("th3")
    def bn1(self): return self.TH("bn1")
    def bn2(self): return self.TH("bn2")

    def hx_th1(self): return self.TH_HEX(self.TH("th1"))
    def hx_th2(self): return self.TH_HEX(self.TH("th2"))
    def hx_th3(self): return self.TH_HEX(self.TH("th3"))
    def hx_bn1(self): return self.TH_HEX(self.TH("bn1"))
    def hx_bn2(self): return self.TH_HEX(self.TH("bn2"))

    def vert(self): return 78, 194, 58
    def rouge(self): return 199, 60, 90
