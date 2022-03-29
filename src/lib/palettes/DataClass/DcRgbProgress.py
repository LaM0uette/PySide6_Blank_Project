"""
DcRgbProgress.%class(
    gen = PaRgb.%

    base: tuple = PaRgb.%
    hover: tuple = PaRgb.%
    texte: tuple = PaRgb.%
    texte_hover: tuple = PaRgb.%
    chunk: tuple = PaRgb.%
    chunk_hover: tuple = PaRgb.%
"""
from dataclasses import dataclass

from src.lib.palettes import *


@dataclass
class Base:
    gen: tuple = None

    base: tuple = PaRgb.TH1
    hover: tuple = PaRgb.BN1
    texte: tuple = PaRgb.TH3
    texte_hover: tuple = PaRgb.TH3
    chunk: tuple = PaRgb.TH1
    chunk_hover: tuple = PaRgb.BN1


    def __post_init__(self):
        if self.gen:
            self.base = self.gen
            self.hover = self.gen
            self.texte = self.gen
            self.texte_hover = self.gen
            self.chunk = self.gen
            self.chunk_hover = self.gen
