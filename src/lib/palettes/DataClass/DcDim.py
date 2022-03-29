"""
DcDim.%class(
    fixed_width: int = PaDim.% \n
    fixed_height: int = PaDim.% \n
    minimum_width: int = PaDim.% \n
    minimum_height: int = PaDim.% \n
    maximum_width: int = PaDim.% \n
    maximum_height: int = PaDim.%)
"""

from dataclasses import dataclass


@dataclass
class Base:

    fixed_width: int = None
    fixed_height: int = None

    minimum_width: int = None
    minimum_height: int = None

    maximum_width: int = None
    maximum_height: int = None


    def __post_init__(self):
        if self.fixed_width:
            self.minimum_width = self.fixed_width
            self.maximum_width = self.fixed_width

        if self.fixed_height:
            self.minimum_height = self.fixed_height
            self.maximum_height = self.fixed_height
