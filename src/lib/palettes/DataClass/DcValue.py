"""
DcValue.%class(
    min: int = %
    max: int = %
    step: int = %)
"""

from dataclasses import dataclass


@dataclass
class Base:

    min: int = 0
    max: int = 100
    step: int = 1
    page_step: int = 10
