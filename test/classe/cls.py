from Combo_box import Combo_box


class _base:
    class rtn(Combo_box):
        def __init__(self, colors_type):
            super().__init__(
                colors_type=colors_type,
                colors=(10, 10, 10),
                dim="dim1",
                img="img")


    def th(self): self.rtn(colors_type="th")
    def tr(self): self.rtn(colors_type="tr")



_base().tr()
